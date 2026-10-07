import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


validator = module("validate_package")
builder = module("build_release")


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "arbitrary-checkout"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__", "dist"))

    def change_json(self, relative, mutate):
        path = self.root / relative
        data = json.loads(path.read_text())
        mutate(data)
        path.write_text(json.dumps(data))

    def test_checkout_name_is_not_plugin_identity(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_manifest_drift_is_rejected(self):
        self.change_json(".codex-plugin/plugin.json", lambda d: d.update(version="9.9.9"))
        self.assertTrue(any("drift" in e for e in validator.validate(self.root)))

    def test_broken_and_escaping_references_are_rejected(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[missing](missing.md)\n[escape](../private.md)\n")
        errors = validator.validate(self.root)
        self.assertTrue(any("broken local link" in e for e in errors))
        self.assertTrue(any("escapes package" in e for e in errors))

    def test_malformed_manifest_returns_errors(self):
        (self.root / "plugin.json").write_text("not JSON")
        self.assertTrue(validator.validate(self.root))

    def test_malformed_ui_returns_errors(self):
        (self.root / "skills/idea-framing/agents/openai.yaml").write_text("- wrong shape\n")
        self.assertTrue(any("interface object" in e for e in validator.validate(self.root)))

    def test_marketplace_path_cannot_point_outside_package(self):
        self.change_json(".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["source"].update(path="../private"))
        self.assertTrue(any("marketplace identity/path" in e for e in validator.validate(self.root)))

    def test_missing_source_reference_is_rejected_by_cli(self):
        path = self.root / "references/idea-brief-template.md"
        path.unlink()
        result = subprocess.run([sys.executable, str(self.root / "scripts/validate_package.py"), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("broken local link", result.stderr)

    def test_build_reproducible_and_excludes_private_work(self):
        for relative in (".env", "discovery/private.md", ".venv/private.txt", "scripts/__pycache__/private.py", "notes/private.md"):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("private marker")
        first, checksum = builder.build(self.root)
        content = first.read_bytes()
        self.assertEqual(builder.build(self.root)[0].read_bytes(), content)
        self.assertIn(first.name, checksum.read_text())
        with zipfile.ZipFile(first) as archive:
            names = archive.namelist()
            self.assertIn("skill-product-manager/plugin.json", names)
            self.assertIn("skill-product-manager/references/io-contracts.md", names)
            self.assertEqual(sum(n.endswith("/SKILL.md") for n in names), 7)
            self.assertFalse(any("private" in n or ".env" in n or "__pycache__" in n for n in names))

    def test_extracted_archive_is_self_contained(self):
        archive, _ = builder.build(self.root)
        target = Path(self.temp.name) / "extracted"
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(target)
        self.assertEqual(validator.validate(target / "skill-product-manager"), [])

    def test_symlink_cannot_exfiltrate_external_file(self):
        target = Path(self.temp.name) / "private.txt"
        target.write_text("private")
        path = self.root / "references/leak.txt"
        try:
            path.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable on this platform")
        with self.assertRaises(ValueError):
            builder.build(self.root)

    def test_archive_name_cannot_escape_output(self):
        self.change_json("plugin.json", lambda d: d.update(name="../outside"))
        with self.assertRaises(ValueError):
            builder.build(self.root)


if __name__ == "__main__":
    unittest.main()
