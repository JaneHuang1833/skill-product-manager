#!/usr/bin/env python3
"""Build a deterministic, allowlisted plugin ZIP and a SHA-256 checksum."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT_FILES = {
    "plugin.json", "README.md", "ARCHITECTURE.md", "LICENSE", "CHANGELOG.md",
    "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "PRIVACY.md",
    "SUPPORT.md", "ROADMAP.md", "requirements-dev.txt",
    ".gitignore", ".gitattributes", ".editorconfig",
}
DIRECTORIES = {
    "skills", "references", "scripts", "assets", "docs", "examples", "tests",
    ".codex-plugin", ".agents",
}
SKIP_PARTS = {"__pycache__", ".git", ".venv", "venv", "dist", "discovery"}
ALLOWED_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".svg", ".txt"}
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def select_files(root):
    root = Path(root).resolve()
    selected = []
    for name in sorted(ROOT_FILES):
        path = root / name
        if path.is_symlink():
            raise ValueError(f"Refusing symlink: {name}")
        if path.is_file():
            selected.append(path)
    for name in sorted(DIRECTORIES):
        folder = root / name
        if folder.is_symlink():
            raise ValueError(f"Refusing symlink directory: {name}")
        if not folder.is_dir():
            continue
        for path in sorted(folder.rglob("*")):
            relative = path.relative_to(root)
            if any(p in SKIP_PARTS or p.startswith(".env") for p in relative.parts):
                continue
            if path.is_symlink():
                raise ValueError(f"Refusing symlink: {relative}")
            if path.is_file() and path.suffix in ALLOWED_SUFFIXES:
                selected.append(path)
    return sorted(selected, key=lambda p: p.relative_to(root).as_posix())


def build(root, output=None):
    root = Path(root).resolve()
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest.get("name", ""), manifest.get("version", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Invalid archive package name")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version):
        raise ValueError("Invalid release version")
    selected = select_files(root)
    if not (root / "LICENSE").is_file() or not any(
        p.name == "SKILL.md" for p in selected
    ):
        raise ValueError("A release needs a license and at least one skill")
    output = Path(output).resolve() if output else root / "dist"
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{name}-{version}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in selected:
            relative = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(f"{name}/{relative}", date_time=FIXED_TIME)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes(), compresslevel=9)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(archive.suffix + ".sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return archive, checksum


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        archive, checksum = build(args.root, args.output)
    except (OSError, ValueError, TypeError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    print(archive)
    print(checksum)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
