# Synthetic validation plan

artifact_id: example-validation
artifact_type: validation_plan
version: 1
updated_at: 2026-10-07T12:00:00+08:00
status: draft
inputs: example-brief v1; example-dossier v1
claims: H1 (Assumption, Unverified): a reviewable draft reduces correction effort.
unknowns: real participants, current baseline, tool reliability and permitted transcripts.
sources: S-fixture — [local fictional scenario](source-material.md), inspected as a fixture.
decision_ref: example-dossier v1
assumption_refs: H1
sequence: establish baseline → compare draft → assess actual behavior.
resource_constraints: no execution; proposed one-week concierge test.

## Experiment E1

| Field | Proposed value |
|---|---|
| assumption_id | H1 |
| hypothesis | In a week, project leads spend less correction time using a draft without losing ownership clarity |
| method | Concierge action drafts versus the lead's current process on comparable voluntarily supplied transcripts |
| participants_channel | 3 willing project leads selected by the user; no recruitment performed |
| metric_event | Lead reviews, corrects and accepts or rejects an action list |
| numerator_denominator | Accepted lists needing no major correction / all valid reviewed lists; median review minutes; incorrect ownership / all proposed actions |
| sample_window | At least 6 valid reviewed lists across one week; too few is inconclusive |
| success_threshold | Proposed: at least 5/6 accepted without major correction, lower median time than baseline, no critical ownership error |
| failure_threshold | At most 2/6 accepted, or correction time exceeds baseline without better accuracy |
| inconclusive_zone | 3–4/6 accepted, insufficient sample, unmatched transcript difficulty or missing baseline |
| kill_criteria | Repeated critical ownership errors or no valid benefit across two tests |
| effort_cost_ceiling | Proposed 3 hours preparation/delivery; no paid acquisition |
| permissions | Only permitted transcripts; no recording, external messages or publication by default |
| owner | User; assistant can prepare local drafts |
| next_action_by_outcome | Success: define bounded automation; failure: revise/stop; inconclusive: collect missing comparison evidence |

These thresholds are illustration-only personal decision standards, not industry benchmarks. All outcomes remain Unknown.
