#!/usr/bin/env node
/**
 * Get your API key at https://llmscout.co/api-portal
 *
 * LLM Scout Brand Intelligence API - JavaScript example (Node 18+)
 */

const API_BASE = "https://llmscout.co/api/brand-intelligence";
const DEMO_KEY = "llmscout_demo_2024";

async function main() {
  const brand = process.argv[2] || "Stripe";
  const apiKey = process.env.API_KEY || DEMO_KEY;

  let data;
  try {
    const url = new URL(API_BASE);
    url.searchParams.set("brand", brand);
    url.searchParams.set("api_key", apiKey);

    const resp = await fetch(url.toString());
    const text = await resp.text();

    if (!resp.ok) {
      let errMsg = `API request failed: ${resp.status} ${resp.statusText}`;
      try {
        const err = JSON.parse(text);
        errMsg += ` - ${JSON.stringify(err)}`;
      } catch {
        errMsg += ` - ${text.slice(0, 200)}`;
      }
      throw new Error(errMsg);
    }

    data = JSON.parse(text);
  } catch (e) {
    console.error(e.message || e);
    process.exit(1);
  }

  const visibilityScore = data.visibility_score;
  const shareOfVoice = data.share_of_voice;
  const competitors = data.competitors || [];
  const top5 = competitors.slice(0, 5).map((c) => (typeof c === "object" && c?.name ? c.name : c));
  const prompts = data.related_prompts || data.prompts || [];
  const platformCoverage = data.platform_coverage || data.coverage_by_platform;

  console.log(`Brand: ${brand}`);
  console.log(`Visibility score: ${visibilityScore ?? "N/A"}`);
  console.log(`Share of voice: ${shareOfVoice ?? "N/A"}`);
  console.log(`Top 5 competitors: ${JSON.stringify(top5)}`);
  console.log(`Number of prompts: ${prompts.length}`);
  console.log(`Platform coverage: ${platformCoverage ?? "N/A"}`);
}

main();
