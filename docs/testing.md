# Testing status

## Automated checks

On October 7, 2026, the maintainer ran all 19 package and scoring regression tests on macOS with Python 3.12.14. All passed. The checks cover manifest agreement, local links, skill metadata, deterministic archive contents, exclusion of private work, symlink rejection and similarity arithmetic with missing evidence. The portable manifest also passed the official Agent Plugins 1.0.0 JSON schema.

GitHub Actions runs the automated suite on Linux, Windows and macOS. Consult the actual [CI runs](https://github.com/JaneHuang1833/skill-product-manager/actions/workflows/ci.yml) for remote status; a workflow definition alone is not a passing result.

## Independent forward test

One separate agent read the packaged instructions and the raw synthetic meeting-followup source, without seeing the expected example decision or outputs. It handled an offline discovery request and produced a linked dossier and a usable validation kit.

Observed behavior: recommended VALIDATE FIRST, preserved missing scores as null, labeled mock products as fictional, distinguished local inspection from unexecuted public research, and treated an embedded credential-exfiltration sentence as untrusted source data. No external actions or experiments were executed. The score helper checked both provisional comparisons.

The review found no blocking defect on this route. Two small contract ambiguities were corrected: local source locators are explicit, and synthetic sources/products are flagged separately from definition verification.

## Limits and next tests

One agent run does not establish repeatability across models, live-search recall, real product demand or installation compatibility. The [behavior cases](../tests/behavior-cases.md) are a proposed regression checklist, not a claim that every case has been executed. Future changes should exercise live-source attribution, resume behavior and the BUILD-to-specification route. Client installation should be checked against the actual host version before claiming support.
