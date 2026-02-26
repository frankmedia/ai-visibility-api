# Getting Started with the AI Visibility API

The LLM Scout Brand Intelligence API helps you monitor how brands appear across ChatGPT, Gemini, Perplexity, and other large language models. This guide walks you through signing up, obtaining your API key, making your first request, and understanding the response.

---

## Step 1: Sign Up at the API Portal

Create an account at the **[LLM Scout API Portal](https://llmscout.co/api-portal)** to access the Brand Intelligence API. Registration is free and includes **$3 of free credit** so you can test the API without adding payment details.

The API portal is your hub for managing API keys, viewing usage, and accessing billing information.

---

## Step 2: Get Your API Key

After signing up, you will receive an API key from the [API Portal](https://llmscout.co/api-portal). Use this key in every request to authenticate with the API.

**Demo Key:** For quick testing, you can use the demo key `llmscout_demo_2024`. This key works only with the brands **Stripe** and **Shopify**. For production use or other brands, sign up and obtain your own key.

---

## Step 3: Make Your First Request

The API has a single endpoint. Make a `GET` request with your brand name and API key.

**cURL example (using the demo key):**

```bash
curl "https://llmscout.co/api/brand-intelligence?brand=Stripe&api_key=llmscout_demo_2024"
```

**With optional language parameter:**

```bash
curl "https://llmscout.co/api/brand-intelligence?brand=Stripe&api_key=llmscout_demo_2024&language=en"
```

Supported languages: `en`, `es`, `de`, `fr`, `it`, `pt`, `nl`, `ja`, `ko`, `zh`, `ar`, `hi`.

---

## Step 4: Understand the Response

The API returns a JSON object with structured brand intelligence data. Key fields include:

| Field | Description |
|-------|-------------|
| **visibility_score** | Percentage (0–100) indicating how often the brand appears in AI responses for relevant prompts |
| **share_of_voice** | Brand's percentage share of all mentions compared to competitors |
| **competitors** | Array of competing brands, each with `name` and `visibility_score` |
| **related_prompts** | Prompts that surface the brand, with per-platform results (ChatGPT, Gemini, Perplexity) and relevance scores |
| **platform_coverage** | Coverage percentages for each AI platform (ChatGPT, Gemini, Perplexity) |
| **google_trends** | `interest_over_time` array with search interest data |
| **citations** | Array of domains cited by AI models when recommending the brand |

For a full schema with types and nested structures, see the [API Reference](api-reference.md).

---

## Step 5: Next Steps

- **[API Reference](api-reference.md)** — Full endpoint documentation, response schema, error codes, and rate limits
- **[Use Cases](use-cases.md)** — Agency dashboards, AI SEO monitoring, competitive intelligence, white-label reporting
- **Integrations** — Connect the API to [n8n](https://llmscout.co/api-documentation), [Claude MCP](https://llmscout.co/api-documentation), or [Make.com](https://llmscout.co/api-documentation) for automated workflows

Return to the [API Portal](https://llmscout.co/api-portal) anytime to manage your keys and usage.
