# Similarity rubric (0–10)

Score the same bounded Idea Brief against every substantively related canonical product. Similarity is overlap, not quality, maturity or opportunity attractiveness.

| Dimension | Max | Low / middle / full anchor |
|---|---:|---|
| Problem / JTBD | 3.0 | Different job / same job family with different outcome / same job and desired outcome |
| Target User + Context | 1.5 | Different role and trigger / one overlaps / same role, situation and trigger |
| Core Workflow | 2.0 | Different sequence / key steps overlap / same input-to-result journey and checkpoints |
| Capabilities / Tools | 2.0 | Different mechanisms / some necessary capabilities overlap / same essential reasoning, tools and data access |
| Output / UX | 1.0 | Different artifact or interaction / similar artifact or interaction / same artifact contract and usage pattern |
| Distribution / Product Form | 0.5 | Different deployment form / partially compatible packaging / same installation/platform form |

Intermediate scores are permitted with a specific rationale; use a tenth of a point. Sum raw points, do not multiply by weights a second time. Include each dimension's score, max, rationale and source IDs; distinguish an inference about intent from a documented feature.

Unknown evidence is `null`, never zero. Fetch the missing source if it may change classification and the user's permitted scope allows it. For incomplete candidates report `Provisional`, observed subtotal and possible range `[subtotal, subtotal + missing maxima]`; do not rank as a confirmed numeric total. For a candidate with a verified point estimate, calculate all six components and show the 0–10 total. Spec acceptance requires complete scoring for the verified comparison set when both the reference idea and candidate establish every dimension; otherwise preserve the provisional result. A fully inspected candidate can still have an incomplete score because the target idea's form or workflow is unknown. Do not turn that input gap into a claim that the candidate is undocumented. Inaccessible leads stay in a separate unverified annex.

Use [../scripts/score_similarity.py](../scripts/score_similarity.py) for arithmetic when file execution is available; otherwise apply these exact rules. The script accepts six component records and returns totals/ranges; it does not create judgments or verify sources.

| Total | Interpretation |
|---|---|
| 9.0–10 | Almost the same job and product design |
| 7.0–8.9 | Highly similar, with meaningful scope/capability differences |
| 5.0–6.9 | Adjacent, with substantial reusable ideas |
| 3.0–4.9 | Partly related |
| 0–2.9 | Weakly related; normally exclude from primary table |

## Unified comparison table

| Product | Type | Source | Similarity | Target User | JTBD | Core Features | First Principle | Key Difference | Reusable Ideas |
|---|---|---|---:|---|---|---|---|---|---|

For live ecosystem research, sources are clickable inspected supporting URLs, not repository names. For a user-constrained local/offline comparison, link the actual supplied files and label snapshot provenance, supplied upstream URL (if known), date and lack of current remote verification; never invent or silently claim verified URLs. Table cells stay compact; attach component breakdown and profiles in the detailed artifact. Analyze every substantive related product, with an annex when presentation grows too large. Select major competitors by closeness or importance as an alternative and explain that selection. Deduplicate fork/mirror/version/listing identities; keep functionally independent forks separate with lineage.

## First Principle profile for each major competitor

Answer these eight questions from documented evidence plus explicitly labelled reasoning:

1. What original job must the user complete?
2. How was it done before?
3. Where is the largest friction in that method?
4. Why is native LLM chat insufficient in this context?
5. What structure does this product add?
6. Which repetitive cognitive work is standardized?
7. Which tool, data or workflow access does it supply?
8. What gives the user a reason to return?

Do not paraphrase a README feature list as the explanation. If native chat may suffice, say so; do not manufacture a reason the product must exist. Repeated use is a hypothesis without behavior evidence.

## Landscape classification, before the final opportunity decision

- **A Highly redundant:** close overlap with verified mature coverage. Identify covered jobs, use/reuse routes, maintenance and license uncertainty, and what material difference would justify rebuilding. A high score alone does not establish maturity.
- **B Partly similar:** identify gaps in user, use case, workflow, UX/output quality, autonomy, integrations/data/context/memory, evaluation/reliability, privacy/cost/distribution/compatibility. Choose plausible wedges and explain why the gap matters to a user; more features alone is not a wedge.
- **C No highly similar product verified:** no verified highly similar product within declared coverage. Test white space versus small demand, infeasibility, platform limits, wrong form and semantic mismatch. Access-limited research may leave the landscape unresolved.

This classification feeds opportunity evaluation; it is not automatically STOP or BUILD.
