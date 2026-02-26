# AI Visibility API – Monitor Brand Presence Across LLMs

[![Get API Key](https://img.shields.io/badge/Get%20API%20Key-Free%20%243%20Credit-6E65FF?style=for-the-badge)](https://llmscout.co/api-portal)
[![API Docs](https://img.shields.io/badge/API%20Docs-llmscout.co-111827?style=for-the-badge)](https://llmscout.co/api-documentation)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

The **AI Visibility API** enables developers, agencies, and SaaS platforms to monitor how brands appear inside large language models and AI search engines such as **ChatGPT**, **Claude**, **Gemini**, and **Perplexity**.

As AI systems increasingly replace traditional search, understanding how your brand is referenced, cited, or recommended by LLMs has become a measurable competitive advantage.

This repository provides documentation, integration guides, and code examples for working with the [LLM Scout Brand Intelligence API](https://llmscout.co/api-documentation).

---

## Get Your API Key

Sign up at the **[LLM Scout API Portal](https://llmscout.co/api-portal)** to get your API key with **$3 free credit** — no payment required to start.

> The demo key `llmscout_demo_2024` works with **Stripe** and **Shopify** for testing.

---

## What Is an AI Visibility API?

An AI visibility API is a programmable interface that allows you to:

- **Track brand mentions** inside LLM-generated responses
- **Analyse prompt-level visibility** across multiple AI models
- **Monitor competitor references** in AI answers
- **Detect citation sources** and link inclusion
- **Retrieve structured AI search intelligence data**

Unlike traditional SEO APIs that monitor Google rankings, an AI visibility API measures presence inside generative AI responses.

---

## Why AI Visibility Matters

AI systems are rapidly becoming decision layers. Users now ask:

- *"Best negotiation consultancy firms in Europe"*
- *"Top fintech SaaS providers"*
- *"Who offers AI visibility tracking tools?"*
- *"Best AI search monitoring platforms"*

If your brand is not mentioned inside those answers, you are invisible in AI-driven discovery.

An AI visibility API enables:

- Continuous **AI brand monitoring**
- **Prompt intelligence** tracking
- **Competitive benchmarking** across LLMs
- **AI citation gap analysis**
- **AI search share-of-voice** measurement

---

## Quick Start

### cURL

```bash
curl "https://llmscout.co/api/brand-intelligence?brand=Stripe&api_key=llmscout_demo_2024"
```

### Python

```python
import requests

response = requests.get(
    "https://llmscout.co/api/brand-intelligence",
    params={"brand": "Stripe", "api_key": "YOUR_API_KEY"}
)

data = response.json()
print(f"Visibility Score: {data['visibility_score']}%")
print(f"Share of Voice: {data['share_of_voice']}%")
print(f"Competitors: {[c['name'] for c in data['competitors'][:5]]}")
```

### JavaScript (Node.js)

```javascript
const res = await fetch(
  "https://llmscout.co/api/brand-intelligence?brand=Stripe&api_key=YOUR_API_KEY"
);
const data = await res.json();

console.log(`Visibility Score: ${data.visibility_score}%`);
console.log(`Share of Voice: ${data.share_of_voice}%`);
console.log(`Prompts: ${data.related_prompts.length}`);
```

> Replace `YOUR_API_KEY` with your key from the [API Portal](https://llmscout.co/api-portal). Use `llmscout_demo_2024` for testing with Stripe or Shopify.

---

## API Endpoint

```
GET https://llmscout.co/api/brand-intelligence
```

| Parameter  | Required | Description                                           |
|-----------|----------|-------------------------------------------------------|
| `brand`   | Yes      | Brand name to analyse (e.g. `Stripe`, `Shopify`)     |
| `api_key` | Yes      | Your API key from the [API Portal](https://llmscout.co/api-portal) |
| `language` | No      | Language code: `en`, `es`, `de`, `fr`, `it`, `pt`, `nl`, `ja`, `ko`, `zh`, `ar`, `hi` |

### Response Fields

| Field | Description |
|-------|-------------|
| `visibility_score` | Percentage of AI queries where the brand appears (0-100) |
| `share_of_voice` | Brand's share of all mentions vs competitors |
| `competitors` | Array of competing brands with their visibility scores |
| `related_prompts` | Prompts that surface this brand in AI responses, with per-platform results |
| `platform_coverage` | Breakdown by ChatGPT, Gemini, Perplexity |
| `google_trends` | Search interest data over time |
| `citations` | Domains cited by AI models when recommending the brand |

See [full API reference](docs/api-reference.md) for detailed response schema.

---

## Integrations

Use the AI Visibility API with your favourite automation and AI tools:

| Platform | Guide | Description |
|----------|-------|-------------|
| **n8n** | [n8n Integration](integrations/n8n/) | Importable workflow for automated brand monitoring |
| **Claude (MCP)** | [Claude MCP Server](integrations/claude-mcp/) | Use as a tool inside Claude Desktop via Model Context Protocol |
| **Make.com** | [Make.com Scenario](integrations/make/) | No-code AI visibility monitoring with Make |

---

## Use Cases

### 1. AI Brand Monitoring

Track how often your brand appears in ChatGPT, Claude, Gemini, and Perplexity responses.

### 2. AI SEO & Generative Engine Optimisation (GEO)

Measure generative engine optimisation performance over time.

### 3. Competitive AI Intelligence

Identify which competitors are cited in AI answers for your target prompts.

### 4. AI Citation Tracking

Extract domains referenced by AI models when recommending brands.

### 5. White-Label AI Visibility Dashboards

Embed AI visibility data into client-facing analytics tools or internal dashboards.

See [detailed use cases](docs/use-cases.md) for implementation patterns.

---

## Documentation

- [Getting Started](docs/getting-started.md) — Sign up, get your key, make your first request
- [API Reference](docs/api-reference.md) — Full endpoint documentation with response schema
- [Use Cases](docs/use-cases.md) — Agency dashboards, AI SEO monitoring, white-label reporting

---

## LLM Scout — AI Visibility Infrastructure

The **[LLM Scout](https://llmscout.co)** platform provides structured AI visibility intelligence across multiple large language models and 12 languages.

It enables:

- Prompt-level visibility tracking
- Brand and competitor analysis
- AI citation extraction
- Real-time or cached response retrieval
- Multi-language AI search monitoring

Designed for:

- **Agencies** offering AI search services
- **SaaS platforms** integrating AI monitoring dashboards
- **Enterprise marketing teams**
- **AI research and intelligence platforms**

[Explore the Research Tool](https://llmscout.co/research-tool) | [View Pricing](https://llmscout.co/#pricing) | [API Documentation](https://llmscout.co/api-documentation)

---

## Keywords & Related Search Terms

This project is relevant for developers and marketers searching for:

`AI visibility API` · `AI search monitoring API` · `LLM monitoring API` · `ChatGPT brand tracking` · `Claude citation monitoring` · `Gemini AI visibility tracking` · `Perplexity search monitoring` · `AI brand intelligence API` · `Generative engine optimisation tools` · `AI SEO tracking API` · `AI share of voice API` · `LLM brand intelligence`

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**[Get Your API Key →](https://llmscout.co/api-portal)**
