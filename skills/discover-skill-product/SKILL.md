---
name: discover-skill-product
description: Guide a vague Skill, Plugin, Command, MCP, or Agent idea through framing, ecosystem research, comparison, opportunity decisions, validation, and product definition. Use for end-to-end product discovery; use individual skills for single-stage requests.
---

# Discover Skill Product

Answer three questions: does it already exist, is it worth pursuing, and what should it become? Maintain a discovery dossier; apply stage skills rather than duplicating their methods.

## Scope and inputs
Use for a new or resumed idea-to-decision workflow. Accept natural language, prior artifacts, user observations, platform constraints and budgets. A competitor search or a spec-only request stays within that stage. Follow the user's language; package instructions are in English.

## Tools
Use the host's available search, page reading and file tools. GitHub, browser and marketplace connectors are optional. Applying a skill means reading its instructions; do not invent Skill RPCs, registered commands, autonomous services or tools.

## Routing
Read each skill and its necessary references only when entering that stage. Use the [artifact contracts](../../references/io-contracts.md).

| Stage | Skill | Deliverable and checkpoint |
|---|---|---|
| Understand | [idea-framing](../idea-framing/SKILL.md) | Brief and tentative form; ask 1–3 decisive questions if needed |
| Search | [ecosystem-scan](../ecosystem-scan/SKILL.md) | Verified candidates and actual coverage; disclose access limits |
| Compare | [similarity-analysis](../similarity-analysis/SKILL.md) | Canonical comparison, scores, first principles and gaps |
| Evaluate | [product-opportunity-evaluation](../product-opportunity-evaluation/SKILL.md) | Evidence, counterevidence, assumptions and one recommendation |
| Decide | Use the opportunity review | Rationale, confidence, risk, evidence and next action |
| Define | [product-definition](../product-definition/SKILL.md) | Bounded MVP and design-changing unknowns |
| Spec | Continue product-definition; use [validation-plan](../validation-plan/SKILL.md) as appropriate | 18-section spec and technical handoff, draft or ready |

Follow the decision:
- **STOP:** deliver evidence, the stopping reason and what would change it.
- **USE EXISTING:** identify the verified solution, covered job and evaluation/setup path.
- **EXTEND / FORK:** verify license and material gap before defining an extension. Missing permission stays unknown.
- **VALIDATE FIRST:** deliver the cheapest test with validation-plan; ordinarily wait for real results before proceeding. If the user requests an early spec, make it a conditional draft.
- **BUILD MVP / BUILD FULL PRODUCT:** continue definition and spec with appropriate validation; resolve critical requirements.

A checkpoint reports what is known, what matters next and what remains uncertain. It is not a repeated permission gate. Continue work already authorized by the user. Ask only for missing facts that could change the decision. If the user chooses a different route, record `user_override`, retain the recommendation and evidence, and help within their chosen scope.

## Resume and delivery
Update dossier stage, artifact IDs/versions, recommendation, actual user choice, pending questions, unknowns and next action. Reuse valid upstream work. A changed user/job invalidates affected downstream artifacts; record that dependency rather than quietly carrying old conclusions forward.

Keep chat concise: conclusion, compact comparison, decisive evidence/unknowns and artifact links. Save the dossier and stage documents under a collision-safe `discovery/<product-slug>/` directory when file tools are available; otherwise deliver inline and say nothing was saved. Follow the [contracts](../../references/io-contracts.md).

Research and local drafts do not authorize external messages, installation, experiments, implementation or deployment. Existing user authorization governs any next action.
