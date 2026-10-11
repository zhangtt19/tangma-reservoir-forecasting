"""Verify and extract the original model from three download parts."""
from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parent
archive = json.loads((root / "manifest.json").read_text(encoding="utf-8"))["archive"]
target = root / archive["name"]
output = root / "tangma-model"
if target.exists() or output.exists():
    raise SystemExit("Output already exists. Use a fresh folder to avoid overwriting files.")
for part in archive["parts"]:
    data = (root / part["name"]).read_bytes()
    if len(data) != part["bytes"] or hashlib.sha256(data).hexdigest() != part["sha256"]:
        raise SystemExit("Part checksum failed: " + part["name"])
with target.open("xb") as dest:
    for part in archive["parts"]:
        dest.write((root / part["name"]).read_bytes())
if hashlib.sha256(target.read_bytes()).hexdigest() != archive["sha256"]:
    raise SystemExit("Combined ZIP checksum failed.")
with zipfile.ZipFile(target) as z:
    for entry in z.infolist():
        resolved = (output / entry.filename).resolve()
        if not resolved.is_relative_to(output.resolve()):
            raise SystemExit("Unsafe archive path: " + entry.filename)
    z.extractall(output)
print("Verified model extracted to:", output)
