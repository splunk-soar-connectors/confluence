# File: confluence_connector.py
# Copyright (c) 2019-2021 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.

# Phantom App imports
import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

import requests
import json
from bs4 import BeautifulSoup


class RetVal(tuple):
    def __new__(cls, val1, val2):
        return tuple.__new__(RetVal, (val1, val2))


class ConfluenceConnector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(ConfluenceConnector, self).__init__()

        self._state = None
        self._base_url = None
        self._username = None
        self._password = None
        self._verify = None

    def _process_empty_response(self, response, action_result):

        if response.status_code == 200:
            return RetVal(phantom.APP_SUCCESS, {})

        return RetVal(action_result.set_status(phantom.APP_ERROR, "Empty response and no information in the header"),
                      None)

    def _process_html_response(self, response, action_result):

        # An html response, treat it like an error
        status_code = response.status_code

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            error_text = soup.text
            split_lines = error_text.split('\n')
            split_lines = [x.strip() for x in split_lines if x.strip()]
            error_text = '\n'.join(split_lines)
        except:
            error_text = "Cannot parse error details"

        message = "Status Code: {0}. Data from server:\n{1}\n".format(status_code,
                                                                      error_text)

        message = message.replace('{', '{{').replace('}', '}}')

        if len(message) > 500:
            message = 'Basic Authentication Failure - Reason : AUTHENTICATED_FAILED. This request requires HTTP authentication.'

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_json_response(self, r, action_result):

        # Try a json parse
        try:
            resp_json = r.json()
        except Exception as e:
            return RetVal(
                action_result.set_status(phantom.APP_ERROR, "Unable to parse JSON response. Error: {0}".format(str(e))),
                None)

        if 200 <= r.status_code < 399:
            return RetVal(phantom.APP_SUCCESS, resp_json)

        msg = ''
        if resp_json.get("message"):
            msg = resp_json.get("message").strip('.').encode("utf-8")

        if resp_json.get("data", {}).get("authorized") is not None:
            msg = "{0}Authorized: {1}".format("{0}. ".format(msg) if msg else "",
                                              resp_json.get("data", {}).get("authorized"))

        if resp_json.get("data", {}).get("errors"):
            for error in resp_json.get("data", {}).get("errors"):
                if error.get("message", {}).get("key"):
                    msg = "{}. {}".format(msg, error.get("message").get("key").strip('.').encode("utf-8"))

        if msg:
            message = "Error from server. Status Code: {0} Data from server: {1}".format(
                r.status_code, '{0}.'.format(msg.strip()))
        else:
            message = "Error from server. Status Code: {0} Data from server: {1}".format(
                r.status_code, r.text.replace('{', '{{').replace('}', '}}').encode('utf-8'))

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_response(self, r, action_result):

        # store the r_text in debug data, it will get dumped in the logs if the action fails
        if hasattr(action_result, 'add_debug_data'):
            action_result.add_debug_data({'r_status_code': r.status_code})
            action_result.add_debug_data({'r_text': r.text})
            action_result.add_debug_data({'r_headers': r.headers})

        # Process each 'Content-Type' of response separately

        # Process a json response
        if 'json' in r.headers.get('Content-Type', ''):
            return self._process_json_response(r, action_result)

        # Process an HTML response, Do this no matter what the api talks.
        # There is a high chance of a PROXY in between phantom and the rest of
        # world, in case of errors, PROXY's return HTML, this function parses
        # the error and adds it to the action_result.
        if 'html' in r.headers.get('Content-Type', ''):
            return self._process_html_response(r, action_result)

        # it's not content-type that is to be parsed, handle an empty response
        if not r.text:
            return self._process_empty_response(r, action_result)

        # everything else is actually an error at this point
        message = "Can't process response from server. Status Code: {0} Data from server: {1}".format(
            r.status_code, r.text.replace('{', '{{').replace('}', '}}'))

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _make_rest_call(self, endpoint, action_result, headers=None, params=None, data=None, method="get"):

        resp_json = None

        try:
            request_func = getattr(requests, method)
        except AttributeError:
            return RetVal(action_result.set_status(phantom.APP_ERROR, "Invalid method: {0}".format(method)), resp_json)

        # Create a URL to connect to
        url = "{}{}".format(self._base_url, endpoint)

        try:
            r = request_func(
                url,
                auth=(self._username, self._password),
                json=data,
                headers=headers,
                verify=self._verify,
                params=params)
        except Exception as e:
            try:
                return RetVal(action_result.set_status(phantom.APP_ERROR,
                                                       "Error Connecting to server. Details: {0}".format(
                                                           str(e).encode('utf-8'))), resp_json)
            except:
                return RetVal(action_result.set_status(phantom.APP_ERROR,
                                                       "Error Connecting to server. Please verify the asset configuration parameters."),
                              resp_json)

        return self._process_response(r, action_result)

    def _handle_test_connectivity(self, param):

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # make rest call
        ret_val, _ = self._make_rest_call('/rest/api/content', action_result, params=None, headers=None)

        if phantom.is_fail(ret_val):
            # the call to the 3rd party device or service failed, action result should contain all the error details
            # so just return from here
            self.save_progress("Test Connectivity Failed")
            return action_result.get_status()

        # Return success
        self.save_progress("Test Connectivity Passed")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_comment(self, param):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(param)))

        page_id = param['page_id']
        body = param.get('body', '')

        _headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        data = {
            "type": "comment",
            "container": {
                "id": page_id,
                "type": "page",
                "status": "current"
            },
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }

        ret_val, response = self._make_rest_call('/rest/api/content', action_result, params=None, headers=_headers,
                                                 data=data, method="post")

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        # Add a dictionary that is made up of the most important values from data into the summary
        summary = action_result.update_summary({})
        summary['comment_id'] = response["id"]

        # Return success, no need to set the message, only the status
        # BaseConnector will create a textual message based off of the summary dictionary
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_page(self, param):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(param)))

        space_key = param['space_key']
        title = param['title']

        data = {
            'type': 'page',
            'space': {
                'key': space_key
            },
            'title': title
        }
        ancestor_id = param.get('parent_page_id')
        if ancestor_id:
            data['ancestors'] = [{'id': ancestor_id}]

        ret_val, response = self._make_rest_call('/rest/api/content', action_result, params=None, headers=None,
                                                 data=data, method="post")

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        # Add a dictionary that is made up of the most important values from data into the summary
        summary = action_result.update_summary({})
        summary['page_id'] = response["id"]

        # Return success, no need to set the message, only the status
        # BaseConnector will create a textual message based off of the summary dictionary
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_page(self, param):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        params = {
            'expand': "body.storage",
            'spaceKey': param['space_key'],
            'title': param['title']
        }

        # make rest call
        ret_val, response = self._make_rest_call('/rest/api/content', action_result, params=params, headers=None)

        if phantom.is_fail(ret_val):
            # the call to the 3rd party device or service failed, action result should contain all the error details
            # so just return from here
            return action_result.get_status()

        # Now post process the data,  uncomment code as you deem fit
        summary = action_result.update_summary({})
        if len(response['results']) > 0:
            self.save_progress("Page found")
            summary['page_id'] = response['results'][0]['id']
        else:
            self.save_progress("Page not found")
            summary['page_id'] = None
            action_result.add_data(response)
            return action_result.set_status(phantom.APP_ERROR, "Page not found")

        action_result.add_data(response)
        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):

        # break at run-time
        # import web_pdb
        # web_pdb.set_trace()

        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if action_id == 'test_connectivity':
            ret_val = self._handle_test_connectivity(param)

        elif action_id == 'add_comment':
            ret_val = self._handle_add_comment(param)

        elif action_id == 'create_page':
            ret_val = self._handle_create_page(param)

        elif action_id == 'get_page':
            ret_val = self._handle_get_page(param)

        return ret_val

    def initialize(self):

        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        # get the asset config
        config = self.get_config()

        # Access values in asset config by the name

        self._base_url = config['base_url']
        if self._base_url[-1] == '/':
            self._base_url = self._base_url[:-1]
        self._username = config.get('username')
        self._password = config.get('password')
        self._verify = config.get('verify_server_cert', False)

        return phantom.APP_SUCCESS

    def finalize(self):

        # Save the state, this data is saved across actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


