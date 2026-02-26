# Use Cases for the AI Visibility API

The LLM Scout Brand Intelligence API supports agencies, marketing teams, and SaaS platforms that need to measure and improve brand visibility across AI search engines. This document outlines six common use cases, the API data to use, and example workflows.

---

## Use Case 1: Agency AI Visibility Dashboards

**Description:** Agencies can build dashboards that show clients how their brands perform in ChatGPT, Gemini, and Perplexity. Clients see visibility scores, share of voice, and competitor comparison in one place.

**API data to use:**
- `visibility_score` — Primary client-facing metric
- `share_of_voice` — Relative performance vs market
- `platform_coverage` — Per-platform breakdown (ChatGPT, Gemini, Perplexity)
- `competitors` — Competitor list with visibility scores
- `related_prompts` — Prompts where the brand appears

**Example workflow:**
1. Poll the API weekly or monthly for each client brand.
2. Store results in your database or data warehouse.
3. Build dashboards (e.g. Grafana, Metabase, or custom) showing trends over time.
4. Export reports for client presentations.

**Integrations:** Use [n8n](https://llmscout.co/api-documentation), [Make.com](https://llmscout.co/api-documentation), or [Claude MCP](https://llmscout.co/api-documentation) to automate polling and data ingestion. Get your API key from the [API Portal](https://llmscout.co/api-portal).

---

## Use Case 2: AI SEO / GEO Monitoring

**Description:** Generative Engine Optimisation (GEO) teams track how well brands rank in AI-generated answers. The API provides metrics analogous to traditional SEO but for AI search engines.

**API data to use:**
- `visibility_score` — Main GEO performance metric
- `related_prompts` — Prompt-level presence; each prompt has `text`, `relevance`, and per-platform results
- `platform_coverage` — Coverage per AI platform
- `google_trends.interest_over_time` — Correlate AI visibility with search interest

**Example workflow:**
1. Run the API for target brands and keywords.
2. Compare visibility scores before and after content or prompt optimisation.
3. Identify prompts where the brand is absent and prioritise content updates.
4. Track `interest_over_time` to align AI visibility with seasonal or trending searches.

---

## Use Case 3: Competitive Intelligence

**Description:** Brands and agencies monitor which competitors are mentioned in AI responses for their target queries. This enables strategic positioning and content adjustments.

**API data to use:**
- `competitors` — Competing brands with `name` and `visibility_score`
- `share_of_voice` — Brand’s share vs competitors
- `related_prompts` — Prompts where competitors appear, with per-platform breakdown

**Example workflow:**
1. Query the API for your brand and relevant keywords.
2. Compare your `visibility_score` and `share_of_voice` to top `competitors`.
3. Analyse `related_prompts` to see which prompts favour competitors.
4. Adjust content, positioning, or prompts to improve visibility in high-impact queries.

---

## Use Case 4: AI Citation Tracking

**Description:** Brands and PR teams want to know which domains AI models cite when recommending their brand. This helps prioritise backlink and citation campaigns and identify trustworthy sources.

**API data to use:**
- `citations` — Array of domains cited by AI models when recommending the brand

**Example workflow:**
1. Call the API for your brand.
2. Extract and deduplicate domains from the `citations` array.
3. Compare against your existing backlink profile to find new citation opportunities.
4. Reach out to high-authority domains that cite competitors but not your brand.

---

## Use Case 5: White-Label Reporting

**Description:** SaaS platforms and analytics vendors embed AI visibility data into their own products without exposing the underlying API. Reports are branded with the vendor’s identity.

**API data to use:**
- All response fields: `visibility_score`, `share_of_voice`, `competitors`, `related_prompts`, `platform_coverage`, `google_trends`, `citations`

**Example workflow:**
1. Integrate the API into your backend service.
2. Cache and aggregate results per client/brand.
3. Expose data through your own API or UI under your branding.
4. Apply rate limiting and quotas based on your tier.

Integrate via [n8n](https://llmscout.co/api-documentation), [Make.com](https://llmscout.co/api-documentation), or [Claude MCP](https://llmscout.co/api-documentation). Obtain an API key from the [API Portal](https://llmscout.co/api-portal).

---

## Use Case 6: AI Readiness Audits

**Description:** Consultants and internal teams run audits to assess whether a brand is discoverable in AI search. Audits identify gaps in AI visibility and recommend actions.

**API data to use:**
- `visibility_score` — Overall AI readiness metric
- `related_prompts` — Gaps where the brand is absent despite relevant prompts
- `platform_coverage` — Weak platforms that need attention
- `citations` — Citation quality and authority of sources
- `competitors` — Benchmarking against peers

**Example workflow:**
1. Run the API for the brand across multiple languages (e.g. `en`, `de`, `fr`).
2. Score readiness by combining `visibility_score`, `platform_coverage`, and citation quality.
3. Identify low-visibility prompts and platforms.
4. Produce an audit report with actionable recommendations (content, structured data, citations).
5. Re-run the API after changes to measure improvement.

---

## Integrations and Next Steps

- **n8n** — Importable workflows for automated brand monitoring
- **Claude MCP** — Use the API as a tool inside Claude Desktop via Model Context Protocol
- **Make.com** — No-code scenarios for AI visibility monitoring

Sign up at the [API Portal](https://llmscout.co/api-portal) for an API key with $3 free credit. See the [API Reference](api-reference.md) for technical details and the [Getting Started](getting-started.md) guide for setup steps.
