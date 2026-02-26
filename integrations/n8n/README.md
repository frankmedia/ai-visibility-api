# n8n Integration — AI Visibility API

Automate AI visibility monitoring with n8n and the LLM Scout Brand Intelligence API. This guide shows how to build a workflow that fetches brand intelligence data and outputs it to Google Sheets, Slack, or Email.

For n8n AI visibility workflows and n8n LLM monitoring, this integration lets you schedule regular brand checks and route results to your preferred destinations.

---

## Prerequisites

- An n8n instance (self-hosted or n8n Cloud)
- API key from the [LLM Scout API Portal](https://llmscout.co/api-portal) ($3 free credit)

---

## Step-by-Step Workflow Setup

### 1. Add HTTP Request Node

Create a new workflow and add an **HTTP Request** node:

- **Method:** GET
- **URL:** `https://llmscout.co/api/brand-intelligence`

### 2. Configure Query Parameters

Enable **Send Query Parameters** and add:

| Name     | Value                    |
|----------|--------------------------|
| `brand`  | `Stripe` (or your brand)  |
| `api_key`| `{{ $env.API_KEY }}`     |

Set `API_KEY` in your n8n environment variables, or replace the expression with your key for testing. For production, use credentials or environment variables.

Optional parameter:

| Name       | Value        |
|------------|--------------|
| `language` | `en` (or `es`, `de`, `fr`, `it`, `pt`, `nl`, `ja`, `ko`, `zh`, `ar`, `hi`) |

### 3. Add Set Node to Extract Key Fields

Add a **Set** node after the HTTP Request. Map the following fields from the API response:

| Field Name        | Expression / Value          |
|-------------------|-----------------------------|
| `brand_name`      | `Stripe` (or from input)    |
| `visibility_score`| `{{ $json.visibility_score }}` |
| `share_of_voice`  | `{{ $json.share_of_voice }}`  |
| `competitors`     | `{{ $json.competitors }}`     |

Use **Keep Only Set** if you want a clean output with only these fields.

### 4. Output to Destination

Connect the Set node to one or more of:

- **Google Sheets:** Add a Google Sheets node. Map `brand_name`, `visibility_score`, and `share_of_voice` to columns. Append a new row on each run.
- **Slack:** Add a Slack node. Use a Message node to format the visibility score and share of voice into a readable message and send to a channel.
- **Email:** Add an Email node (Gmail, SMTP, etc.). Use the Set node output as the email body or map fields into a template.

### 5. Add Trigger and Schedule

- **Manual trigger:** Use the default Manual Trigger to run on demand.
- **Schedule:** Add a **Schedule Trigger** node at the start to run weekly or daily:
  - Weekly: Use cron expression `0 9 * * 1` (e.g. Mondays at 9:00)
  - Daily: Use cron expression `0 9 * * *` (e.g. 9:00 every day)

Connect the Schedule Trigger to the HTTP Request node.

---

## Importable Workflow

An importable workflow JSON is provided in this folder:

**[workflow.json](./workflow.json)**

To import:

1. In n8n, open the workflow menu (three dots) and choose **Import from File** or **Import from URL**.
2. Select `workflow.json` or paste its contents.
3. Set your `API_KEY` environment variable in n8n settings.
4. Adjust the `brand` parameter if needed (default: Stripe).
5. Run the workflow manually or activate it with a schedule.

---

## Scheduling Recommendations

- **Weekly:** Good for regular brand health checks without high API usage.
- **Daily:** Use if you track fast-changing markets or run campaigns.
- **Rate limits:** The API allows 10 requests per minute and 1000 per day. Plan schedules accordingly.

---

## API Reference

- **Endpoint:** GET `https://llmscout.co/api/brand-intelligence`
- **Docs:** [API Documentation](https://llmscout.co/api-documentation)
- **Sign up:** [API Portal](https://llmscout.co/api-portal)

---

## SEO Keywords

n8n AI visibility, n8n LLM monitoring, AI brand monitoring workflow, n8n automation, LLM Scout integration
