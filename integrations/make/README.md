# Make.com Integration — AI Visibility API

Automate AI visibility monitoring with Make.com and the LLM Scout Brand Intelligence API. This guide walks through building a scenario that fetches brand intelligence data and routes it to Google Sheets, Slack, or Email.

For Make.com AI visibility workflows and Make AI brand monitoring, this integration lets you schedule regular brand checks and send results to your preferred destinations.

---

## Prerequisites

- Make.com account
- API key from the [LLM Scout API Portal](https://llmscout.co/api-portal) ($3 free credit)

---

## Step-by-Step Scenario Setup

### 1. Create a New Scenario

In Make.com, create a new scenario. You will add modules in this order.

### 2. Add Trigger (Optional)

For scheduled runs:

- Add **Schedule** module as the trigger
- Set interval: daily (e.g. 9:00) or weekly (e.g. Mondays at 9:00)

For manual runs, leave the scenario without a trigger and use **Run once** when testing.

### 3. Add HTTP Module — Make a Request

Add an **HTTP > Make a request** module:

- **URL:** `https://llmscout.co/api/brand-intelligence`
- **Method:** GET
- **Query string:** Add the following parameters

| Name     | Value                                      |
|----------|--------------------------------------------|
| `brand`  | `Stripe` (or your brand name)              |
| `api_key`| Your API key (or map from a variable)      |

Optional: add `language` with value `en` (or `es`, `de`, `fr`, `it`, `pt`, `nl`, `ja`, `ko`, `zh`, `ar`, `hi`).

### 4. Parse JSON Response

The API returns JSON. Make.com parses it automatically in most cases. If you need to work with specific fields:

- Use the **HTTP** module output to map values
- Or add a **Tools > Set variable** module to store `visibility_score`, `share_of_voice`, and `brand` for reuse

### 5. Add Router for Outputs

Add a **Router** module after the HTTP request. Create routes for each destination:

**Route 1 — Google Sheets:**
- Add **Google Sheets > Add a row** module
- Map: `brand` (or brand name), `visibility_score`, `share_of_voice`, and optionally `competitors` or `citations` to columns
- Connect the route to this module

**Route 2 — Slack:**
- Add **Slack > Create a message** module
- Build a message body using the visibility score and share of voice
- Example: `Brand {{1.brand}} visibility: {{1.visibility_score}}%, share of voice: {{1.share_of_voice}}%`
- Send to your desired channel

**Route 3 — Email:**
- Add **Email > Send an email** module (Gmail, SMTP, or other)
- Set recipient, subject, and body
- Map `visibility_score`, `share_of_voice`, and brand name into the email content

### 6. Schedule the Scenario

- Open scenario settings
- Under **Scheduling**, choose:
  - **Daily** for regular monitoring
  - **Weekly** to reduce API usage
- Activate the scenario to run on schedule

---

## Response Fields

The Brand Intelligence API returns:

| Field             | Description                                           |
|-------------------|-------------------------------------------------------|
| `visibility_score` | Percentage of AI queries where the brand appears     |
| `share_of_voice`  | Brand's share of mentions vs competitors             |
| `competitors`     | Array of competing brands with visibility scores     |
| `related_prompts` | Prompts that surface the brand                       |
| `platform_coverage`| Breakdown by ChatGPT, Gemini, Perplexity             |
| `citations`       | Domains cited when recommending the brand            |

Map these fields into your Google Sheets columns, Slack messages, or email templates as needed.

---

## Rate Limits and Costs

- **Rate limits:** 10 requests per minute, 1000 per day
- **Cost:** Approximately $0.15–0.30 per request (see [API Portal](https://llmscout.co/api-portal) for details)
- **Free credit:** $3 on sign-up

Adjust your schedule to stay within limits.

---

## API Reference

- **Endpoint:** GET `https://llmscout.co/api/brand-intelligence`
- **Parameters:** `brand` (required), `api_key` (required), `language` (optional)
- **Docs:** [API Documentation](https://llmscout.co/api-documentation)
- **Sign up:** [API Portal](https://llmscout.co/api-portal)

---

## SEO Keywords

Make.com AI visibility, Make AI brand monitoring, Make.com automation, LLM Scout integration, AI visibility workflow
