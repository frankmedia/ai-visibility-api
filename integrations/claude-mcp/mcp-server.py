#!/usr/bin/env python3
"""
Get your API key at https://llmscout.co/api-portal

MCP server for LLM Scout Brand Intelligence API.
Exposes get_brand_visibility tool for Claude Desktop.
"""

import json
import os

import requests
from mcp.server.fastmcp import FastMCP

API_BASE = "https://llmscout.co/api/brand-intelligence"

mcp = FastMCP(
    "ai-visibility-api",
    description="LLM Scout Brand Intelligence API - query AI visibility metrics for brands",
)


@mcp.tool()
def get_brand_visibility(brand: str, language: str = "en") -> str:
    """
    Get AI visibility metrics for a brand from the LLM Scout Brand Intelligence API.
    Returns visibility score, share of voice, competitors, and related prompts.
    """
    api_key = os.environ.get("API_KEY")
    if not api_key:
        return (
            "Error: API_KEY environment variable is not set. "
            "Get your API key at https://llmscout.co/api-portal"
        )

    try:
        resp = requests.get(
            API_BASE,
            params={"brand": brand, "api_key": api_key, "language": language},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        err_msg = str(e)
        if hasattr(e, "response") and e.response is not None:
            try:
                err_body = e.response.json()
                err_msg = json.dumps(err_body, indent=2)
            except Exception:
                text = e.response.text[:500] if e.response.text else str(e)
                err_msg = f"{e.response.status_code}: {text}"
        return f"API request failed: {err_msg}"
    except ValueError as e:
        return f"Invalid JSON response: {e}"

    visibility_score = data.get("visibility_score")
    share_of_voice = data.get("share_of_voice")
    competitors = data.get("competitors") or []
    related_prompts = data.get("related_prompts") or []
    platform_coverage = data.get("platform_coverage") or {}

    lines = [
        f"Brand: {brand}",
        f"Visibility score: {visibility_score if visibility_score is not None else 'N/A'}%",
        f"Share of voice: {share_of_voice if share_of_voice is not None else 'N/A'}%",
    ]
    if competitors:
        comp_names = [
            c.get("name", c) if isinstance(c, dict) else str(c)
            for c in competitors[:5]
        ]
        lines.append(f"Top competitors: {', '.join(comp_names)}")
    if platform_coverage:
        lines.append(f"Platform coverage: {json.dumps(platform_coverage)}")
    if related_prompts:
        top_prompts = [
            (p.get("text", "")[:80] + "...")
            if len(p.get("text", "")) > 80
            else p.get("text", "")
            for p in related_prompts[:3]
        ]
        lines.append(f"Sample prompts: {json.dumps(top_prompts)}")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