if __name__ == '__main__':

    import sys
    import pudb
    import argparse

    pudb.set_trace()

    argparser = argparse.ArgumentParser()

    argparser.add_argument('input_test_json', help='Input Test JSON file')
    argparser.add_argument('-u', '--username', help='username', required=False)
    argparser.add_argument('-p', '--password', help='password', required=False)

    args = argparser.parse_args()
    session_id = None

    username = args.username
    password = args.password

    if username is not None and password is None:
        # User specified a username but not a password, so ask
        import getpass

        password = getpass.getpass("Password: ")

    if username and password:
        try:
            login_url = BaseConnector._get_phantom_base_url() + "login"
            print("Accessing the Login page")
            r = requests.get(login_url, verify=False)
            csrftoken = r.cookies['csrftoken']

            data = dict()
            data['username'] = username
            data['password'] = password
            data['csrfmiddlewaretoken'] = csrftoken

            headers = {
                'Cookie': "csrftoken={}".format(csrftoken),
                'Referer': login_url
            }

            print("Logging into Platform to get the session id")
            r2 = requests.post(login_url, verify=False, data=data, headers=headers)
            session_id = r2.cookies['sessionid']
        except Exception as e:
            print("Unable to get session id from the platform. Error: " + str(e))
            exit(1)

    if len(sys.argv) < 2:
        print("No test json specified as input")
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = ConfluenceConnector()
        connector.print_progress_message = True

        if session_id is not None:
            in_json['user_session_token'] = session_id

        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    exit(0)
