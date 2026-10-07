# Stage artifact contracts and provenance

Use Markdown documents with these named fields by default; emit JSON equivalents when requested or needed for a tool. This is a typed conceptual contract, not a pre-existing runtime API. Do not invent a persistence service.

The complete envelope and registries belong in the saved stage artifact, not a second copy of the conversational report. In chat, show the conclusion, compact table, decision-relevant rationale/unknowns and source links; link the detailed artifact. If file tools are unavailable, provide necessary detail inline but do not repeat the same claims in both prose and a raw registry. Full JSON/envelope exports are available on request.

## Common envelope

| Field | Type / rule |
|---|---|
| artifact_id | string, stable local ID |
| artifact_type | idea_brief / ecosystem_scan / similarity_analysis / opportunity_review / validation_plan / product_definition / product_spec / technical_handoff / discovery_dossier |
| version | positive integer; increment on material changes |
| updated_at | local ISO 8601 datetime with offset when available |
| status | draft / ready / limited / blocked / stopped; Spec also declares handoff_status |
| inputs | artifact ID/version list; record invalidated downstream artifacts after upstream changes |
| claims | Claim[] |
| unknowns | {id, question, impact, next_action}[] |
| sources | Source[]; may be empty for user-only framing |

`Claim`: {id: string, statement: string, kind: Fact|Inference|Assumption|Recommendation, verification: Verified|Unverified|Conflicted, source_ids: string[], rationale: string}. `Verified` means the inspected source supports the claim, not independent proof of marketing claims. Preserve attribution. An inference can be well-supported but remains an inference. User input is attributed as user evidence; it needs no invented URL.

`Source`: {id: string, url: HTTPS/HTTP URL or null for private/local/user evidence, locator: string|null, synthetic: boolean, title: string, accessed_at: string, source_type: official|repository|author|third_party|user|local, supports: claim ID[], access_status: inspected|inaccessible|snippet_only}. `locator` records the actual local path or user attribution when there is no public URL; use null when it is inapplicable or must be withheld, with a stated reason. `synthetic` is true for generated fixtures. Public search conclusions require an inspected supporting URL. Protect sensitive evidence when exporting.

`Confidence`: {level: low|medium|high, rationale: string}. `Unknown` denotes unanswered text fields; `null` denotes missing numeric values. Empty candidate lists are valid but not evidence of exhaustive absence.

## Stage-specific payloads

| Type | Required fields |
|---|---|
| Idea Brief | target_user, situation, problem_jtbd, current_alternative, expected_outcome, core_workflow (string[]), required_capabilities (string[]), constraints (string[]), proposed_form (Skill|Command/Workflow|Plugin|MCP/Tool|Agent|Combination|Unknown), form_rationale, confidence |
| Ecosystem Scan | brief_ref, strategy (query matrix), coverage (rows), candidate_products (Product[]), exclusions (identity + reason), scope_status (saturated_within_scope|limited|offline), termination_reason |
| Similarity Analysis | brief_ref, scan_ref, landscape (A|B|C|unresolved), canonical_products, comparison_rows, component_scores, major_profiles (eight answers), gaps, reusable_ideas, provisional_leads |
| Opportunity Review | calibrated_problem, dimension_reviews (six named reviews, each evidence/assumptions/risks/confidence), assumption_register, decision (Decision) |
| Validation Plan | decision_ref, assumption_refs, experiments (Experiment[]), sequence, resource_constraints |
| Product Definition | decision_ref, primary_user, trigger, jtbd, current_workflow, desired_outcome, mvp_boundary, differentiator, tools_integrations, success_metrics, question_log, unresolved_blockers |
| Product Spec | definition_ref, research_refs, 18 sections, requirements (ID/P0-P1-P2/dependency/acceptance links), handoff_status (draft|ready_for_handoff), open_blockers |
| Technical Handoff | spec_ref, scope_status, implementation_slices, requirements_acceptance_map, contracts, dependencies_permissions, failure_resume_behavior, evaluation_cases, blocker_owners |
| Discovery Dossier | stage (Understand|Search|Compare|Evaluate|Decide|Define|Spec), artifact_refs, recommendation, user_choice, knowns, critical_unknowns, next_action, pending_questions, invalidated_refs |

`Product`: {id, name, type, canonical_url: URL|null, synthetic: boolean, aliases, lineage, target_user, jtbd, workflow, capabilities, output_ux, form_distribution, source_ids, verification, maintenance_evidence, license: {status: Verified|Unverified|Conflicted, identifier: string|null, source_url: URL|null, scope: string}}. Unknown fields remain unknown; unverified leads do not enter the confirmed competitor set. Synthetic products illustrate designs and never enter the real competitor set, even when their fixture definitions are verified. An inspected local snapshot can verify what its text defines without verifying current remote availability. Preserve any supplied upstream URL as attributed provenance; do not label it independently inspected. Product-definition verification and similarity-score completeness are separate states.

`Decision`: {choice: STOP|USE EXISTING|EXTEND / FORK|VALIDATE FIRST|BUILD MVP|BUILD FULL PRODUCT, rationale, confidence, biggest_risk, strongest_evidence, next_step, user_override: string|null}. The choice is a recommendation; `user_choice` records actual direction separately.

`Experiment`: {id, assumption_id, hypothesis, method, participants_channel, metric_event, numerator_denominator, sample_window, success_threshold, failure_threshold, inconclusive_zone, kill_criteria, effort_cost_ceiling, permissions, owner, next_action_by_outcome}. Thresholds are proposed unless validated/agreed; results are separate evidence.

## Similarity JSON contract

Input to [../scripts/score_similarity.py](../scripts/score_similarity.py): six required keys `problem_jtbd`, `user_context`, `workflow`, `capabilities_tools`, `output_ux`, `distribution_form`. Each value is `{score: number|null, rationale: nonempty string, source_ids: string[]}`. Non-null scores require at least one source ID. Unknown scores must explain missing evidence. Source IDs resolve against the candidate's evidence registry; the helper cannot verify that resolution or truth.

```json
{
  "problem_jtbd": {"score": 3.0, "rationale": "Same bounded job", "source_ids": ["S1"]},
  "user_context": {"score": 1.5, "rationale": "Same primary role and trigger", "source_ids": ["S1"]},
  "workflow": {"score": 2.0, "rationale": "Same necessary sequence", "source_ids": ["S2"]},
  "capabilities_tools": {"score": 2.0, "rationale": "Same necessary access", "source_ids": ["S2"]},
  "output_ux": {"score": 1.0, "rationale": "Same output contract", "source_ids": ["S2"]},
  "distribution_form": {"score": null, "rationale": "Installation form not documented", "source_ids": []}
}
```

Output: `{status: confirmed|provisional, total: number|null, observed_subtotal: number, range: [number,number], missing_dimensions: string[], band: string|null}`. Example above yields subtotal 9.5, range [9.5,10], total/band null, provisional. No silent normalization to 10.

## Resume and export

Honor user-owned saved artifacts and prior answers. Resume from the earliest invalid/insufficient stage; changing user/job invalidates scan, comparison, review and definition, while a naming change need not. Explain the changed dependency and keep prior versions until replaced intentionally. Materially stale evidence gets rechecked according to decision impact, not a fixed arbitrary expiry.

If file tools and workspace access are available, save a dossier and stage documents under a collision-safe `discovery/<product-slug>/` directory. Use source IDs consistently across documents. If not, deliver inline and state that no file was saved. Files and drafts are local deliverables; external messages, installations, experiment launches and deployments are separate actions.
