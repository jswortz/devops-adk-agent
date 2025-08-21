# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from .prompt import GENERAL_INSTRUCTIONS, JIRA_MCP_INSTRUCTIONS


root_agent = Agent(
    model="gemini-2.0-flash",
    name="jira_assistant_agent",
    instruction=GENERAL_INSTRUCTIONS + JIRA_MCP_INSTRUCTIONS,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "mcp-remote",
                        "https://mcp.atlassian.com/v1/sse",
                        "51328",
                        "--debug",
                    ],

                ),
            ),
        )
    ],
)
