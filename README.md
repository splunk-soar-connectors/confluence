[comment]: # "Auto-generated SOAR connector documentation"
# Confluence

Publisher: Splunk  
Connector Version: 2\.0\.2  
Product Vendor: Atlassian  
Product Name: Confluence  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app supports a variety of actions for content generation in Confluence

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Confluence asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | Base URL
**verify\_server\_cert** |  optional  | boolean | Verify server SSL certificate
**username** |  required  | string | Username
**password** |  required  | password | Password

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using the supplied configuration  
[add comment](#action-add-comment) - Add a comment to an existing page  
[create page](#action-create-page) - Create a page in the space  
[get page](#action-get-page) - Get a page by name  

## action: 'test connectivity'
Validate the asset configuration for connectivity using the supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'add comment'
Add a comment to an existing page

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**page\_id** |  required  | ID of the page to post comment | string |  `confluence page id` 
**body** |  required  | Comment body text | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.body | string | 
action\_result\.parameter\.page\_id | string |  `confluence page id` 
action\_result\.data\.\*\.\_expandable\.children | string | 
action\_result\.data\.\*\.\_expandable\.descendants | string | 
action\_result\.data\.\*\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.\_expandable\.operations | string | 
action\_result\.data\.\*\.\_expandable\.restrictions | string | 
action\_result\.data\.\*\.\_links\.base | string |  `url` 
action\_result\.data\.\*\.\_links\.collection | string | 
action\_result\.data\.\*\.\_links\.context | string | 
action\_result\.data\.\*\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.\_links\.webui | string | 
action\_result\.data\.\*\.body\.\_expandable\.anonymous\_export\_view | string | 
action\_result\.data\.\*\.body\.\_expandable\.editor | string | 
action\_result\.data\.\*\.body\.\_expandable\.export\_view | string | 
action\_result\.data\.\*\.body\.\_expandable\.styled\_view | string | 
action\_result\.data\.\*\.body\.\_expandable\.view | string | 
action\_result\.data\.\*\.body\.storage\.\_expandable\.content | string | 
action\_result\.data\.\*\.body\.storage\.representation | string | 
action\_result\.data\.\*\.body\.storage\.value | string | 
action\_result\.data\.\*\.container\.\_expandable\.ancestors | string | 
action\_result\.data\.\*\.container\.\_expandable\.body | string | 
action\_result\.data\.\*\.container\.\_expandable\.children | string | 
action\_result\.data\.\*\.container\.\_expandable\.container | string | 
action\_result\.data\.\*\.container\.\_expandable\.descendants | string | 
action\_result\.data\.\*\.container\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.container\.\_expandable\.operations | string | 
action\_result\.data\.\*\.container\.\_expandable\.restrictions | string | 
action\_result\.data\.\*\.container\.\_expandable\.space | string | 
action\_result\.data\.\*\.container\.\_links\.edit | string | 
action\_result\.data\.\*\.container\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.container\.\_links\.tinyui | string | 
action\_result\.data\.\*\.container\.\_links\.webui | string | 
action\_result\.data\.\*\.container\.extensions\.position | string | 
action\_result\.data\.\*\.container\.history\.\_expandable\.contributors | string | 
action\_result\.data\.\*\.container\.history\.\_expandable\.lastUpdated | string | 
action\_result\.data\.\*\.container\.history\.\_expandable\.nextVersion | string | 
action\_result\.data\.\*\.container\.history\.\_expandable\.previousVersion | string | 
action\_result\.data\.\*\.container\.history\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.container\.history\.createdBy\.\_expandable\.status | string | 
action\_result\.data\.\*\.container\.history\.createdBy\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.container\.history\.createdBy\.displayName | string | 
action\_result\.data\.\*\.container\.history\.createdBy\.profilePicture\.height | numeric | 
action\_result\.data\.\*\.container\.history\.createdBy\.profilePicture\.isDefault | boolean | 
action\_result\.data\.\*\.container\.history\.createdBy\.profilePicture\.path | string | 
action\_result\.data\.\*\.container\.history\.createdBy\.profilePicture\.width | numeric | 
action\_result\.data\.\*\.container\.history\.createdBy\.type | string | 
action\_result\.data\.\*\.container\.history\.createdBy\.userKey | string |  `md5` 
action\_result\.data\.\*\.container\.history\.createdBy\.username | string |  `user name` 
action\_result\.data\.\*\.container\.history\.createdDate | string | 
action\_result\.data\.\*\.container\.history\.latest | boolean | 
action\_result\.data\.\*\.container\.id | string | 
action\_result\.data\.\*\.container\.status | string | 
action\_result\.data\.\*\.container\.title | string | 
action\_result\.data\.\*\.container\.type | string | 
action\_result\.data\.\*\.container\.version\.\_expandable\.content | string | 
action\_result\.data\.\*\.container\.version\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.container\.version\.by\.\_expandable\.status | string | 
action\_result\.data\.\*\.container\.version\.by\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.container\.version\.by\.displayName | string | 
action\_result\.data\.\*\.container\.version\.by\.profilePicture\.height | numeric | 
action\_result\.data\.\*\.container\.version\.by\.profilePicture\.isDefault | boolean | 
action\_result\.data\.\*\.container\.version\.by\.profilePicture\.path | string | 
action\_result\.data\.\*\.container\.version\.by\.profilePicture\.width | numeric | 
action\_result\.data\.\*\.container\.version\.by\.type | string | 
action\_result\.data\.\*\.container\.version\.by\.userKey | string |  `md5` 
action\_result\.data\.\*\.container\.version\.by\.username | string |  `user name` 
action\_result\.data\.\*\.container\.version\.hidden | boolean | 
action\_result\.data\.\*\.container\.version\.message | string | 
action\_result\.data\.\*\.container\.version\.minorEdit | boolean | 
action\_result\.data\.\*\.container\.version\.number | numeric | 
action\_result\.data\.\*\.container\.version\.when | string | 
action\_result\.data\.\*\.extensions\.\_expandable\.resolution | string | 
action\_result\.data\.\*\.extensions\.location | string | 
action\_result\.data\.\*\.history\.\_expandable\.contributors | string | 
action\_result\.data\.\*\.history\.\_expandable\.lastUpdated | string | 
action\_result\.data\.\*\.history\.\_expandable\.nextVersion | string | 
action\_result\.data\.\*\.history\.\_expandable\.previousVersion | string | 
action\_result\.data\.\*\.history\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.history\.createdBy\.\_expandable\.status | string | 
action\_result\.data\.\*\.history\.createdBy\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.history\.createdBy\.displayName | string | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.height | numeric | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.isDefault | boolean | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.path | string | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.width | numeric | 
action\_result\.data\.\*\.history\.createdBy\.type | string | 
action\_result\.data\.\*\.history\.createdBy\.userKey | string |  `md5` 
action\_result\.data\.\*\.history\.createdBy\.username | string |  `user name` 
action\_result\.data\.\*\.history\.createdDate | string | 
action\_result\.data\.\*\.history\.latest | boolean | 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.space\.\_expandable\.description | string | 
action\_result\.data\.\*\.space\.\_expandable\.homepage | string | 
action\_result\.data\.\*\.space\.\_expandable\.icon | string | 
action\_result\.data\.\*\.space\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.space\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.space\.\_links\.webui | string | 
action\_result\.data\.\*\.space\.id | numeric | 
action\_result\.data\.\*\.space\.key | string | 
action\_result\.data\.\*\.space\.name | string | 
action\_result\.data\.\*\.space\.type | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.version\.\_expandable\.content | string | 
action\_result\.data\.\*\.version\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.version\.by\.\_expandable\.status | string | 
action\_result\.data\.\*\.version\.by\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.version\.by\.displayName | string | 
action\_result\.data\.\*\.version\.by\.profilePicture\.height | numeric | 
action\_result\.data\.\*\.version\.by\.profilePicture\.isDefault | boolean | 
action\_result\.data\.\*\.version\.by\.profilePicture\.path | string | 
action\_result\.data\.\*\.version\.by\.profilePicture\.width | numeric | 
action\_result\.data\.\*\.version\.by\.type | string | 
action\_result\.data\.\*\.version\.by\.userKey | string |  `md5` 
action\_result\.data\.\*\.version\.by\.username | string |  `user name` 
action\_result\.data\.\*\.version\.hidden | boolean | 
action\_result\.data\.\*\.version\.message | string | 
action\_result\.data\.\*\.version\.minorEdit | boolean | 
action\_result\.data\.\*\.version\.number | numeric | 
action\_result\.data\.\*\.version\.when | string | 
action\_result\.summary\.comment\_id | string | 
action\_result\.summary\.important\_data | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'create page'
Create a page in the space

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**space\_key** |  required  | Name of the space to create the page | string |  `confluence space key` 
**title** |  required  | Page title | string | 
**parent\_page\_id** |  optional  | Parent page ID | string |  `confluence page id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.parent\_page\_id | string |  `confluence page id` 
action\_result\.parameter\.space\_key | string |  `confluence space key` 
action\_result\.parameter\.title | string | 
action\_result\.data\.\*\.\_expandable\.children | string | 
action\_result\.data\.\*\.\_expandable\.descendants | string | 
action\_result\.data\.\*\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.\_expandable\.operations | string | 
action\_result\.data\.\*\.\_expandable\.restrictions | string | 
action\_result\.data\.\*\.\_links\.base | string |  `url` 
action\_result\.data\.\*\.\_links\.collection | string | 
action\_result\.data\.\*\.\_links\.context | string | 
action\_result\.data\.\*\.\_links\.edit | string | 
action\_result\.data\.\*\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.\_links\.tinyui | string | 
action\_result\.data\.\*\.\_links\.webui | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.ancestors | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.body | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.children | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.container | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.descendants | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.history | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.operations | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.space | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_expandable\.version | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_links\.self | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_links\.tinyui | string | 
action\_result\.data\.\*\.ancestors\.\*\.\_links\.webui | string | 
action\_result\.data\.\*\.ancestors\.\*\.extensions\.position | string | 
action\_result\.data\.\*\.ancestors\.\*\.id | string | 
action\_result\.data\.\*\.ancestors\.\*\.status | string | 
action\_result\.data\.\*\.ancestors\.\*\.title | string | 
action\_result\.data\.\*\.ancestors\.\*\.type | string | 
action\_result\.data\.\*\.body\.\_expandable\.anonymous\_export\_view | string | 
action\_result\.data\.\*\.body\.\_expandable\.editor | string | 
action\_result\.data\.\*\.body\.\_expandable\.export\_view | string | 
action\_result\.data\.\*\.body\.\_expandable\.styled\_view | string | 
action\_result\.data\.\*\.body\.\_expandable\.view | string | 
action\_result\.data\.\*\.body\.storage\.\_expandable\.content | string | 
action\_result\.data\.\*\.body\.storage\.representation | string | 
action\_result\.data\.\*\.body\.storage\.value | string | 
action\_result\.data\.\*\.container\.\_expandable\.description | string | 
action\_result\.data\.\*\.container\.\_expandable\.homepage | string | 
action\_result\.data\.\*\.container\.\_expandable\.icon | string | 
action\_result\.data\.\*\.container\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.container\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.container\.\_links\.webui | string | 
action\_result\.data\.\*\.container\.id | numeric | 
action\_result\.data\.\*\.container\.key | string | 
action\_result\.data\.\*\.container\.name | string | 
action\_result\.data\.\*\.container\.type | string | 
action\_result\.data\.\*\.extensions\.position | string | 
action\_result\.data\.\*\.history\.\_expandable\.contributors | string | 
action\_result\.data\.\*\.history\.\_expandable\.lastUpdated | string | 
action\_result\.data\.\*\.history\.\_expandable\.nextVersion | string | 
action\_result\.data\.\*\.history\.\_expandable\.previousVersion | string | 
action\_result\.data\.\*\.history\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.history\.createdBy\.\_expandable\.status | string | 
action\_result\.data\.\*\.history\.createdBy\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.history\.createdBy\.displayName | string | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.height | numeric | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.isDefault | boolean | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.path | string | 
action\_result\.data\.\*\.history\.createdBy\.profilePicture\.width | numeric | 
action\_result\.data\.\*\.history\.createdBy\.type | string | 
action\_result\.data\.\*\.history\.createdBy\.userKey | string |  `md5` 
action\_result\.data\.\*\.history\.createdBy\.username | string |  `user name` 
action\_result\.data\.\*\.history\.createdDate | string | 
action\_result\.data\.\*\.history\.latest | boolean | 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.space\.\_expandable\.description | string | 
action\_result\.data\.\*\.space\.\_expandable\.homepage | string | 
action\_result\.data\.\*\.space\.\_expandable\.icon | string | 
action\_result\.data\.\*\.space\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.space\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.space\.\_links\.webui | string | 
action\_result\.data\.\*\.space\.id | numeric | 
action\_result\.data\.\*\.space\.key | string | 
action\_result\.data\.\*\.space\.name | string | 
action\_result\.data\.\*\.space\.type | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.version\.\_expandable\.content | string | 
action\_result\.data\.\*\.version\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.version\.by\.\_expandable\.status | string | 
action\_result\.data\.\*\.version\.by\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.version\.by\.displayName | string | 
action\_result\.data\.\*\.version\.by\.profilePicture\.height | numeric | 
action\_result\.data\.\*\.version\.by\.profilePicture\.isDefault | boolean | 
action\_result\.data\.\*\.version\.by\.profilePicture\.path | string | 
action\_result\.data\.\*\.version\.by\.profilePicture\.width | numeric | 
action\_result\.data\.\*\.version\.by\.type | string | 
action\_result\.data\.\*\.version\.by\.userKey | string |  `md5` 
action\_result\.data\.\*\.version\.by\.username | string |  `user name` 
action\_result\.data\.\*\.version\.hidden | boolean | 
action\_result\.data\.\*\.version\.message | string | 
action\_result\.data\.\*\.version\.minorEdit | boolean | 
action\_result\.data\.\*\.version\.number | numeric | 
action\_result\.data\.\*\.version\.when | string | 
action\_result\.summary\.important\_data | string | 
action\_result\.summary\.page\_id | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get page'
Get a page by name

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**space\_key** |  required  | Name of the space containing the page | string |  `confluence space key` 
**title** |  required  | Page title | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.space\_key | string |  `confluence space key` 
action\_result\.parameter\.title | string | 
action\_result\.data\.\*\.\_links\.base | string |  `url` 
action\_result\.data\.\*\.\_links\.context | string | 
action\_result\.data\.\*\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.limit | numeric | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.ancestors | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.children | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.container | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.descendants | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.history | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.metadata | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.operations | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.restrictions | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.space | string | 
action\_result\.data\.\*\.results\.\*\.\_expandable\.version | string | 
action\_result\.data\.\*\.results\.\*\.\_links\.edit | string | 
action\_result\.data\.\*\.results\.\*\.\_links\.self | string |  `url` 
action\_result\.data\.\*\.results\.\*\.\_links\.tinyui | string | 
action\_result\.data\.\*\.results\.\*\.\_links\.webui | string | 
action\_result\.data\.\*\.results\.\*\.body\.\_expandable\.anonymous\_export\_view | string | 
action\_result\.data\.\*\.results\.\*\.body\.\_expandable\.editor | string | 
action\_result\.data\.\*\.results\.\*\.body\.\_expandable\.export\_view | string | 
action\_result\.data\.\*\.results\.\*\.body\.\_expandable\.styled\_view | string | 
action\_result\.data\.\*\.results\.\*\.body\.\_expandable\.view | string | 
action\_result\.data\.\*\.results\.\*\.body\.storage\.\_expandable\.content | string | 
action\_result\.data\.\*\.results\.\*\.body\.storage\.representation | string | 
action\_result\.data\.\*\.results\.\*\.body\.storage\.value | string | 
action\_result\.data\.\*\.results\.\*\.extensions\.position | string | 
action\_result\.data\.\*\.results\.\*\.id | string |  `confluence page id` 
action\_result\.data\.\*\.results\.\*\.status | string | 
action\_result\.data\.\*\.results\.\*\.title | string | 
action\_result\.data\.\*\.results\.\*\.type | string | 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.start | numeric | 
action\_result\.summary\.important\_data | string | 
action\_result\.summary\.page\_id | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 