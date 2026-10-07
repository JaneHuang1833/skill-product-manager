---
name: product-definition
description: Clarify a selected Skill, Plugin, Command, MCP, or Agent product into a bounded MVP, an 18-section product specification and technical handoff. Use after an opportunity decision; does not implement code.
---

# Product Definition

## Scope and inputs
Use when the user chooses to proceed and requests MVP definition, requirements, a PRD/spec or a technical handoff. Deliver only the requested slice for narrower requests. Accept the brief, research, decision, prior answers and constraints; validation is optional. Reuse existing evidence without implying missing research happened.

## Tools
Read material and write local documents. Verify current official capabilities or compatibility when needed. Implementation tools are not required to write a spec.

## Method
1. Identify unknowns that would change design. Ask 1–3 decisive questions per round, prioritizing user, trigger, JTBD, current workflow, outcome, scope, differentiator, integrations and metrics. Do not re-ask answered questions.
2. Update definition and question log after answers. Do independent work while dependent choices stay `Unknown`; avoid a full PRD before sufficient clarification.
3. Define one primary job/user/scenario, P0/P1/P2 and exclusions. Assess product form. Prefer verified reuse/extension where appropriate, with actual license evidence.
4. Once information is sufficient, complete the [18-section template](../../references/product-spec-template.md). Reference upstream research, decision and validation rather than duplicating conflicting evidence.
5. For P0, specify inputs/outputs, tools, data permissions, failure/resume behavior, metrics and Given/When/Then acceptance. Uncertain critical platform support is a blocker.
6. Produce a technical handoff companion: implementation slices, dependencies, done criteria, requirement-to-acceptance map, contracts, evaluation cases and blocker owners/next actions. Critical P0 unknowns keep it `draft`.

## Deliverable
An updated **Product Definition**, then **Product Spec — [Name]** and **Technical Handoff** when justified. Follow the [contracts](../../references/io-contracts.md). Save Markdown where possible; otherwise deliver complete requested content inline and disclose that no file was saved.

End with knowns, critical unknowns and next action. A user may request a conditional draft despite weak evidence; record their override without treating preference as fact. This stage does not authorize coding, installation or publication.
