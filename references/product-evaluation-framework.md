# Product Opportunity Review

## 0. Calibrate the problem

Write `Role + Situation + Problem + Desired Outcome + Current Alternative + Evidence`. If the promise is “serve more people”, name the additional identifiable segment and its job. Carry research coverage and landscape classification into the review. A user's enthusiasm is intent, not behavior evidence.

## Six dimensions

For each dimension return **Evidence / Assumptions / Risks / Confidence**, including contradictory evidence and source IDs. Confidence is low/medium/high with reasons about relevance, recency and independence, not an invented probability. Unknown stays unknown; do not invent market size, pricing, users or costs. Avoid an aggregate score that can conceal a fatal dependency.

| Dimension | Decision-changing analysis |
|---|---|
| 1. Demand reality | Is the job real? Active solution seeking, frequency, severity, current alternatives, time/money/effort already spent, concrete behavior. Separate “sounds useful” from observed attempts to solve it. |
| 2. Scale and reach | Can users be identified, found and reached? `Potential Value ≈ Users × Frequency × Value per Use` is a reasoning lens, not a revenue forecast. State units, ranges and assumptions. Examine marketplace, GitHub, developer community, AI ecosystem and sharing channels; install friction matters. |
| 3. Supply and feasibility | Model capability for required task; Web/API/MCP/Browser access; data rights/permissions; platform dependency; API/tool reliability; platform rule changes; maintenance, API, compatibility and support costs. A list of tools is not proof of feasibility. Use current primary docs or propose a bounded proof. |
| 4. Competition and differentiation | Compare Skills, Plugins, Agents, SaaS, saved prompts, native chat, manual workflow and doing nothing. Explain why the user switches. Evaluate workflow, context/data, integrations, distribution, network/community, brand, evaluation system and accumulated user knowledge; distinguish copyable prompts from demonstrated durable assets. |
| 5. Business or sustainability | Commercial: payer, reason, WTP evidence, budget source, model, cost structure, inference/API costs, maintenance/support/acquisition and plausible margin assumptions. Open-source/personal: maintenance value, growth, contributor likelihood, ecosystem/distribution/portfolio value and maintainer budget. Do not force a paid business model. |
| 6. Validation and decision | Identify the load-bearing assumption most likely to invalidate the whole product. State the strongest supporting case, search for disconfirming evidence, then describe the cheapest test at hypothesis/method/metric/success/failure/kill/next-action level. Detailed operational experiment design belongs to validation-plan. |

## Assumptions and red team

Use value, usability, feasibility, viability, ethics, go-to-market, strategy and team as lenses where relevant, not eight mandatory filler paragraphs. List only material assumptions. Each has ID, claim, category, impact if wrong, uncertainty, supporting/refuting evidence and “fails if …”. Prioritize high consequence, high uncertainty, low-cost-to-test assumptions. Ordinal rankings are enough; numeric ranking is an aid, not measured probability.

Make the strongest reasonable case for the idea before testing its claims. A sound claim need not be attacked artificially. Evidence against native chat insufficiency, willingness to install, repeated use, data access or a proposed wedge may be more decisive than feature enthusiasm.

## Decision

Choose exactly one primary recommendation:

| Decision | When justified | Next output |
|---|---|---|
| STOP | Weak job/value, fatal dependency, or failed critical experiment with no sensible pivot | Evidence, stop reason and possible changed condition |
| USE EXISTING | Verified alternatives adequately satisfy the specified job and constraints | Named product, covered job, setup/review path and sources |
| EXTEND / FORK | Close fit with a useful bounded gap and verified reuse permission/terms | Base project, exact gap, license URL/scope, maintenance and extension plan |
| VALIDATE FIRST | Plausible opportunity, but a decision-bearing unknown remains | Load-bearing assumption and cheapest experiment |
| BUILD MVP | Sufficient job/behavior, credible wedge, feasible access and plausible reach justify a bounded investment | MVP definition with remaining assumptions and validation |
| BUILD FULL PRODUCT | Demand, differentiation, feasibility, distribution and sustainability have strong evidence, with no unresolved critical assumption | Scope and release criteria; still define boundaries |

Do not grant BUILD FULL PRODUCT from desk research alone. If research is offline/limited or reuse permission is unresolved, recommend a conditional path or VALIDATE FIRST instead of claiming proof. Existing competitors do not force STOP; absence does not justify BUILD.

Always output: **Decision rationale / Confidence / Biggest Risk / Strongest Evidence / Next Step**. Strongest Evidence may be “none yet”; the recommendation is distinct from that evidence. If the user elects to proceed against advice, retain the recommendation and record `user_override`, implications and unresolved assumptions without obstructing their chosen work.
