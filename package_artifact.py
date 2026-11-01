from pathlib import Path
import shutil
import sys

source = Path("assets.csv")
output_dir = Path("output")
destination = output_dir / "validated_assets.csv"

if not source.exists():
    print("ERROR: assets.csv not found")
    sys.exit(1)

output_dir.mkdir(exist_ok=True)

shutil.copy2(source, destination)

print(f"Artifact prepared: {destination}")
print(f"Size: {destination.stat().st_size} bytes")
