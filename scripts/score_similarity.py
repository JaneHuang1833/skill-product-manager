#!/usr/bin/env python3
"""Check component evidence shape and compute similarity without imputing unknowns."""

import argparse
from decimal import Decimal
import json
from pathlib import Path
import sys

MAXIMA = {
    "problem_jtbd": Decimal("3.0"),
    "user_context": Decimal("1.5"),
    "workflow": Decimal("2.0"),
    "capabilities_tools": Decimal("2.0"),
    "output_ux": Decimal("1.0"),
    "distribution_form": Decimal("0.5"),
}


def score_similarity(components):
    if not isinstance(components, dict) or set(components) != set(MAXIMA):
        raise ValueError("Provide exactly the six documented dimension keys")
    subtotal = Decimal("0")
    missing = []
    for name, maximum in MAXIMA.items():
        item = components[name]
        if not isinstance(item, dict) or set(item) != {"score", "rationale", "source_ids"}:
            raise ValueError(f"{name}: expected score, rationale, source_ids")
        if not isinstance(item["rationale"], str) or not item["rationale"].strip():
            raise ValueError(f"{name}: a nonempty rationale is required")
        sources = item["source_ids"]
        if not isinstance(sources, list) or any(
            not isinstance(s, str) or not s.strip() for s in sources
        ):
            raise ValueError(f"{name}: source_ids must be an array of nonempty strings")
        raw = item["score"]
        if raw is None:
            missing.append(name)
            continue
        if isinstance(raw, bool) or not isinstance(raw, (int, float, Decimal)):
            raise ValueError(f"{name}: score must be numeric or null")
        value = Decimal(str(raw))
        if not value.is_finite() or not Decimal("0") <= value <= maximum:
            raise ValueError(f"{name}: score outside 0–{maximum}")
        if value % Decimal("0.1") != 0:
            raise ValueError(f"{name}: use increments of 0.1")
        if not sources:
            raise ValueError(f"{name}: a scored dimension requires source IDs")
        subtotal += value
    upper = subtotal + sum((MAXIMA[n] for n in missing), Decimal("0"))
    band = None
    if not missing:
        if subtotal >= 9:
            band = "almost_identical"
        elif subtotal >= 7:
            band = "highly_similar"
        elif subtotal >= 5:
            band = "adjacent"
        elif subtotal >= 3:
            band = "partly_related"
        else:
            band = "weakly_related"
    return {
        "status": "provisional" if missing else "confirmed",
        "total": None if missing else float(subtotal),
        "observed_subtotal": float(subtotal),
        "range": [float(subtotal), float(upper)],
        "missing_dimensions": missing,
        "band": band,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Component JSON path, or - for stdin")
    args = parser.parse_args()
    try:
        raw = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
        print(json.dumps(score_similarity(json.loads(raw)), ensure_ascii=False, indent=2))
    except (ValueError, OSError) as exc:
        print(f"Invalid similarity input: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
