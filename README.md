
# DevOps ADK Agent

A DevOps agent built using the Atlassian Developer Kit (ADK) that integrates with Atlassian's Model Context Protocol (MCP) server for enhanced DevOps workflows.

## Overview

This agent leverages the Atlassian MCP server to provide seamless integration with Atlassian cloud services, enabling automated DevOps tasks and workflows through the ADK framework.

## Prerequisites

- Node.js installed on your system
- An Atlassian Cloud account
- Access to the Atlassian services you want to integrate with

## Setup Steps

### 1. Authentication

Run this command first to authenticate with your Atlassian Cloud Account:

```bash
npx -y mcp-remote https://mcp.atlassian.com/v1/sse
```

This will initiate an OAuth flow to generate an authentication token for accessing Atlassian services through the MCP server.

### 2. Install Dependencies

```bash
poetry install
```

## Usage

After completing the authentication step, you can run the agent to perform various DevOps tasks integrated with your Atlassian services.

## MCP Server Integration

This agent uses the Atlassian MCP server which provides:
- Secure OAuth-based authentication
- Real-time event streaming via Server-Sent Events (SSE)
- Integration with Jira, Confluence, and other Atlassian products
- Context-aware operations for DevOps workflows

## Documentation

For more detailed information:
- [Atlassian MCP Server Setup Guide](https://support.atlassian.com/rovo/docs/setting-up-ides/)
- [ADK MCP Server Documentation](https://support.atlassian.com/rovo/docs/setting-up-ides/)
- See `CLAUDE.md` for Claude-specific integration details