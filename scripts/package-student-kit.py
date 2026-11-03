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
    "codes/lecture-2/README.md": "codes/lecture-2/README.md",
    "codes/lecture-2/basic_python.py": "codes/lecture-2/basic_python.py",
    "codes/lecture-2/basic_python.ipynb": "codes/lecture-2/basic_python.ipynb",
    "codes/lecture-3/README.md": "codes/lecture-3/README.md",
    "codes/lecture-3/control_flow.py": "codes/lecture-3/control_flow.py",
    "codes/lecture-3/control_flow.ipynb": "codes/lecture-3/control_flow.ipynb",
    "codes/lecture-4/README.md": "codes/lecture-4/README.md",
    "codes/lecture-4/checking_calculations.py": "codes/lecture-4/checking_calculations.py",
    "codes/lecture-4/checking_calculations.ipynb": "codes/lecture-4/checking_calculations.ipynb",
    "codes/lecture-5/README.md": "codes/lecture-5/README.md",
    "codes/lecture-5/saving_start.py": "codes/lecture-5/saving_start.py",
    "codes/lecture-6/README.md": "codes/lecture-6/README.md",
    "codes/lecture-6/first_dataset.py": "codes/lecture-6/first_dataset.py",
    "codes/lecture-6/first_dataset.ipynb": "codes/lecture-6/first_dataset.ipynb",
    "codes/lecture-6/data/raw/households.csv": "codes/lecture-6/data/raw/households.csv",
    "codes/lecture-6/outputs/README.md": "codes/lecture-6/outputs/README.md",
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
