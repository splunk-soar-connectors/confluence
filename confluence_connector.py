# File: confluence_connector.py
#
# Copyright (c) 2019-2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Phantom App imports

import json

import phantom.app as phantom
import requests
from bs4 import BeautifulSoup
from phantom import vault
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector


DEFAULT_REQUEST_TIMEOUT = 30  # In seconds


class RetVal(tuple):
    def __new__(cls, val1, val2):
        return tuple.__new__(RetVal, (val1, val2))


class ConfluenceConnector(BaseConnector):
    def __init__(self):
        super().__init__()
        self._state = None
        self._base_url = None
        self._base_path = None
        self._username = None
        self._api_token = None
        self._verify = None

    def _process_response(self, r, action_result):
        action_result.add_debug_data({"r_status_code": r.status_code, "r_text": r.text, "r_headers": r.headers})

        content_type = r.headers.get("Content-Type", "").lower()

        if "json" in content_type:
            return self._process_json_response(r, action_result)

        if "html" in content_type:
            return self._process_html_response(r, action_result)

        if not r.text:
            return self._process_empty_response(r, action_result)

        message = f"Cannot process response. Status Code: {r.status_code}, Response: {r.text[:500]}"
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_empty_response(self, response, action_result):
        if response.status_code == 200:
            return RetVal(phantom.APP_SUCCESS, {})
        return RetVal(action_result.set_status(phantom.APP_ERROR, "Empty response with no headers"), None)

    def _process_html_response(self, response, action_result):
        try:
            soup = BeautifulSoup(response.text, "html.parser")
            error_text = soup.get_text(strip=True)
        except Exception:
            error_text = "Unable to parse HTML response."

        message = f"HTML Response. Status Code: {response.status_code}, Error: {error_text[:500]}"
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_json_response(self, r, action_result):
        try:
            resp_json = r.json()
        except Exception as e:
            return RetVal(action_result.set_status(phantom.APP_ERROR, f"Failed to parse JSON: {e!s}"), None)

        if 200 <= r.status_code < 400:
            return RetVal(phantom.APP_SUCCESS, resp_json)

        error_message = resp_json.get("message", r.text[:500])
        return RetVal(action_result.set_status(phantom.APP_ERROR, f"Error from server: {error_message}"), None)

    def _make_rest_call(self, endpoint, action_result, headers=None, params=None, data=None, files=None, method="get"):
        try:
            request_func = getattr(requests, method.lower())
        except AttributeError:
            return RetVal(action_result.set_status(phantom.APP_ERROR, f"Invalid HTTP method: {method}"), None)

        url = f"{self._base_url}{self._base_path}/{endpoint.lstrip('/')}"
        self.save_progress(f"Making {method.upper()} request to URL: {url}")

        try:
            response = request_func(
                url,
                auth=(self._username, self._api_token),
                json=data,
                headers=headers,
                verify=self._verify,
                params=params,
                files=files,
                timeout=DEFAULT_REQUEST_TIMEOUT,
            )
        except Exception as e:
            return RetVal(action_result.set_status(phantom.APP_ERROR, f"Connection error: {e!s}"), None)

        self.save_progress(f"Response Status Code: {response.status_code}")
        return self._process_response(response, action_result)

    def _handle_test_connectivity(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        headers = {"Accept": "application/json"}
        params = {"limit": 1}  # Limit to 1 result for testing connectivity

        ret_val, _ = self._make_rest_call("/spaces", action_result, headers=headers, params=params, method="get")

        if phantom.is_fail(ret_val):
            self.save_progress("Test Connectivity Failed")
            return action_result.get_status()

        self.save_progress("Test Connectivity Passed")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_page(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))

        if param["space_id"].isdigit():
            space_id = param["space_id"]
        else:
            space_id = self._get_space_id(param["space_id"], action_result)
            if not space_id:
                return action_result.get_status()

        title = param["title"]
        parent_page_id = param.get("parent_page_id", "")
        body = param.get("body", "")

        data = {
            "type": "page",
            "spaceId": space_id,
            "title": title,
            "parentId": parent_page_id,
            "body": {"storage": {"value": body, "representation": "storage"}},
        }

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        ret_val, response = self._make_rest_call("/pages", action_result, headers=headers, data=data, method="post")

        if phantom.is_fail(ret_val):
            self.save_progress(f"Failed to create page: {action_result.get_message()}")
            return action_result.get_status()

        action_result.add_data(response)
        action_result.update_summary({"page_id": response.get("id")})
        self.save_progress("Page created successfully.")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_comment(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))

        page_id = param["page_id"]
        body = param.get("body", "")

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        data = {"pageId": page_id, "body": {"storage": {"value": body, "representation": "storage"}}}

        ret_val, response = self._make_rest_call("/footer-comments", action_result, headers=headers, data=data, method="post")

        if phantom.is_fail(ret_val):
            self.save_progress(f"Failed to add comment: {action_result.get_message()}")
            return action_result.get_status()

        action_result.add_data(response)
        action_result.update_summary({"comment_id": response.get("id")})
        self.save_progress("Comment added successfully.")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_page(self, param):
        """Retrieve a page by space key and title."""
        action_result = self.add_action_result(ActionResult(dict(param)))

        if param["space_id"].isdigit():
            space_id = param["space_id"]
        else:
            space_id = self._get_space_id(param["space_id"], action_result)
            if not space_id:
                return action_result.get_status()

        title = param["title"]

        params = {"body-format": "storage", "space-id": space_id, "title": title}

        headers = {"Accept": "application/json"}

        # Make the GET request to fetch the page
        ret_val, response = self._make_rest_call("/pages", action_result, headers=headers, params=params, method="get")

        if phantom.is_fail(ret_val):
            self.save_progress(f"Failed to retrieve page: {action_result.get_message()}")
            return action_result.get_status()

        # Process the response
        results = response.get("results", [])
        if not results:
            self.save_progress("Page not found")
            action_result.add_data(response)
            return action_result.set_status(phantom.APP_ERROR, "Page not found")

        # Add the first page result to data
        action_result.add_data(results[0])
        action_result.update_summary({"page_id": results[0].get("id")})
        self.save_progress("Page retrieved successfully.")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_child_pages(self, param):
        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Access action parameters passed in the 'param' dictionary

        # Required values can be accessed directly
        page_id = param["page_id"]
        sort = param.get("sort", "")
        limit = param.get("limit", "")

        params = {}

        if sort:
            params["sort"] = sort
        if limit:
            params["limit"] = limit

        # Optional values should use the .get() function
        # optional_parameter = param.get('optional_parameter', 'default_value')

        # make rest call
        ret_val, response = self._make_rest_call(f"/pages/{page_id}/direct-children", action_result, params=params, headers=None)

        if phantom.is_fail(ret_val):
            # the call to the 3rd party device or service failed, action result should contain all the error details
            # for now the return is commented out, but after implementation, return from here
            # return action_result.get_status()
            pass

        summary = action_result.update_summary({})
        if len(response["results"]) > 0:
            self.save_progress("Page Found")
            for result in response["results"]:
                summary["children"] = result["title"]

        else:
            self.save_progress("Page not found")
            summary["children"] = None
            action_result.add_data(response)
            return action_result.set_status(phantom.APP_ERROR, "Page not found")

        action_result.add_data(response)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_attachement(self, param):
        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Access action parameters passed in the 'param' dictionary

        # Required values can be accessed directly
        page_id = param["page_id"]
        file_hash = param["file_hash"]

        success, message, info = vault.vault_info(vault_id=file_hash)
        if not success:
            self.save_progress(f"Failed to retrieve file from vault: {message}")
            return action_result.set_status(phantom.APP_ERROR, f"Failed to retrieve file from vault: {message}")

        # Optional values should use the .get() function
        file_name = param.get("file_name", "")
        if not file_name:
            file_name = info[0]["name"]

        file_path = info[0]["path"]
        content_type = "multipart/form-data"

        _headers = {"X-Atlassian-Token": "no-check"}

        f = open(file_path, "rb")
        file_data = f.read()
        f.close()

        files = {"file": (file_name, file_data, content_type), "minorEdit": "true"}

        # utilizes v1 api
        self._base_path = "/rest/api"
        # make rest call
        ret_val, response = self._make_rest_call(
            f"/content/{page_id}/child/attachment", action_result, params=None, headers=_headers, files=files, method="post"
        )

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        # Add the response into the data section
        # action_result.add_data(response)

        # Add a dictionary that is made up of the most important values from data into the summary
        summary = action_result.update_summary({})
        if len(response["results"]) > 0:
            self.save_progress("Attachment added.")
            summary["attachment_id"] = response["results"][0]["id"]

        else:
            self.save_progress("Attachment not added.")
            summary["attachment_id"] = None
            action_result.add_data(response)
            return action_result.set_status(phantom.APP_ERROR, "Attachment failed.")

        # Return success, no need to set the message, only the status
        # BaseConnector will create a textual message based off of the summary dictionary
        action_result.add_data(response)
        self.save_progress(f"In action handler for: {self.get_action_identifier()}. Action Status: {phantom.APP_SUCCESS}")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _get_space_id(self, space_key, action_result):
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")

        # Access action parameters passed in the 'param' dictionary
        _headers = {"Accept": "application/json"}

        params = {"keys": space_key}

        # Optional values should use the .get() function
        # optional_parameter = param.get('optional_parameter', 'default_value')

        # make rest call
        ret_val, response = self._make_rest_call("/spaces", action_result, params=params, headers=_headers)

        if phantom.is_fail(ret_val):
            # the call to the 3rd party device or service failed, action result should contain all the error details
            # for now the return is commented out, but after implementation, return from here
            # return action_result.get_status()
            pass

        # Now post process the data,  uncomment code as you deem fit
        # summary = action_result.update_summary({})
        if len(response["results"]) > 0:
            self.save_progress("Space found")
            for result in response["results"]:
                space_id = result["id"]

        else:
            self.save_progress("Space not found")
            return action_result.set_status(phantom.APP_ERROR, "Space not found")

        # action_result.add_data(response)
        return space_id

    def handle_action(self, param):
        action_id = self.get_action_identifier()
        self.debug_print(f"Action ID: {action_id}")

        action_mapping = {
            "test_connectivity": self._handle_test_connectivity,
            "create_page": self._handle_create_page,
            "add_comment": self._handle_add_comment,
            "get_page": self._handle_get_page,
            "get_child_pages": self._handle_get_child_pages,
            "create_attachment": self._handle_create_attachement,
        }

        action = action_mapping.get(action_id)
        if action:
            return action(param)

        return phantom.APP_ERROR

    def initialize(self):
        self._state = self.load_state()
        config = self.get_config()

        self._base_url = config["base_url"].rstrip("/")
        self._base_path = self._base_path = config.get("base_path", "").strip("/")
        # Re-add a leading slash to base_path if not empty
        if self._base_path:
            self._base_path = f"/{self._base_path}"
        self._username = config.get("username")
        self._api_token = config.get("apitoken")
        self._verify = config.get("verify_server_cert", False)

        return phantom.APP_SUCCESS

    def finalize(self):
        self.save_state(self._state)
        return phantom.APP_SUCCESS


if __name__ == "__main__":
    import argparse
    import sys

    argparser = argparse.ArgumentParser()
    argparser.add_argument("input_test_json", help="Input Test JSON file")
    args = argparser.parse_args()

    with open(args.input_test_json) as f:
        input_data = json.load(f)

    connector = ConfluenceConnector()
    connector.print_progress_message = True
    result = connector.handle_action(input_data)
    print(json.dumps(result, indent=4))

    sys.exit(0)
