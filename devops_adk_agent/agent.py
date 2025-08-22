# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from .prompt import GENERAL_INSTRUCTIONS, JIRA_MCP_INSTRUCTIONS
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool
from typing import Dict, Any
import json

# {"account_id":"712020:554064b3-8293-4bab-8ea6-b9bea9fade8b","email":"admin@jwortz.altostrat.com","name":"Jeremy Wortz","picture":"https://secure.gravatar.com/avatar/0707a1b0c2a6a5249a27ce1189cbb4d3?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FJW-4.png","account_status":"active","characteristics":{"not_mentionable":false},"last_updated":"2025-02-28T00:07:01.542Z","nickname":"Jeremy Wortz","locale":"en-US","extended_profile":{"phone_numbers":[],"team_type":"Software Development"},"account_type":"atlassian","email_verified":true}"


def get_atlassian_info_callback(
    tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext, tool_response: Dict
):
    """
    This callback function processes responses from specific tools to store Atlassian metadata and Jira project information in the tool context's state.
    """
    tool_name = tool.name
    if tool_name == "getAccessibleAtlassianResources":
        if tool_context.state.get("atlassian_metadata", False):
            return
        tool_context.state["atlassian_metadata"] = tool_response
    if tool_name == "getVisibleJiraProjects":
        if tool_context.state.get("jira_projects", False):
            return
        tool_context.state["jira_projects"] = tool_response


get_info_agent = Agent(
    model="gemini-2.0-flash",
    name="get_info_agent",
    instruction="Use this Agent one time to save Atlassian metadata to state by using getAccessibleAtlassianResources and getVisibleJiraProjects tools, then transfer back to the parent agent.",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "mcp-remote",
                        "https://mcp.atlassian.com/v1/sse",
                        "--debug",
                    ],
                ),
            ),
            tool_filter=[
                "getAccessibleAtlassianResources",
                "getVisibleJiraProjects",
            ],  # we will just use this tool to get our project info and save it to state
        )
    ],
    after_tool_callback=get_atlassian_info_callback,
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="jira_assistant_agent",
    instruction=GENERAL_INSTRUCTIONS + JIRA_MCP_INSTRUCTIONS,
    sub_agents=[get_info_agent],
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "mcp-remote",
                        "https://mcp.atlassian.com/v1/sse",
                        "--debug",
                    ],
                ),
            ),
        )
    ],
)
