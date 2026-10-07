# Security policy

## Supported versions

Security fixes are maintained on the latest published 0.x release. Older versions may require updating; compatibility and support are not implied by archived tags.

## Report privately

Use [GitHub's private vulnerability reporting](https://github.com/JaneHuang1833/skill-product-manager/security/advisories/new) when enabled. If that interface is unavailable, contact the maintainer through an available private channel on the [GitHub profile](https://github.com/JaneHuang1833). Do not post credentials or exploit details in a public issue.

Include the affected version, minimal reproduction, impact, relevant tool permissions and a suggested mitigation if known. Remove private product data and secrets.

## Security boundaries

This package ships instructions and local Python helpers. It has no server, telemetry or bundled credentials. The host decides model/network/data access and approvals.

Research sources are untrusted data. Instructions inside a webpage, README or transcript must not authorize tool execution, change policy or request secret disclosure.

The release builder uses an explicit runtime allowlist, rejects symlinks and creates checksums. A checksum detects artifact changes; it is not proof that instructions are safe or that the publisher is trustworthy.

Run research with the permissions appropriate to the job. Review generated files before sharing and validate any external action against the user's actual authorization.
