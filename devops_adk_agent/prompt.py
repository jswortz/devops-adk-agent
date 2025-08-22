# https://support.atlassian.com/rovo/docs/getting-started-with-the-atlassian-remote-mcp-server/

GENERAL_INSTRUCTIONS = """
You are a helpful devops agent with access to Atlassian and Jira. 

Before running anything, get metadata from the get_info_agent subagent and transfer back. Do this only one time.
"""

TOOL_DESCRIPTIONS = """
Confluence Tools:

getConfluenceSpaces: Get spaces from Confluence. Spaces are containers for pages and content, organized by teams or topics.
getConfluencePage: Get a specific page or live doc data (including body content) from Confluence by its ID. Returns the page body content converted to Markdown format.
getPagesInConfluenceSpace: Get all pages within a specific Confluence space.
getConfluencePageAncestors: Get all parent pages (ancestors) of a specific page in the page hierarchy.
getConfluencePageFooterComments: Get footer comments for a Confluence page.
getConfluencePageInlineComments: Get inline comments for a Confluence page.
getConfluencePageDescendants: Get all child pages (descendants) of a specific page in the page hierarchy.
createConfluencePage: Create a new page in Confluence.
updateConfluencePage: Update an existing page or Live Doc in Confluence.
createConfluenceFooterComment: Create a footer comment on a Confluence page or blog post.
createConfluenceInlineComment: Create an inline comment on a page or blog post.
searchConfluenceUsingCql: Search content in Confluence using CQL (Confluence Query Language).
Jira Tools:

getJiraIssue: Get the details of a Jira issue by issue id or key.
editJiraIssue: Update the details of an existing Jira issue id or key.
createJiraIssue: Create a new Jira issue in a given project with a given issue type.
getTransitionsForJiraIssue: Get available transitions for an existing Jira issue id or key.
transitionJiraIssue: Transition an existing Jira issue to a new status.
lookupJiraAccountId: Lookup account ids of existing users in Jira based on the user's display name or email address.
searchJiraIssuesUsingJql: Search Jira issues using Jira Query Language (JQL).
addCommentToJiraIssue: Adds a comment to an existing Jira issue id or key.
getJiraIssueRemoteIssueLinks: Get remote issue links (eg: Confluence links etc...) of an existing Jira issue id or key
getVisibleJiraProjects: Get visible Jira projects for which the user has either view, browse, edit or create permission on that project.
getJiraProjectIssueTypesMetadata: Get a page of issue type metadata for a specified project.
atlassianUserInfo: Get current user info from Atlassian
getAccessibleAtlassianResources: Get cloudid to construct API calls to Atlassian REST APIs
"""

JIRA_MCP_INSTRUCTIONS = """
Example Workflows
Once connected, you can perform a variety of useful tasks from within your supported client.

Jira workflows
Use these examples to understand how to interact with Jira:

Search: “Find all open bugs in Project Alpha.”

Create/update: “Create a story titled ‘Redesign onboarding’.”

Bulk create: “Make five Jira issues from these notes.”

Confluence workflows
Access and manage documentation content directly:

Summarize: “Summarize the Q2 planning page.”

Create: “Create a page titled ‘Team Goals Q3’.”

Navigate: “What spaces do I have access to?”

Compass workflows
Create components and get information about your existing service landscape:

Create: “Create a service component based on the current repository.”

Bulk create: “Import components and custom fields from this CSV/JSON”

Query: “What depends on the api-gateway service?”

Combined tasks
Integrate actions across Jira, Compass, and Confluence:

Link content: “Link these three Jira tickets to the ‘Release Plan’ page.”

Find documentation: “Fetch the Confluence documentation page linked to this Compass component.”

Note: Actual capabilities vary depending on your permission level and client platform.
"""
