#!/usr/bin/env python3
"""
Get your API key at https://llmscout.co/api-portal

LLM Scout Brand Intelligence API - Python example
"""

import os
import sys
import requests

API_BASE = "https://llmscout.co/api/brand-intelligence"
DEMO_KEY = "llmscout_demo_2024"


def main():
    brand = sys.argv[1] if len(sys.argv) > 1 else "Stripe"
    api_key = os.environ.get("API_KEY", DEMO_KEY)

    try:
        resp = requests.get(
            API_BASE,
            params={"brand": brand, "api_key": api_key},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        if hasattr(e, "response") and e.response is not None:
            try:
                err = e.response.json()
                print(f"Response: {err}")
            except Exception:
                print(f"Status: {e.response.status_code}, Body: {e.response.text[:200]}")
        sys.exit(1)
    except ValueError as e:
        print(f"Invalid JSON response: {e}")
        sys.exit(1)

    visibility_score = data.get("visibility_score")
    share_of_voice = data.get("share_of_voice")
    competitors = data.get("competitors") or []
    top_5_names = [c.get("name", c) if isinstance(c, dict) else str(c) for c in competitors[:5]]
    prompts = data.get("related_prompts") or data.get("prompts") or []
    platform_coverage = data.get("platform_coverage") or data.get("coverage_by_platform")

    print(f"Brand: {brand}")
    print(f"Visibility score: {visibility_score if visibility_score is not None else 'N/A'}")
    print(f"Share of voice: {share_of_voice if share_of_voice is not None else 'N/A'}")
    print(f"Top 5 competitors: {top_5_names}")
    print(f"Number of prompts: {len(prompts)}")
    print(f"Platform coverage: {platform_coverage if platform_coverage is not None else 'N/A'}")


if __name__ == "__main__":
    main()
