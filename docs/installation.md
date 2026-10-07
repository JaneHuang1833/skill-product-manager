# Installation

## Repository marketplace

Use a Codex version that supports repository plugin marketplaces:

```sh
codex plugin marketplace add JaneHuang1833/skill-product-manager --ref v0.2.0
```

Then open the Plugins Directory in your supported desktop client, select the **Skill Product Manager** marketplace and install **Skill Product Manager**. Restart or refresh the client as needed and begin a new chat.

The repository catalog points to the plugin at `./`, relative to the repository root. Marketplace ID: `skill-product-manager`. Plugin ID: `skill-product-manager`.

The command adds the source; it does not by itself prove installation or activation. Client surfaces differ. This repository's GitHub publication is separate from submission to OpenAI's universal public Plugins Directory.

## Local development

```sh
git clone https://github.com/JaneHuang1833/skill-product-manager.git
cd skill-product-manager
codex plugin marketplace add .
```

Select the local marketplace in the desktop client's Plugins Directory. Keep the entire plugin folder intact: its skills reference shared files outside their individual directories.

For a release ZIP, download the archive and its checksum from [GitHub Releases](https://github.com/JaneHuang1833/skill-product-manager/releases). Verify the checksum, extract the single `skill-product-manager/` directory, then add that extracted directory as a local marketplace. Use your host's package import if it explicitly supports portable plugin archives.

macOS/Linux checksum check:

```sh
shasum -a 256 -c skill-product-manager-0.2.0.zip.sha256
```

PowerShell check:

```powershell
Get-FileHash .\skill-product-manager-0.2.0.zip -Algorithm SHA256
Get-Content .\skill-product-manager-0.2.0.zip.sha256
```

Compare the hash values in PowerShell.

## Verify the installation

In a new chat:

```text
Use $idea-framing to frame a plugin that extracts action items
from transcripts I supply. Do not research competitors yet.
```

Expected behavior: a brief, explicit unknowns and at most 1–3 design-changing questions if needed. It should not assume recording access or create a full PRD.

Then ask for a current ecosystem scan. Verify actual source URLs and coverage logs. Host tools determine whether live research is possible.

## Update and remove

For a marketplace tracking `main`:

```sh
codex plugin marketplace upgrade skill-product-manager
```

A pinned `v0.2.0` source remains at that release. To switch deliberately:

```sh
codex plugin marketplace remove skill-product-manager
codex plugin marketplace add JaneHuang1833/skill-product-manager --ref main
```

Manage installation/enabled state in your client's plugin UI. Removing the marketplace source is separate from any generated discovery files. Do not delete your own saved artifacts as part of an update.

## Compatibility and troubleshooting

The package follows the [portable Agent Plugins layout](https://developers.openai.com/plugins/build/plugins) and includes the supported Codex compatibility manifest. Packaging documentation was checked on 2026-10-07. Automated checks validate metadata and references; they do not establish installation in every client.

| Symptom | Check |
|---|---|
| Marketplace command not recognized | Update to a supported client, or use its documented local import path |
| Plugin missing | Check marketplace source and refresh/restart; root has plugin.json and skills/ |
| Skill references fail | Install the whole package, not a single copied skill |
| Old instructions remain | Update the installed source, refresh and start a new chat |
| No live research | Provide host search/page tools, or accept an offline/limited artifact |
| Permission prompt for a connector | The connector is host-supplied; evaluate its requested scope separately |
| Unknown client compatibility | Report version, platform and a minimal reproduction in an issue |

No connector credentials or Python packages are needed merely to install the instruction plugin. Python and development packages are needed only when running its helpers/checks.

Reference: [official OpenAI packaging and marketplace documentation](https://developers.openai.com/plugins/build/plugins).
