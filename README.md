# Confluence

Publisher: Splunk \
Connector Version: 3.0.3 \
Product Vendor: Atlassian \
Product Name: Confluence \
Minimum Product Version: 6.3.0

This app supports a variety of actions for content generation in Confluence

### Configuration variables

This table lists the configuration variables required to operate Confluence. These variables are specified when configuring a Confluence asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** | required | string | Base URL |
**verify_server_cert** | optional | boolean | Verify server SSL certificate |
**username** | required | string | Username |
**apitoken** | required | password | API Token |
**base_path** | optional | string | Base Path |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using the supplied configuration \
[add comment](#action-add-comment) - Add a comment to an existing page \
[create page](#action-create-page) - Create a page in the space \
[get page](#action-get-page) - Get a page by name

## action: 'test connectivity'

Validate the asset configuration for connectivity using the supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'add comment'

Add a comment to an existing page

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**page_id** | required | ID of the page to post comment | string | `confluence page id` |
**body** | required | Comment body text | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.body | string | | IP lookup results on 1.1.1.1:\\n \\n US\\n Country Name\\n 37.751\\n -97.822 |
action_result.parameter.page_id | string | `confluence page id` | 1703966 |
action_result.data.\*.\_expandable.children | string | | /rest/api/content/1703967/child |
action_result.data.\*.\_expandable.descendants | string | | /rest/api/content/1703967/descendant |
action_result.data.\*.\_expandable.metadata | string | | |
action_result.data.\*.\_expandable.operations | string | | |
action_result.data.\*.\_expandable.restrictions | string | | /rest/api/content/1703967/restriction/byOperation |
action_result.data.\*.\_links.base | string | `url` | http://192.16.195.173:9090 |
action_result.data.\*.\_links.collection | string | | /rest/api/content |
action_result.data.\*.\_links.context | string | | |
action_result.data.\*.\_links.self | string | `url` | http://192.168.195.173:9090/rest/api/content/1703967 |
action_result.data.\*.\_links.webui | string | | /display/TST/Shift+Log+3?focusedCommentId=1703967#comment-1703967 |
action_result.data.\*.body.\_expandable.anonymous_export_view | string | | |
action_result.data.\*.body.\_expandable.editor | string | | |
action_result.data.\*.body.\_expandable.export_view | string | | |
action_result.data.\*.body.\_expandable.styled_view | string | | |
action_result.data.\*.body.\_expandable.view | string | | |
action_result.data.\*.body.storage.\_expandable.content | string | | /rest/api/content/1703967 |
action_result.data.\*.body.storage.representation | string | | storage |
action_result.data.\*.body.storage.value | string | | IP lookup results on 8.8.8.8:\\n \\n US\\n Country Name\\n 37.751\\n -97.822 |
action_result.data.\*.container.\_expandable.ancestors | string | | |
action_result.data.\*.container.\_expandable.body | string | | |
action_result.data.\*.container.\_expandable.children | string | | /rest/api/content/1703966/child |
action_result.data.\*.container.\_expandable.container | string | | /rest/api/space/TST |
action_result.data.\*.container.\_expandable.descendants | string | | /rest/api/content/1703966/descendant |
action_result.data.\*.container.\_expandable.metadata | string | | |
action_result.data.\*.container.\_expandable.operations | string | | |
action_result.data.\*.container.\_expandable.restrictions | string | | /rest/api/content/1703966/restriction/byOperation |
action_result.data.\*.container.\_expandable.space | string | | /rest/api/space/TST |
action_result.data.\*.container.\_links.edit | string | | /pages/resumedraft.action?draftId=1703966 |
action_result.data.\*.container.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/content/1703966 |
action_result.data.\*.container.\_links.tinyui | string | | /x/HgAa |
action_result.data.\*.container.\_links.webui | string | | /display/TST/Shift+Log+3 |
action_result.data.\*.container.extensions.position | string | | none |
action_result.data.\*.container.history.\_expandable.contributors | string | | |
action_result.data.\*.container.history.\_expandable.lastUpdated | string | | |
action_result.data.\*.container.history.\_expandable.nextVersion | string | | |
action_result.data.\*.container.history.\_expandable.previousVersion | string | | |
action_result.data.\*.container.history.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/content/1703966/history |
action_result.data.\*.container.history.createdBy.\_expandable.status | string | | |
action_result.data.\*.container.history.createdBy.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/user?key=4028fa8161b977bf0161b97970730000 |
action_result.data.\*.container.history.createdBy.displayName | string | | Test User |
action_result.data.\*.container.history.createdBy.profilePicture.height | numeric | | 48 |
action_result.data.\*.container.history.createdBy.profilePicture.isDefault | boolean | | True False |
action_result.data.\*.container.history.createdBy.profilePicture.path | string | | /images/icons/profilepics/default.svg |
action_result.data.\*.container.history.createdBy.profilePicture.width | numeric | | 48 |
action_result.data.\*.container.history.createdBy.type | string | | known |
action_result.data.\*.container.history.createdBy.userKey | string | `md5` | 4028fa8161b977bf0161b97970730000 |
action_result.data.\*.container.history.createdBy.username | string | `user name` | admin |
action_result.data.\*.container.history.createdDate | string | | 2018-03-04T08:42:52.264-08:00 |
action_result.data.\*.container.history.latest | boolean | | True False |
action_result.data.\*.container.id | string | | 1703966 |
action_result.data.\*.container.status | string | | current |
action_result.data.\*.container.title | string | | Shift Log 3 |
action_result.data.\*.container.type | string | | page |
action_result.data.\*.container.version.\_expandable.content | string | | /rest/api/content/1703966 |
action_result.data.\*.container.version.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/content/1703966/version/1 |
action_result.data.\*.container.version.by.\_expandable.status | string | | |
action_result.data.\*.container.version.by.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/user?key=4028fa8161b977bf0161b97970730000 |
action_result.data.\*.container.version.by.displayName | string | | Test User |
action_result.data.\*.container.version.by.profilePicture.height | numeric | | 48 |
action_result.data.\*.container.version.by.profilePicture.isDefault | boolean | | True False |
action_result.data.\*.container.version.by.profilePicture.path | string | | /images/icons/profilepics/default.svg |
action_result.data.\*.container.version.by.profilePicture.width | numeric | | 48 |
action_result.data.\*.container.version.by.type | string | | known |
action_result.data.\*.container.version.by.userKey | string | `md5` | 4028fa8161b977bf0161b97970730000 |
action_result.data.\*.container.version.by.username | string | `user name` | admin |
action_result.data.\*.container.version.hidden | boolean | | True False |
action_result.data.\*.container.version.message | string | | |
action_result.data.\*.container.version.minorEdit | boolean | | True False |
action_result.data.\*.container.version.number | numeric | | 1 |
action_result.data.\*.container.version.when | string | | 2018-03-04T08:42:52.264-08:00 |
action_result.data.\*.extensions.\_expandable.resolution | string | | |
action_result.data.\*.extensions.location | string | | footer |
action_result.data.\*.history.\_expandable.contributors | string | | |
action_result.data.\*.history.\_expandable.lastUpdated | string | | |
action_result.data.\*.history.\_expandable.nextVersion | string | | |
action_result.data.\*.history.\_expandable.previousVersion | string | | |
action_result.data.\*.history.\_links.self | string | `url` | http://192.168.195.173:9090/rest/api/content/1703967/history |
action_result.data.\*.history.createdBy.\_expandable.status | string | | |
action_result.data.\*.history.createdBy.\_links.self | string | `url` | http://192.168.195.173:9090/rest/experimental/user?key=4028fa8161b977bf0161b97970730000 |
action_result.data.\*.history.createdBy.displayName | string | | Test User |
action_result.data.\*.history.createdBy.profilePicture.height | numeric | | 48 |
action_result.data.\*.history.createdBy.profilePicture.isDefault | boolean | | True False |
action_result.data.\*.history.createdBy.profilePicture.path | string | | /images/icons/profilepics/default.svg |
action_result.data.\*.history.createdBy.profilePicture.width | numeric | | 48 |
action_result.data.\*.history.createdBy.type | string | | known |
action_result.data.\*.history.createdBy.userKey | string | `md5` | 4028fa8161b977bf0161b97970730000 |
action_result.data.\*.history.createdBy.username | string | `user name` | admin |
action_result.data.\*.history.createdDate | string | | 2018-03-04T08:42:53.578-08:00 |
action_result.data.\*.history.latest | boolean | | True False |
action_result.data.\*.id | string | | 1703967 |
action_result.data.\*.space.\_expandable.description | string | | |
action_result.data.\*.space.\_expandable.homepage | string | | /rest/api/content/65601 |
action_result.data.\*.space.\_expandable.icon | string | | |
action_result.data.\*.space.\_expandable.metadata | string | | |
action_result.data.\*.space.\_links.self | string | `url` | http://192.168.195.173:9090/rest/api/space/TST |
action_result.data.\*.space.\_links.webui | string | | /display/TST |
action_result.data.\*.space.id | numeric | | 98307 |
action_result.data.\*.space.key | string | | TST |
action_result.data.\*.space.name | string | | TST |
action_result.data.\*.space.type | string | | global |
action_result.data.\*.status | string | | current |
action_result.data.\*.title | string | | Re: Shift Log 3 |
action_result.data.\*.type | string | | comment |
action_result.data.\*.version.\_expandable.content | string | | /rest/api/content/1703967 |
action_result.data.\*.version.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/content/1703967/version/1 |
action_result.data.\*.version.by.\_expandable.status | string | | |
action_result.data.\*.version.by.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/user?key=4028fa8161b977bf0161b97970730000 |
action_result.data.\*.version.by.displayName | string | | Test User |
action_result.data.\*.version.by.profilePicture.height | numeric | | 48 |
action_result.data.\*.version.by.profilePicture.isDefault | boolean | | True False |
action_result.data.\*.version.by.profilePicture.path | string | | /images/icons/profilepics/default.svg |
action_result.data.\*.version.by.profilePicture.width | numeric | | 48 |
action_result.data.\*.version.by.type | string | | known |
action_result.data.\*.version.by.userKey | string | `md5` | 4028fa8161b977bf0161b97970730000 |
action_result.data.\*.version.by.username | string | `user name` | admin |
action_result.data.\*.version.hidden | boolean | | True False |
action_result.data.\*.version.message | string | | |
action_result.data.\*.version.minorEdit | boolean | | True False |
action_result.data.\*.version.number | numeric | | 1 |
action_result.data.\*.version.when | string | | 2018-03-04T08:42:53.578-08:00 |
action_result.summary.comment_id | string | | 1703999 |
action_result.summary.important_data | string | | value |
action_result.message | string | | Important data: value |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'create page'

Create a page in the space

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**space_key** | required | Name of the space to create the page | string | `confluence space key` |
**title** | required | Page title | string | |
**parent_page_id** | optional | Parent page ID | string | `confluence page id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.parent_page_id | string | `confluence page id` | 1703966 |
action_result.parameter.space_key | string | `confluence space key` | TST |
action_result.parameter.title | string | | Shift Log |
action_result.data.\*.\_expandable.children | string | | /rest/api/content/1703942/child |
action_result.data.\*.\_expandable.descendants | string | | /rest/api/content/1703942/descendant |
action_result.data.\*.\_expandable.metadata | string | | |
action_result.data.\*.\_expandable.operations | string | | |
action_result.data.\*.\_expandable.restrictions | string | | /rest/api/content/1703942/restriction/byOperation |
action_result.data.\*.\_links.base | string | `url` | http://192.16.195.173:9090 |
action_result.data.\*.\_links.collection | string | | /rest/api/content |
action_result.data.\*.\_links.context | string | | |
action_result.data.\*.\_links.edit | string | | /pages/resumedraft.action?draftId=1703942 |
action_result.data.\*.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/content/1703942 |
action_result.data.\*.\_links.tinyui | string | | /x/BgAa |
action_result.data.\*.\_links.webui | string | | /display/TST/Shift+Log |
action_result.data.\*.ancestors.\*.\_expandable.ancestors | string | | |
action_result.data.\*.ancestors.\*.\_expandable.body | string | | |
action_result.data.\*.ancestors.\*.\_expandable.children | string | | /rest/api/content/20283427/child |
action_result.data.\*.ancestors.\*.\_expandable.container | string | | /rest/api/space/TC |
action_result.data.\*.ancestors.\*.\_expandable.descendants | string | | /rest/api/content/20283427/descendant |
action_result.data.\*.ancestors.\*.\_expandable.history | string | | /rest/api/content/20283427/history |
action_result.data.\*.ancestors.\*.\_expandable.metadata | string | | |
action_result.data.\*.ancestors.\*.\_expandable.operations | string | | |
action_result.data.\*.ancestors.\*.\_expandable.space | string | | /rest/api/space/TC |
action_result.data.\*.ancestors.\*.\_expandable.version | string | | |
action_result.data.\*.ancestors.\*.\_links.self | string | | http://localhost:8090/rest/api/content/20283427 |
action_result.data.\*.ancestors.\*.\_links.tinyui | string | | /x/I4A1AQ |
action_result.data.\*.ancestors.\*.\_links.webui | string | | /display/TC/New+test+page |
action_result.data.\*.ancestors.\*.extensions.position | string | | none |
action_result.data.\*.ancestors.\*.id | string | | 20283427 |
action_result.data.\*.ancestors.\*.status | string | | current |
action_result.data.\*.ancestors.\*.title | string | | New test page |
action_result.data.\*.ancestors.\*.type | string | | page |
action_result.data.\*.body.\_expandable.anonymous_export_view | string | | |
action_result.data.\*.body.\_expandable.editor | string | | |
action_result.data.\*.body.\_expandable.export_view | string | | |
action_result.data.\*.body.\_expandable.styled_view | string | | |
action_result.data.\*.body.\_expandable.view | string | | |
action_result.data.\*.body.storage.\_expandable.content | string | | /rest/api/content/1703942 |
action_result.data.\*.body.storage.representation | string | | storage |
action_result.data.\*.body.storage.value | string | | |
action_result.data.\*.container.\_expandable.description | string | | |
action_result.data.\*.container.\_expandable.homepage | string | | /rest/api/content/65601 |
action_result.data.\*.container.\_expandable.icon | string | | |
action_result.data.\*.container.\_expandable.metadata | string | | |
action_result.data.\*.container.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/space/TST |
action_result.data.\*.container.\_links.webui | string | | /display/TST |
action_result.data.\*.container.id | numeric | | 98307 |
action_result.data.\*.container.key | string | | TST |
action_result.data.\*.container.name | string | | TST |
action_result.data.\*.container.type | string | | global |
action_result.data.\*.extensions.position | string | | none |
action_result.data.\*.history.\_expandable.contributors | string | | |
action_result.data.\*.history.\_expandable.lastUpdated | string | | |
action_result.data.\*.history.\_expandable.nextVersion | string | | |
action_result.data.\*.history.\_expandable.previousVersion | string | | |
action_result.data.\*.history.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/content/1703942/history |
action_result.data.\*.history.createdBy.\_expandable.status | string | | |
action_result.data.\*.history.createdBy.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/user?key=4028fa8161b977bf0161b97970730000 |
action_result.data.\*.history.createdBy.displayName | string | | Test User |
action_result.data.\*.history.createdBy.profilePicture.height | numeric | | 48 |
action_result.data.\*.history.createdBy.profilePicture.isDefault | boolean | | True False |
action_result.data.\*.history.createdBy.profilePicture.path | string | | /images/icons/profilepics/default.svg |
action_result.data.\*.history.createdBy.profilePicture.width | numeric | | 48 |
action_result.data.\*.history.createdBy.type | string | | known |
action_result.data.\*.history.createdBy.userKey | string | `md5` | 4028fa8161b977bf0161b97970730000 |
action_result.data.\*.history.createdBy.username | string | `user name` | admin |
action_result.data.\*.history.createdDate | string | | 2018-03-04T07:13:16.603-08:00 |
action_result.data.\*.history.latest | boolean | | True False |
action_result.data.\*.id | string | | 1703942 |
action_result.data.\*.space.\_expandable.description | string | | |
action_result.data.\*.space.\_expandable.homepage | string | | /rest/api/content/65601 |
action_result.data.\*.space.\_expandable.icon | string | | |
action_result.data.\*.space.\_expandable.metadata | string | | |
action_result.data.\*.space.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/space/TST |
action_result.data.\*.space.\_links.webui | string | | /display/TST |
action_result.data.\*.space.id | numeric | | 98307 |
action_result.data.\*.space.key | string | | TST |
action_result.data.\*.space.name | string | | TST |
action_result.data.\*.space.type | string | | global |
action_result.data.\*.status | string | | current |
action_result.data.\*.title | string | | Shift Log |
action_result.data.\*.type | string | | page |
action_result.data.\*.version.\_expandable.content | string | | /rest/api/content/1703942 |
action_result.data.\*.version.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/content/1703942/version/1 |
action_result.data.\*.version.by.\_expandable.status | string | | |
action_result.data.\*.version.by.\_links.self | string | `url` | http://192.16.195.173:9090/rest/experimental/user?key=4028fa8161b977bf0161b97970730000 |
action_result.data.\*.version.by.displayName | string | | Test User |
action_result.data.\*.version.by.profilePicture.height | numeric | | 48 |
action_result.data.\*.version.by.profilePicture.isDefault | boolean | | True False |
action_result.data.\*.version.by.profilePicture.path | string | | /images/icons/profilepics/default.svg |
action_result.data.\*.version.by.profilePicture.width | numeric | | 48 |
action_result.data.\*.version.by.type | string | | known |
action_result.data.\*.version.by.userKey | string | `md5` | 4028fa8161b977bf0161b97970730000 |
action_result.data.\*.version.by.username | string | `user name` | admin |
action_result.data.\*.version.hidden | boolean | | True False |
action_result.data.\*.version.message | string | | |
action_result.data.\*.version.minorEdit | boolean | | True False |
action_result.data.\*.version.number | numeric | | 1 |
action_result.data.\*.version.when | string | | 2018-03-04T07:13:16.603-08:00 |
action_result.summary.important_data | string | | value |
action_result.summary.page_id | string | | 1703998 |
action_result.message | string | | Important data: value |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get page'

Get a page by name

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**space_key** | required | Name of the space containing the page | string | `confluence space key` |
**title** | required | Page title | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.space_key | string | `confluence space key` | TST |
action_result.parameter.title | string | | Shift Log 2 |
action_result.data.\*.\_links.base | string | `url` | http://192.16.195.173:9090 |
action_result.data.\*.\_links.context | string | | |
action_result.data.\*.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/content?spaceKey=TST&expand=body.storage&context=guid&context=artifact_id&context=parent_action_run&title=Shift+Log+2 |
action_result.data.\*.limit | numeric | | 25 |
action_result.data.\*.results.\*.\_expandable.ancestors | string | | |
action_result.data.\*.results.\*.\_expandable.children | string | | /rest/api/content/65601/child |
action_result.data.\*.results.\*.\_expandable.container | string | | /rest/api/space/TST |
action_result.data.\*.results.\*.\_expandable.descendants | string | | /rest/api/content/65601/descendant |
action_result.data.\*.results.\*.\_expandable.history | string | | /rest/api/content/65601/history |
action_result.data.\*.results.\*.\_expandable.metadata | string | | |
action_result.data.\*.results.\*.\_expandable.operations | string | | |
action_result.data.\*.results.\*.\_expandable.restrictions | string | | /rest/api/content/65601/restriction/byOperation |
action_result.data.\*.results.\*.\_expandable.space | string | | /rest/api/space/TST |
action_result.data.\*.results.\*.\_expandable.version | string | | |
action_result.data.\*.results.\*.\_links.edit | string | | /pages/resumedraft.action?draftId=65601 |
action_result.data.\*.results.\*.\_links.self | string | `url` | http://192.16.195.173:9090/rest/api/content/65601 |
action_result.data.\*.results.\*.\_links.tinyui | string | | /x/QQAB /x/CAAa |
action_result.data.\*.results.\*.\_links.webui | string | | /display/TST/TST+Home |
action_result.data.\*.results.\*.body.\_expandable.anonymous_export_view | string | | |
action_result.data.\*.results.\*.body.\_expandable.editor | string | | |
action_result.data.\*.results.\*.body.\_expandable.export_view | string | | |
action_result.data.\*.results.\*.body.\_expandable.styled_view | string | | |
action_result.data.\*.results.\*.body.\_expandable.view | string | | |
action_result.data.\*.results.\*.body.storage.\_expandable.content | string | | /rest/api/content/65601 |
action_result.data.\*.results.\*.body.storage.representation | string | | storage |
action_result.data.\*.results.\*.body.storage.value | string | | <ac:layout>\<ac:layout-section ac:type="single"><ac:layout-cell> \<ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="935965cb-dcd1-4334-9f43-d33256d38f67">\<ac:parameter ac:name="title">Welcome to your new space!\</ac:parameter><ac:rich-text-body><p>Confluence spaces are great for sharing content and news with your team. This is your home page. Right now it shows recent space activity, but you can customize this page in any way you like.</p>\</ac:rich-text-body>\</ac:structured-macro><h2>Complete these tasks to get started</h2><ac:task-list> <ac:task> <ac:task-id>1\</ac:task-id> <ac:task-status>incomplete\</ac:task-status> <ac:task-body><strong>Edit this home page</strong> - Click <em>Edit</em> in the top right of this screen to customize your Space home page\</ac:task-body> \</ac:task> <ac:task> <ac:task-id>2\</ac:task-id> <ac:task-status>incomplete\</ac:task-status> <ac:task-body><strong>Create your first page</strong> - Click the <em>Create</em> button in the header to get started\</ac:task-body> \</ac:task> <ac:task> <ac:task-id>3\</ac:task-id> <ac:task-status>incomplete\</ac:task-status> <ac:task-body><strong>Brand your Space</strong> - Click <em>Configure Sidebar</em> in the left panel to update space details and logo\</ac:task-body> \</ac:task> <ac:task> <ac:task-id>4\</ac:task-id> <ac:task-status>incomplete\</ac:task-status> <ac:task-body><strong>Set permissions</strong> - Click <em>Space Tools</em> in the left sidebar to update permissions and give others access\</ac:task-body> \</ac:task> \</ac:task-list><p> </p>\</ac:layout-cell>\</ac:layout-section>\<ac:layout-section ac:type="two_equal"><ac:layout-cell> <h2>Recent space activity</h2><p>\<ac:structured-macro ac:name="recently-updated" ac:schema-version="1" ac:macro-id="bb48b3e3-1171-4799-867e-32938d991be7">\<ac:parameter ac:name="types">page, comment, blogpost\</ac:parameter>\<ac:parameter ac:name="max">5\</ac:parameter>\<ac:parameter ac:name="hideHeading">true\</ac:parameter>\<ac:parameter ac:name="theme">social\</ac:parameter>\</ac:structured-macro></p>\</ac:layout-cell><ac:layout-cell> <h2>Space contributors</h2><p>\<ac:structured-macro ac:name="contributors" ac:schema-version="1" ac:macro-id="fdf07fe9-d741-4e36-816a-c89d567f054e">\<ac:parameter ac:name="mode">list\</ac:parameter>\<ac:parameter ac:name="scope">descendants\</ac:parameter>\<ac:parameter ac:name="limit">5\</ac:parameter>\<ac:parameter ac:name="showLastTime">true\</ac:parameter>\<ac:parameter ac:name="order">update\</ac:parameter>\</ac:structured-macro></p>\</ac:layout-cell>\</ac:layout-section>\<ac:layout-section ac:type="single"><ac:layout-cell> <p> </p>\</ac:layout-cell>\</ac:layout-section>\</ac:layout> |
action_result.data.\*.results.\*.extensions.position | string | | none |
action_result.data.\*.results.\*.id | string | `confluence page id` | 65601 |
action_result.data.\*.results.\*.status | string | | current |
action_result.data.\*.results.\*.title | string | | TST Home |
action_result.data.\*.results.\*.type | string | | page |
action_result.data.\*.size | numeric | | 0 |
action_result.data.\*.start | numeric | | 0 |
action_result.summary.important_data | string | | value |
action_result.summary.page_id | string | | 1703944 |
action_result.message | string | | Important data: value |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
