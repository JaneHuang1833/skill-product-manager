import copy
import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "score_similarity.py"
spec = importlib.util.spec_from_file_location("score_similarity", MODULE_PATH)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def components():
    return {
        k: {"score": float(v), "rationale": "Verified overlap", "source_ids": ["S1"]}
        for k, v in helper.MAXIMA.items()
    }


class SimilarityTests(unittest.TestCase):
    def test_all_dimensions_add_to_ten_without_double_weighting(self):
        result = helper.score_similarity(components())
        self.assertEqual(result["total"], 10)
        self.assertEqual(result["range"], [10, 10])
        self.assertEqual(result["band"], "almost_identical")

    def test_unknown_is_not_zero_or_a_normalized_confirmed_total(self):
        data = components()
        data["distribution_form"] = {"score": None, "rationale": "Missing source", "source_ids": []}
        result = helper.score_similarity(data)
        self.assertEqual(result["status"], "provisional")
        self.assertIsNone(result["total"])
        self.assertIsNone(result["band"])
        self.assertEqual(result["range"], [9.5, 10])

    def test_all_unknown_preserves_full_uncertainty(self):
        data = components()
        for item in data.values():
            item["score"] = None
            item["source_ids"] = []
        result = helper.score_similarity(data)
        self.assertEqual(result["range"], [0, 10])
        self.assertEqual(len(result["missing_dimensions"]), 6)

    def test_confirmed_zero_requires_evidence(self):
        data = components()
        for item in data.values():
            item["score"] = 0
        self.assertEqual(helper.score_similarity(data)["total"], 0)
        data["workflow"]["source_ids"] = []
        with self.assertRaises(ValueError):
            helper.score_similarity(data)

    def test_invalid_scores_cannot_enter_a_ranking(self):
        for value in [-0.1, 3.1, True, "3", float("nan"), float("inf"), 0.15]:
            with self.subTest(value=value):
                data = components()
                data["problem_jtbd"]["score"] = value
                with self.assertRaises(ValueError):
                    helper.score_similarity(data)

    def test_incomplete_or_unsupported_contract_rejected(self):
        data = components()
        del data["workflow"]
        with self.assertRaises(ValueError):
            helper.score_similarity(data)
        data = components()
        data["extra"] = copy.deepcopy(data["workflow"])
        with self.assertRaises(ValueError):
            helper.score_similarity(data)

    def test_rationale_and_source_shape_required(self):
        for field, value in [("rationale", " "), ("source_ids", "S1"), ("source_ids", [""])]:
            data = components()
            data["workflow"][field] = value
            with self.assertRaises(ValueError):
                helper.score_similarity(data)

    def test_decimal_arithmetic_and_band_boundary(self):
        data = components()
        data["problem_jtbd"]["score"] = 2.9
        data["user_context"]["score"] = 0.5
        self.assertEqual(helper.score_similarity(data)["total"], 8.9)
        self.assertEqual(helper.score_similarity(data)["band"], "highly_similar")


if __name__ == "__main__":
    unittest.main()
