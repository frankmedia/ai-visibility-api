# Claude MCP Server — AI Visibility API

Use the LLM Scout Brand Intelligence API as a tool inside Claude Desktop via the Model Context Protocol (MCP). Query brand visibility scores, share of voice, and competitor data directly from Claude.

For Claude MCP AI visibility and MCP brand intelligence tool integrations, this server exposes a single tool that Claude can call when users ask about brand presence in AI systems.

---

## What Is MCP?

The **Model Context Protocol (MCP)** is an open protocol that lets AI applications like Claude Desktop connect to external tools and data sources. An MCP server exposes capabilities (tools, prompts, resources) that the AI can invoke during a conversation. When you run this server, Claude gains access to live brand intelligence data from the LLM Scout API.

---

## Prerequisites

- Python 3.10 or newer
- `mcp` and `requests` Python packages
- API key from the [LLM Scout API Portal](https://llmscout.co/api-portal) ($3 free credit)

---

## Installation

```bash
pip install mcp requests
```

From the `integrations/claude-mcp` directory:

```bash
pip install mcp requests
```

---

## How to Run

1. Set your API key as an environment variable:

   ```bash
   export API_KEY="your_api_key_here"
   ```

2. Start the MCP server:

   ```bash
   python mcp-server.py
   ```

   The server runs over STDIO. Keep it running in the background or configure Claude Desktop to launch it automatically.

---

## Claude Desktop Configuration

Add this server to your Claude Desktop configuration so Claude can use the brand visibility tool.

**macOS:** Edit `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows:** Edit `%APPDATA%\Claude\claude_desktop_config.json`

Add the following (adjust the path to where `mcp-server.py` lives):

```json
{
  "mcpServers": {
    "ai-visibility": {
      "command": "python",
      "args": ["/path/to/ai-visibility-api/integrations/claude-mcp/mcp-server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Replace `/path/to/ai-visibility-api` with the actual path to the repository. You can also omit the `env` block and set `API_KEY` in your shell before launching Claude.

---

## Example Usage

Once configured, you can ask Claude questions like:

- "What is Stripe's AI visibility score?"
- "How does Shopify compare to its competitors in AI search visibility?"
- "What is the share of voice for Adobe in AI recommendations?"

Claude will call the `get_brand_visibility` tool, fetch data from the LLM Scout API, and respond with visibility score, share of voice, competitor list, and related prompts.

---

## API Reference

- **Endpoint:** GET `https://llmscout.co/api/brand-intelligence`
- **Parameters:** `brand` (required), `api_key` (required), `language` (optional)
- **Docs:** [API Documentation](https://llmscout.co/api-documentation)
- **Sign up:** [API Portal](https://llmscout.co/api-portal)

---

## SEO Keywords

Claude MCP AI visibility, MCP brand intelligence tool, Claude Desktop MCP, Model Context Protocol AI monitoring, LLM Scout Claude integration
