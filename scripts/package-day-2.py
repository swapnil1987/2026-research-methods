"""Package only Day 2 classroom runtime files; slides stay online."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
lesson = root / "codes/day-2"
files = {
    "README.md": lesson / "README.md",
    "data_science.ipynb": lesson / "data_science.ipynb",
    "worked_analysis.py": lesson / "worked_analysis.py",
    "data/README.md": lesson / "data/README.md",
    "data/raw/households.csv": lesson / "data/raw/households.csv",
    "data/raw/regions.csv": lesson / "data/raw/regions.csv",
    "outputs/README.md": lesson / "outputs/README.md",
    "environment-student.yml": root / "environment-student.yml",
}
output = root / "slides/_site/downloads/research-methods-day-2.zip"
output.parent.mkdir(parents=True, exist_ok=True)
for source in files.values():
    if not source.is_file():
        raise SystemExit(f"Missing classroom file: {source}")
with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
    for name, source in sorted(files.items()):
        archive.write(source, "research-methods-day-2/" + name)
with ZipFile(output) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(files)
print(f"Created {output} ({len(files)} code/data/setup files; no slides)")
