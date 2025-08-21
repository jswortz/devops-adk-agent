# DevOps ADK Agent - Claude Integration Guide

This document provides Claude-specific information for working with the DevOps ADK Agent and Atlassian MCP server integration.

## Overview

This agent is designed to work with the Atlassian Developer Kit (ADK) and uses the Atlassian Model Context Protocol (MCP) server for seamless integration with Atlassian Cloud services.

## Authentication

**Important**: Always run the authentication command first before attempting any operations:

```bash
npx -y mcp-remote https://mcp.atlassian.com/v1/sse
```

This command initiates an OAuth flow that will:
1. Open a browser window for Atlassian Cloud authentication
2. Generate an OAuth token for API access
3. Store the token securely for subsequent operations

## MCP Server Details

The Atlassian MCP server (`https://mcp.atlassian.com/v1/sse`) provides:

- **Protocol**: Server-Sent Events (SSE) for real-time communication
- **Authentication**: OAuth 2.0 flow for secure access
- **Integration Points**: 
  - Jira for issue tracking and project management
  - Confluence for documentation
  - Bitbucket for source control
  - Other Atlassian Cloud products

## Key Features

1. **Context-Aware Operations**: The MCP server provides contextual information about your Atlassian environment
2. **Real-Time Updates**: SSE connection enables live updates from Atlassian services
3. **Secure Token Management**: OAuth tokens are managed securely through the npx command
4. **Multi-Product Support**: Single authentication for all Atlassian Cloud products

## Working with the Agent

When working with this agent:

1. Ensure authentication is completed before any operations
2. The agent can access and manipulate data across your Atlassian Cloud instance
3. All operations are performed through the secure MCP server connection
4. The agent respects Atlassian Cloud permissions and access controls

## Troubleshooting

If you encounter issues:

1. **Authentication failures**: Re-run the npx command to refresh the OAuth token
2. **Connection issues**: Check network connectivity to mcp.atlassian.com
3. **Permission errors**: Verify your Atlassian Cloud account has appropriate access rights

## Resources

- [Atlassian MCP Server Setup](https://support.atlassian.com/rovo/docs/setting-up-ides/)
- [ADK Documentation](https://support.atlassian.com/rovo/docs/setting-up-ides/)
- [Atlassian Cloud API Documentation](https://developer.atlassian.com/cloud/)

## Development Notes

- The agent uses Poetry for dependency management
- Python-based implementation in the `devops-adk-agent/` directory
- Main entry points: `agent.py` and `prompt.py`
- OAuth flow screenshots available: `ouath-flow.png` and `dev-output.png`