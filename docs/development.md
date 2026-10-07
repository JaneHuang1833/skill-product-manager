# Development and releases

## Environment

Use Python 3.10 or newer. The installed instruction plugin has no Python runtime dependency; these tools are for contributors and optional arithmetic.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/check.py
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/check.py
```

## What is checked

- Seven named skills and matching frontmatter/UI metadata.
- Portable/compatibility manifest consistency and English text.
- Publisher, version, license, icons and repository marketplace path.
- Local links that resolve within the package.
- Similarity bounds, additive arithmetic, malformed input and unknown intervals.
- Release reproducibility, symlink rejection and private/development exclusions.
- CLI failure status and example score contracts.

The tests do not prove source truth, exhaustive search, user value or client installation. Use [behavioral cases](../tests/behavior-cases.md) for actual model/host exercises.

## Official schema verification

Download the schema as data, then run:

```sh
python scripts/validate_package.py . --manifest-schema /path/to/plugin.schema.json
```

Schema URL: [Agent Plugins 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json). This optional validation was performed during release preparation. Regular local/CI checks do not require network fetches.

## Build

```sh
python scripts/check.py
python scripts/build_release.py
```

Output: `dist/skill-product-manager-0.2.0.zip` and its `.sha256`. The archive has one top-level package folder. File ordering, timestamps and permissions are fixed; the same content builds identical bytes.

An explicit allowlist includes instructions, shared references, metadata, assets, documentation, examples, tests, helpers and community/license files. Git history, environments, generated discovery, hidden credentials, logs, bytecode and dist are excluded. Symlinks in distributable paths fail the build.

Validate the extracted archive in an arbitrarily named directory too. The package identity comes from the manifest, not the checkout folder's name.

## Release procedure

1. Update both manifests, README version badge, installation pin and changelog.
2. Run local checks, official schema validation and relevant behavioral cases.
3. Build the archive and inspect its contents and checksum.
4. Commit reviewed files; push a version tag such as `v0.2.0`.
5. The release workflow validates the tagged content, checks version/tag agreement, builds and uploads the ZIP and checksum to GitHub Releases.
6. Verify the public repository, CI result, release assets and download checksum.

Only the release job has repository write permission; ordinary CI has read-only contents. Third-party actions are pinned to reviewed commit SHAs, and Dependabot proposes updates.

A GitHub release does not submit the plugin to OpenAI's universal Plugins Directory. Universal directory publication is a separate process described in the [official submission guide](https://developers.openai.com/plugins/deploy/submission).

## Compatibility evidence

Record exact host version, platform, install method, fresh-chat prompt and observed output before marking client compatibility as tested. Structural success alone is insufficient.

## Maintenance

Prefer a small correction supported by a demonstrated failure. Update the single authoritative reference before changing dependent skills. Preserve input/version relationships and unknown semantics when changing artifact contracts.
