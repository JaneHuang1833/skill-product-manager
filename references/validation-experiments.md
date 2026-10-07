# Validation experiment design

Test the assumption that changes the decision, not the feature easiest to demonstrate. Preference: **actual behavior → costly commitment → opinion**. An interview can reveal past behavior; “would you use it?” is weak evidence.

## Cheapest-test selection

| Risk | Low-cost experiment | What it can and cannot establish |
|---|---|---|
| Real job and pain | Interviews around recent events; inspect voluntarily supplied workflow artifacts | Existing behavior/friction; not automatically WTP or retention |
| Install/distribution friction | Prototype install flow or proposed listing with a clear next action | Funnel/commitment; marketplace impression estimates need real logs |
| Value of structured output | Concierge/manual service using actual user inputs and current alternative comparison | Outcome/action taken; does not prove automated reliability |
| Repeat use | Repeated concierge/prototype sessions at natural job cadence | Return and successful use; allow enough time for job frequency |
| Technical feasibility | Bounded model/tool spike on representative permitted data | Capability, latency/cost and failure modes; not market demand |
| Demand or commitment | README + waitlist, landing page, fake door, listing concept | Stated/behavioral interest at that channel; click alone is not willingness to pay |
| Workflow UX | Prototype or Wizard-of-Oz task completion | Friction and output use; disclose manual operation when necessary |

Designing these experiments does not authorize contacting users, collecting payments, publishing listings or modifying external services. Produce reviewable scripts/prototypes/plans; actual execution follows the user's existing permissions.

## Experiment contract

For each prioritized experiment record:

- `assumption_id`, **Hypothesis** (specific segment + measurable action + observation period).
- **Method / Experiment**, participant eligibility, recruitment channel, sample target rationale, current-alternative/control comparison where useful.
- **Metric**: observable event, numerator/denominator, exclusion rules, instrumentation and data source.
- **Success Threshold / Failure Threshold**, why they change the decision, minimum observations and time window. Thresholds are proposed decisions agreed before execution, never fabricated industry benchmarks.
- **Inconclusive zone**: neither threshold reached, insufficient sample, tooling failure or biased recruitment → collect defined missing evidence; do not call it success.
- **Kill Criteria**: assumption invalidation that warrants STOP, pivot or abandoning the proposed form; distinguish an invalid experiment from a failed hypothesis.
- **Effort / cost ceiling**, required permissions/data handling, owner (`TBD` if unknown), sequence/dependencies.
- **Next Action / Decision** for success, failure and inconclusive outcomes; links to source assumptions and Spec metrics.

Prefer a small number of experiments that cover the critical assumptions. Do not invent results or silently run a launch. Re-evaluate a decision after actual results, keeping previous assumptions and the evidence that changed them.
