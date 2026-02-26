# API Reference — Brand Intelligence API

This document describes the LLM Scout Brand Intelligence API endpoint, parameters, response schema, error codes, and rate limits.

---

## Endpoint

| Property | Value |
|----------|-------|
| **URL** | `https://llmscout.co/api/brand-intelligence` |
| **Method** | `GET` |

---

## Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `brand` | Yes | string | Brand name to analyse (e.g. `Stripe`, `Shopify`) |
| `api_key` | Yes | string | Your API key from the [API Portal](https://llmscout.co/api-portal) |
| `language` | No | string | Language code. Supported: `en`, `es`, `de`, `fr`, `it`, `pt`, `nl`, `ja`, `ko`, `zh`, `ar`, `hi` |

---

## Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `visibility_score` | number | Percentage (0–100) of AI queries where the brand appears |
| `share_of_voice` | number | Brand's share of all mentions vs competitors (%) |
| `competitors` | array | Competing brands; each object has `name` (string) and `visibility_score` (number) |
| `related_prompts` | array | Prompts that surface the brand; each object has `text` (string), `relevance` (number), and `platform` results for `chatgpt`, `gemini`, `perplexity` |
| `platform_coverage` | object | Coverage percentages per platform: `chatgpt`, `gemini`, `perplexity` |
| `google_trends` | object | Contains `interest_over_time` array with search interest data |
| `citations` | array | Domains cited by AI models when recommending the brand |

---

## Example Request

```bash
curl "https://llmscout.co/api/brand-intelligence?brand=Stripe&api_key=llmscout_demo_2024"
```

---

## Example Response

```json
{
  "visibility_score": 78,
  "share_of_voice": 42.5,
  "competitors": [
    { "name": "PayPal", "visibility_score": 65 },
    { "name": "Square", "visibility_score": 58 },
    { "name": "Adyen", "visibility_score": 52 }
  ],
  "related_prompts": [
    {
      "text": "Best payment processing for e-commerce",
      "relevance": 0.92,
      "platform": {
        "chatgpt": true,
        "gemini": true,
        "perplexity": true
      }
    },
    {
      "text": "Top payment APIs for developers",
      "relevance": 0.88,
      "platform": {
        "chatgpt": true,
        "gemini": true,
        "perplexity": false
      }
    }
  ],
  "platform_coverage": {
    "chatgpt": 82,
    "gemini": 76,
    "perplexity": 71
  },
  "google_trends": {
    "interest_over_time": [
      { "date": "2024-01-01", "value": 65 },
      { "date": "2024-01-15", "value": 72 }
    ]
  },
  "citations": [
    "https://stripe.com",
    "https://developer.stripe.com",
    "https://en.wikipedia.org/wiki/Stripe_(company)"
  ]
}
```

---

## Error Codes

| HTTP Status | Meaning | Typical Cause |
|-------------|---------|---------------|
| **400** | Bad Request | Invalid or missing parameters (e.g. `brand` or `api_key` omitted) |
| **401** | Unauthorized | Invalid or expired API key |
| **403** | Forbidden | API key not authorised for this request (e.g. demo key used with non-supported brand) |
| **429** | Too Many Requests | Rate limit exceeded (10/min or 1000/day) |
| **500** | Internal Server Error | Server-side error; retry later |

---

## Rate Limits

| Limit | Value |
|-------|-------|
| Requests per minute | 10 |
| Requests per day | 1000 |

When limits are exceeded, the API returns HTTP 429. Implement retry logic with exponential backoff, or upgrade your plan via the [API Portal](https://llmscout.co/api-portal).

---

## Pricing

Each request costs approximately **$0.15–0.30** depending on brand complexity and freshness of cached data. Sign up at the [API Portal](https://llmscout.co/api-portal) for exact pricing and $3 free credit.
