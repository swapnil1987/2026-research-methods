"""Package Day 2 notebooks, scripts and inputs. Slides stay online."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root=Path(__file__).resolve().parents[1]
lesson=root/"codes/day-2"
stems=("01_pandas","02_preparing","03_summaries","04_grammar","05_design","06_tables")
files={name:lesson/name for name in (
    "README.md","lesson_data.py","data/README.md","data/raw/households.csv",
    "data/raw/regions.csv","outputs/README.md",
)}
for stem in stems:
    for extension in (".py",".ipynb"):
        files[stem+extension]=lesson/(stem+extension)
files["environment-student.yml"]=root/"environment-student.yml"
output=root/"slides/_site/downloads/research-methods-day-2.zip"
output.parent.mkdir(parents=True,exist_ok=True)
for source in files.values():
    if not source.is_file():
        raise SystemExit(f"Missing classroom file: {source}")
with ZipFile(output,"w",compression=ZIP_DEFLATED) as archive:
    for name,source in sorted(files.items()):
        archive.write(source,"research-methods-day-2/"+name)
with ZipFile(output) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist())==len(files)
print(f"Created {output} ({len(files)} code/data/setup files; no slides)")
