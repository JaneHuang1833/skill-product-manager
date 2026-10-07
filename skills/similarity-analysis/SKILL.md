---
name: similarity-analysis
description: Compare verified Skill, Plugin, Workflow, MCP, or Agent candidates using six additive similarity dimensions, first-principles analysis and gaps. Use for competitor comparison; does not replace ecosystem search.
---

# Similarity Analysis

## Scope and inputs
Use to assess overlap, differences and reusable ideas in inspected candidates. Accept an Idea Brief and Ecosystem Scan or readable candidate definitions. Names and search snippets alone are insufficient: inspect definitions or retain separate unverified leads.

## Tools
Use source-page reading, optional GitHub/browser tools and targeted gap-filling search. The Python score helper is optional; analysis does not depend on it.

## Method
1. Read the [rubric](../../references/similarity-rubric.md). Assess actual job relevance, deduplicate identities and explain exclusions or distinct fork lineage.
2. Compare every substantive verified canonical product in the ten-column table. Score each of six dimensions with evidence and rationale. Add raw points once for a total of 0–10; similarity is not quality or maturity.
3. Unknown dimensions are `null`, not zero. Fill decision-changing evidence gaps where feasible, then report remaining gaps as provisional intervals without normalization. The [helper](../../scripts/score_similarity.py) checks structure and arithmetic.
4. For major alternatives, answer the rubric's eight first-principles questions. Distinguish documented features from mechanism inferences; native chat may already suffice.
5. Classify the landscape: A highly redundant with mature coverage evidence, B partly similar, C no highly similar product verified within scope, or unresolved. Describe covered work, gaps, a plausible wedge, reuse, maintenance and license uncertainty.
6. Show a concise shortlist in chat and a complete annex when necessary. Do not use “top five” to conceal substantive candidates; disclose sampling limits.

## Deliverable
**Similarity Analysis**: ten-column table, component scores/rationales/sources, major profiles, landscape, gaps, reuse and provisional leads. Follow the [contracts](../../references/io-contracts.md). Save detailed registries and profiles in the artifact; do not repeat them in chat.

End with knowns, critical unknowns and next action. Existing competitors do not by themselves imply STOP, and an empty set does not imply BUILD.
