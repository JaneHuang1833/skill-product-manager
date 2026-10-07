# Contributing

Thank you for helping make product discovery more reliable.

## Useful contributions

- A minimal prompt that demonstrates incorrect routing or a missed boundary.
- A dated, inspected benchmark of relevant products and canonical identities.
- A reproducible arithmetic, packaging or reference-resolution defect.
- A clearer contract, acceptance criterion or uncertainty treatment.
- Verified client installation results with platform and version.

Avoid expanding every skill into a universal checklist. Keep methods concise and disclose supporting detail progressively.

## Setup

Follow [development](docs/development.md), run `python scripts/check.py`, and use a fresh disposable workspace for behavioral exercises. No account, API key or live external mutation is needed for structural tests.

## Change process

1. Open an issue for a substantial method or contract change.
2. Create a focused branch and preserve unrelated files.
3. Update the source of truth and any affected examples/tests.
4. Run the local checks and inspect the actual user-facing behavior.
5. Submit a PR explaining the trigger, behavior change and validation.

A documentation correction needs no elaborate test that only matches wording. A script or contract change should include a meaningful regression where warranted.

## Review criteria

- The skill's description selects the right requests.
- User intent, existing authorization and answered questions are preserved.
- Claims and reasoning stay distinguishable.
- Unknowns are not silently turned into facts.
- No fictitious tools, searches, users, licenses or experiment results appear.
- Shared references are linked and not duplicated.
- STOP/reuse/validate routes remain valid outcomes.
- P0 requirements have observable acceptance and explicit blockers.

## Behavioral evaluation

Use [the case suite](tests/behavior-cases.md). Give an independent evaluator a realistic request and only the source materials needed. Do not reveal the expected answer beforehand. Record cases actually run, host/tool limits, generated artifacts and observed failures.

Live research benchmarks can change. Record date and source access, and do not claim internet-wide recall from a small labeled set.

## Attribution

Original contributions are submitted under the project's [MIT license](LICENSE). Preserve third-party copyright and permission notices for any copied or substantially adapted material. Cite conceptual inspiration separately; inspect license terms before importing upstream content.

## Community

Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report ordinary problems via [issues](https://github.com/JaneHuang1833/skill-product-manager/issues). Use [private security reporting](SECURITY.md) for vulnerabilities. No response-time or support SLA is promised.
