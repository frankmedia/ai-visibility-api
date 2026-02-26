#!/bin/bash
#
# Get your API key at https://llmscout.co/api-portal
#
# LLM Scout Brand Intelligence API - curl examples
# Replace llmscout_demo_2024 with your API key for production use.
# Demo key works with Stripe and Shopify only.

API_KEY="${API_KEY:-llmscout_demo_2024}"
BASE="https://llmscout.co/api/brand-intelligence"

echo "=== 1. Basic brand lookup (Stripe) ==="
curl -s "${BASE}?brand=Stripe&api_key=${API_KEY}"

echo -e "\n\n=== 2. With language parameter (Spanish) ==="
curl -s "${BASE}?brand=Stripe&api_key=${API_KEY}&language=es"

echo -e "\n\n=== 3. Pretty-printed with jq ==="
curl -s "${BASE}?brand=Stripe&api_key=${API_KEY}" | jq .

echo -e "\n=== 4. Extract just visibility score with jq ==="
curl -s "${BASE}?brand=Stripe&api_key=${API_KEY}" | jq '.visibility_score'
