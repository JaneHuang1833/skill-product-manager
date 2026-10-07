# Architecture

## Instruction, orchestration and artifacts

A business skill owns one discovery stage. The orchestration skill reads those instructions as needed, maintains dependencies and reports checkpoints. A product spec is an implementation contract, not a command that implements the product.

The package does not assume a Skill RPC, a multi-agent service or a particular connector. The host supplies tools and applies instructions.

| Skill | Owns | Boundary | Artifact |
|---|---|---|---|
| idea-framing | User, trigger, job, alternative, outcome, form | No competitor verdict or feature design | Idea Brief |
| ecosystem-scan | Search, inspection, identity, coverage and provenance | No final similarity or business decision | Ecosystem Scan |
| similarity-analysis | Relevance, canonicalization, scoring and first principles | No build decision | Similarity Analysis |
| product-opportunity-evaluation | Evidence, counterevidence, assumptions and recommendation | No experiment execution or full PRD | Opportunity Review |
| validation-plan | Cheapest decision-bearing experiment | No recruitment or publication by default | Validation Plan |
| product-definition | Clarification, MVP, spec and handoff | No implementation by default | Definition / Spec / Handoff |
| discover-skill-product | Routing, versioned dossier and recovery | Does not duplicate stage methods | Discovery Dossier |

## Decisions and state

STOP and USE EXISTING ordinarily end with a decision or reuse path. VALIDATE FIRST ends with an experiment plan until real results arrive. EXTEND / FORK requires license verification. BUILD paths continue to definition and specification.

A user can request a conditional draft or choose a different route. Preserve `user_override`, evidence limitations and unresolved assumptions; do not manufacture support for the preference.

Artifacts carry stable IDs, versions and input references. Changing the target user or job invalidates affected downstream work; changing a display name usually does not. Resume at the earliest invalid stage and retain valid answers.

## Source of truth

| Resource | Responsibility |
|---|---|
| plugin.json | Portable identity, publisher and OpenAI presentation |
| .codex-plugin/plugin.json | Compatibility manifest with matching identity/version |
| .agents/plugins/marketplace.json | Repository distribution entry, relative to repo root |
| skills/*/SKILL.md | Stage scope, method and delivery |
| skills/*/agents/openai.yaml | English UI metadata; implicit invocation stays enabled |
| references/io-contracts.md | Shared envelopes and typed conceptual contracts |
| Other references | Stage-specific methods, rubrics and templates |
| scripts/score_similarity.py | Deterministic score arithmetic and uncertainty |
| scripts/validate_package.py | Package invariants, metadata and local link checks |
| scripts/build_release.py | Allowlisted deterministic archive and checksums |
| scripts/check.py | Single local/CI validation entry point |
| tests/ | Structural regressions and proposed behavioral cases |
| examples/ | Synthetic, explicitly attributed demonstration artifacts |

Shared references must ship with the whole plugin. Copying only one skill directory breaks its relative links. Single-stage invocation is supported when the package remains intact.

The release archive contains the runtime instructions, references, helper, metadata and license. Repository-only development and community materials remain available on GitHub; they need not consume runtime context.
