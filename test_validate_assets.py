import unittest
from validate_assets import validate_asset_ids


class TestAssetValidation(unittest.TestCase):

    def test_valid_asset_ids(self):
        missing, duplicates = validate_asset_ids(
            ["A101", "A102", "A103"]
        )
        self.assertEqual(missing, [])
        self.assertEqual(duplicates, {})

    def test_missing_asset_id(self):
        missing, duplicates = validate_asset_ids(
            ["A101", "", "A103"]
        )
        self.assertEqual(missing, [3])
        self.assertEqual(duplicates, {})

    def test_duplicate_asset_id(self):
        missing, duplicates = validate_asset_ids(
            ["A101", "A102", "A101"]
        )
        self.assertEqual(missing, [])
        self.assertEqual(duplicates, {"A101": 2})


if __name__ == "__main__":
    unittest.main()
