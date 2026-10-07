#!/usr/bin/env python3
"""Run package checks and meaningful regression tests."""

from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    commands = [
        [sys.executable, str(root / "scripts" / "validate_package.py"), str(root)],
        [sys.executable, "-m", "unittest", "discover", "-s", str(root / "tests"), "-p", "test_*.py", "-v"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=root, check=False)
        if result.returncode:
            return result.returncode
    print("PASS: all local checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
