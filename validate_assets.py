# CI test: automatic build trigger

import csv
import sys
from collections import Counter
from pathlib import Path

file_path = Path(__file__).with_name("assets.csv")

with file_path.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

asset_ids = [
    row["asset_id"].strip()
    for row in rows
]

missing = [
    i + 2
    for i, asset_id in enumerate(asset_ids)
    if not asset_id
]

counts = Counter(
    asset_id for asset_id in asset_ids if asset_id
)

duplicates = {
    asset_id: count
    for asset_id, count in counts.items()
    if count > 1
}

print("=== DATA QUALITY REPORT ===")
print(f"Total records: {len(rows)}")
print(f"Missing asset IDs: {len(missing)}")
print(f"Duplicate asset IDs: {len(duplicates)}")

if missing:
    print(f"Missing ID at CSV row(s): {missing}")

for asset_id, count in duplicates.items():
    print(f"Duplicate ID: {asset_id} ({count} occurrences)")

if missing or duplicates:
    print("VALIDATION FAILED")
    sys.exit(1)

print("VALIDATION PASSED")
sys.exit(0)
