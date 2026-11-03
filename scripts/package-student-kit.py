"""Package classroom code and data for download; presentations stay online."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


root = Path(__file__).resolve().parents[1]
output = root / "slides" / "_site" / "downloads" / "research-methods-student-kit.zip"
files = {
    "README.md": "docs/student-setup.md",
    "environment-student.yml": "environment-student.yml",
    "scripts/check_setup.py": "scripts/check_setup.py",
    "codes/lecture-1/README.md": "codes/lecture-1/README.md",
    "codes/lecture-1/household_saving.py": "codes/lecture-1/household_saving.py",
    "codes/lecture-1/project_running.ipynb": "codes/lecture-1/project_running.ipynb",
    "codes/lecture-1/data/raw/households.csv": "codes/lecture-1/data/raw/households.csv",
    "codes/lecture-1/outputs/README.md": "codes/lecture-1/outputs/README.md",
}

for source in files.values():
    if not (root / source).is_file():
        raise SystemExit(f"Missing student file: {source}")

output.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
    for destination, source in sorted(files.items()):
        archive.write(root / source, f"research-methods/{destination}")

with ZipFile(output) as archive:
    damaged = archive.testzip()
    if damaged:
        raise SystemExit(f"ZIP integrity check failed: {damaged}")

print(f"Created {output} ({len(files)} files)")
