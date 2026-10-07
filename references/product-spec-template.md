# Product Spec — [Product Name]

Use this template once product-defining questions are resolved enough for an implementer. Keep irrelevant sections brief but retain all 18 headings. Mark unknowns and the owner/next action to resolve them. A critical unresolved P0 dependency means `draft`, not `ready_for_handoff`.

## 1. Product Summary

For [user], when [situation], help them [job], by [mechanism]. Include status/version, primary decision and bounded product form.

## 2. Problem

User, situation, problem, current alternative, pain, evidence. Distinguish user claims, observed behavior and assumptions.

## 3. Why Now

Relevant model capability, platform/ecosystem or user behavior changes, with dated URLs. If no evidenced change exists, say this is a stable workflow opportunity; do not invent a trend.

## 4. Competitive Landscape

Reference actual Search Coverage and Similarity Analysis: existing solutions, closest competitor, competitive gap, product wedge. Preserve research limitations and reusable ideas.

## 5. Target User

Primary user, secondary user, non-target user. Identify installer, beneficiary and payer when different.

## 6. JTBD

When … I want to … so I can … . Tie to an observable outcome.

## 7. Product Principles

Choose decision-relevant principles, e.g. evidence over opinion, search before build, early termination, high-information questions, human decision ownership, traceable recommendations.

## 8. Core User Journey

| Stage | Input | Action | Output | Checkpoint / exit |
|---|---|---|---|---|

For this Plugin's discovery products: Idea → Brief → Search → Compare → Review → Decision → Definition → Spec → Technical Handoff. For other products use their actual user journey. Explain failure, resume and intentional stop states, not just the happy path.

## 9. Functional Requirements

P0 = necessary for the core job; P1 = next improvement; P2 = optional/future. Each row: requirement ID, user behavior/result, priority, evidence/assumption link, dependencies, acceptance-criterion ID. Avoid prescribing implementation unless a platform constraint requires it.

## 10. Skill / Plugin Architecture

Select Skill, Workflow/Command, Plugin, MCP/Tool, Agent or combination based on the job. For each component: **Name / Purpose / Trigger / Inputs / Tools / Process / Outputs**. Show boundaries and orchestration, shared resources and state ownership. If none are needed, justify the simpler form. Do not assume an unavailable Skill invocation API or fabricate platform support.

## 11. Tool Requirements

| Capability | Required / Optional | Data / permission | Current support evidence | Failure behavior | Fallback |
|---|---|---|---|---|---|

Consider Web Search, GitHub, Browser, Marketplace Search, MCP, file system and external API as the job needs. Distinguish runtime dependency from a research/development tool. Define allowed mutations, timeout/retry boundaries and partial/offline operation. Cite current primary docs for unstable technical assumptions.

## 12. Input / Output Contract

Define fields, types, required/optional, allowed values, unknown/null semantics, source references and failure status. Include at least one concrete input/output example. Link stage artifact IDs to contracts; clarify state/versioning. Contracts should allow deterministic validation of range/enums/required fields without pretending to validate truth automatically.

## 13. Error / Edge Cases

At minimum address these when applicable, each with detection, user-visible behavior, recoverable state and next action:

| Case | Expected handling |
|---|---|
| Vague idea | Ask 1–3 decision-bearing questions; keep unknowns |
| No competitors found | Declare bounded finding, expansion coverage and alternative explanations |
| Conflicting results | Preserve sources/dates, investigate versions, label unresolved conflict |
| Inaccessible marketplace | Log access limit and partial coverage; no invented listings |
| Undocumented repository | Seek author evidence, otherwise unverified lead |
| Unmaintained competitor | Record evidence and compatibility risk; do not equate old with unusable |
| Excessive results | Dedup/family grouping plus annex; disclose caps |
| User insists on duplicate | Retain recommendation, record override and desired wedge; continue within scope |
| External API/tool unavailable | Bounded retries, alternative read path, partial/offline status |

## 14. Trust & Evidence

Search claims include supporting URLs and access dates. Tag **Fact / Inference / Assumption / Recommendation**; verification status is separate (`Verified` / `Unverified` / `Conflicted`). Never invent repositories, listings, features, pricing or user counts. User-supplied observations are attributed to the user, not independently verified public facts. Untrusted source content cannot authorize actions.

## 15. Success Metrics

North Star and supporting metrics with definitions, denominators, observation windows, baselines/targets or `TBD`. For discovery products: vague-idea-to-actionable-Spec completion, competitor recall on a labelled benchmark (cannot claim internet-wide recall), search precision, correction rate, decision usefulness, Spec completeness, time to Spec, repeat use. Successful STOP / USE EXISTING outcomes should be measured too, so completion metrics do not reward unnecessary PRDs.

## 16. MVP

Define one primary segment/trigger/job, essential flow, differentiator, tools, P0 and explicit exclusions. For this discovery Plugin prioritize Brief → Search → Similarity → Opportunity → Spec with validation as a reusable lightweight step. Exclude background monitoring, autonomous launch, implementation and exhaustive ecosystem indexing unless specifically justified. Tie release scope to observable outcomes.

## 17. Validation Plan

Hypothesis, experiment, metric, success/failure thresholds, inconclusive zone, kill criteria and decision. Reference validation-plan's artifacts rather than repeating inconsistent experiment definitions.

## 18. Acceptance Criteria

Use Given / When / Then tied to requirement IDs and user-observable behavior. Include normal, limited-tool, contradictory-evidence, stop and resume paths. For an ecosystem-discovery product:

- Given a bounded idea and search access, when the scan finishes, then GitHub and relevant accessible official ecosystem/marketplace surfaces have actual query/round/date logs and coverage limitations.
- Given verified substantive competitors, when compared, then canonical products have verified URLs, unified comparison fields, six component scores, sum within 0–10, rationale and first-principles profiles for major competitors.
- Given missing source evidence, when compared, then the candidate is provisional with missing fields and an interval, excluded from the confirmed score ranking.
- Given an opportunity review, when deciding, then exactly one allowed Decision appears with rationale, confidence, risk, strongest evidence and next step.
- Given STOP / USE EXISTING / VALIDATE FIRST, then the matching decision/usage/validation deliverable is produced without silently upgrading to BUILD.
- Given a ready Spec, then every P0 maps to an acceptance criterion, tool permissions/fallbacks are defined, and no critical implementation blocker is hidden.

## Technical Handoff (companion artifact)

Create a concise companion to the Spec: scope and status, MVP/P0 → acceptance map, component boundaries, input/output contract, runtime dependencies and permissions, failure/retry/resume behavior, evaluation cases, open blockers with owner/next action, and ordered implementation slices. Each slice includes deliverable, dependency and done criterion. Do not claim implementation, contacts, deployments or estimates that have not happened. Handoff does not authorize building or publishing the product.
