#!/usr/bin/env python3
"""Validate discovery packaging and local references without network access."""

import argparse
import json
from pathlib import Path
import re
import sys

EXPECTED_SKILLS = {
    "idea-framing", "ecosystem-scan", "similarity-analysis",
    "product-opportunity-evaluation", "product-definition",
    "validation-plan", "discover-skill-product",
}
SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
IGNORED_PARTS = {".git", ".venv", "venv", "__pycache__", "dist", "discovery"}


def load_object(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def package_files(root):
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if not any(part in IGNORED_PARTS for part in relative.parts) and path.is_file():
            yield path


def validate(root, manifest_schema=None):
    try:
        import yaml
    except ImportError as exc:
        raise ValueError("Development validation requires PyYAML") from exc
    root = Path(root).resolve()
    errors = []
    try:
        manifest = load_object(root / "plugin.json")
    except (OSError, ValueError) as exc:
        return [str(exc)]
    if manifest.get("$schema") != SCHEMA_URL:
        errors.append("unexpected portable manifest schema")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(manifest.get("name", ""))):
        errors.append("invalid package name")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", str(manifest.get("version", ""))):
        errors.append("release version must be semantic")
    if not manifest.get("description") or not manifest.get("author", {}).get("name"):
        errors.append("description and publisher name are required")
    if not manifest.get("license") or not (root / "LICENSE").is_file():
        errors.append("license identity and LICENSE file are required")
    if manifest_schema:
        try:
            from jsonschema import Draft202012Validator
        except ImportError as exc:
            raise ValueError("Official schema validation requires jsonschema") from exc
        schema = load_object(manifest_schema)
        for error in Draft202012Validator(schema).iter_errors(manifest):
            errors.append("manifest schema: " + error.message)

    interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not isinstance(interface.get(field), str) or not interface[field].strip():
            errors.append(f"interface.{field}: nonempty string required")
    if not isinstance(interface.get("capabilities"), list):
        errors.append("interface.capabilities: array required")
    prompts = interface.get("defaultPrompt", [])
    if isinstance(prompts, str):
        prompts = [prompts]
    if not isinstance(prompts, list) or len(prompts) > 3 or any(
        not isinstance(p, str) or not 1 <= len(p) <= 128 for p in prompts
    ):
        errors.append("interface.defaultPrompt: up to three 1–128 character prompts")

    for field in ("logo", "composerIcon"):
        target = interface.get(field)
        if not isinstance(target, str) or not target.startswith("./") or ".." in Path(target).parts:
            errors.append(f"interface.{field}: plugin-relative path required")
        elif not (root / target).is_file():
            errors.append(f"interface.{field}: referenced image is missing")

    try:
        compatibility = load_object(root / ".codex-plugin" / "plugin.json")
        for field in ("name", "version", "description", "author", "license"):
            if compatibility.get(field) != manifest.get(field):
                errors.append(f"compatibility manifest drift: {field}")
        if compatibility.get("skills") != "./skills/":
            errors.append("compatibility skills path must be ./skills/")
        if compatibility.get("interface") != interface:
            errors.append("compatibility interface drift")
        marketplace = load_object(root / ".agents" / "plugins" / "marketplace.json")
        entries = marketplace.get("plugins")
        if not isinstance(entries, list) or len(entries) != 1:
            errors.append("marketplace must contain the single packaged plugin")
        else:
            entry = entries[0]
            if entry.get("name") != manifest.get("name") or entry.get("source") != {"source": "local", "path": "./"}:
                errors.append("marketplace identity/path does not resolve this package")
            if entry.get("policy", {}).get("installation") != "AVAILABLE" or not entry.get("category"):
                errors.append("marketplace policy/category missing")
            if entry.get("policy", {}).get("authentication") != "ON_INSTALL":
                errors.append("marketplace authentication policy missing")
    except (OSError, ValueError, AttributeError) as exc:
        errors.append(str(exc))

    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if actual != EXPECTED_SKILLS:
        errors.append(f"unexpected skill set: {sorted(actual)}")
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        content = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            errors.append(f"{path}: missing frontmatter")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
            if not isinstance(meta, dict):
                raise ValueError("frontmatter must be an object")
            if meta.get("name") != path.parent.name:
                errors.append(f"{path}: skill name mismatch")
            if not isinstance(meta.get("description"), str) or not meta["description"].strip():
                errors.append(f"{path}: missing description")
            ui_path = path.parent / "agents" / "openai.yaml"
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
            if not isinstance(ui, dict) or not isinstance(ui.get("interface"), dict):
                raise ValueError("UI metadata must contain an interface object")
            skill_ui = ui["interface"]
            if not 25 <= len(skill_ui.get("short_description", "")) <= 64:
                errors.append(f"{ui_path}: short_description length")
            prompt = skill_ui.get("default_prompt", "")
            if not isinstance(prompt, str) or "$" + path.parent.name not in prompt:
                errors.append(f"{ui_path}: default_prompt must name its skill")
            if ui.get("policy", {}).get("allow_implicit_invocation") is False:
                errors.append(f"{ui_path}: unexpected explicit-only policy")
        except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{path}: {exc}")
        if re.search(r"\[TODO[^\]]*\]|\bTODO\b", content):
            errors.append(f"{path}: unfinished scaffold")

    for path in package_files(root):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"{relative}: symlinks are not distributable")
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".svg", ".txt"}:
            continue
        content = path.read_text(encoding="utf-8")
        if re.search(r"[\u3400-\u9fff]", content):
            errors.append(f"{relative}: non-English package text")
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
                target = target.strip().strip("<>").split("#", 1)[0]
                if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                resolved = (path.parent / target).resolve()
                if resolved != root and root not in resolved.parents:
                    errors.append(f"{relative}: link escapes package: {target}")
                elif not resolved.exists():
                    errors.append(f"{relative}: broken local link: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--manifest-schema", type=Path, help="Downloaded official schema JSON")
    args = parser.parse_args()
    try:
        errors = validate(Path(args.root), args.manifest_schema)
    except (ValueError, OSError, TypeError, AttributeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: skills, metadata, manifests, marketplace and local references")
    if args.manifest_schema:
        print("PASS: official portable manifest JSON schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
