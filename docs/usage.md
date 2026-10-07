# Usage

## Choose the smallest useful scope

Use `$discover-skill-product` for end-to-end discovery. If you already have an inspected candidate set, use `$similarity-analysis`. If you have a decision and need a spec, use `$product-definition`. Existing artifacts and answers are valid inputs; restarting from the beginning is unnecessary.

A good initial prompt identifies a primary user, recent trigger, current alternative and desired outcome. If you only have an idea, the framing skill can help establish them.

## Prompt recipes

### End-to-end discovery

```text
Use $discover-skill-product.
Idea: an MCP tool that turns issue discussions into a decision log.
Primary user: maintainers of small open-source projects.
Today: they manually summarize discussions in Markdown.
Investigate existing solutions and recommend a route before defining an MVP.
Use current sources and keep search limitations visible.
```

### Existing product research

```text
Use $ecosystem-scan for a plugin that reviews a supplied product spec
for contradictory requirements. Research workflows and job synonyms,
not just products named "PRD reviewer". Stop at the search artifact.
```

### Compare supplied candidates

```text
Use $similarity-analysis against this brief and these inspected definitions.
Deduplicate mirrors and listings. Show provisional intervals where
a dimension is undocumented; do not treat missing evidence as zero.
```

### Review an opportunity

```text
Use $product-opportunity-evaluation with this brief, scan and comparison.
Evaluate it as a personal open-source tool rather than a paid SaaS.
Give one recommendation and the cheapest test of the main uncertainty.
```

### Define after a decision

```text
Use $product-definition for this BUILD MVP decision.
Reuse the prior answers, identify P0 blockers and produce a bounded
spec with Given/When/Then acceptance and a technical handoff.
```

### Resume

```text
Resume this saved discovery dossier.
The primary user has changed from founders to open-source maintainers.
Keep unaffected answers, identify invalidated artifacts and update
the earliest affected stage before carrying its conclusions forward.
```

## Decision routes

| Recommendation | Next deliverable |
|---|---|
| STOP | Reason, evidence and what would change the conclusion |
| USE EXISTING | Named solution, covered work and evaluation/setup route |
| EXTEND / FORK | Verified license, exact gap and extension scope |
| VALIDATE FIRST | Cheapest experiment; results remain separate evidence |
| BUILD MVP | Bounded definition/spec and remaining assumptions |
| BUILD FULL PRODUCT | Justified scope and release criteria; not granted from desk research alone |

A user can explicitly continue against a recommendation. The dossier retains the recommendation and records the actual choice and override; it does not turn enthusiasm into evidence.

## Results and files

Saved documents go under a collision-safe `discovery/<product-slug>/` directory. Each stage references its inputs by ID and version. Ask for a JSON export when you need a machine-readable envelope; otherwise the default is structured Markdown.

A complete envelope, registry and large comparison annex belong in saved artifacts. The conversational response should focus on the conclusion, decisive evidence, unknowns and next step.

## Personal versus commercial discovery

For personal/open-source work, evaluate maintenance time, actual repeated use, ecosystem value and contributor prospects. For commercial work, add buyer, budget, willingness-to-pay evidence, cost structure and reach. Do not infer a market from star counts or competitor counts.

## Acting on results

The plugin prepares plans and documents. Installation, messages, experiment recruitment, implementation and deployment require the user's corresponding authorization. Reuse authorization already established in the session; a checkpoint is not a request to confirm every stage.
