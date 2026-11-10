"""Check the student installation without changing files or installing software."""

from contextlib import redirect_stdout
import importlib
from io import StringIO
from pathlib import Path
import runpy
import shutil
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    problems = []

    def report(label, passed, help_text):
        print(f"[{'OK' if passed else 'FIX'}] {label}")
        if not passed:
            print(f"      {help_text}")
            problems.append(label)

    report(
        "Python " + sys.version.split()[0],
        sys.version_info[:2] == (3, 12),
        "Run conda activate research-methods, then run this check again.",
    )

    modules = {}
    for name in ("jupyterlab", "ipykernel", "pandas", "numpy", "matplotlib", "plotnine"):
        try:
            modules[name] = importlib.import_module(name)
        except (ImportError, OSError) as error:
            report(
                name,
                False,
                f"{error}. Use the course environment and ask for setup help.",
            )
        else:
            report(name, True, "")

    git_version = ""
    if shutil.which("git"):
        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            if result.returncode == 0:
                git_version = result.stdout.strip()
        except (OSError, subprocess.TimeoutExpired):
            pass
    report(
        git_version or "Git is available",
        bool(git_version),
        "Install Git using the setup guide, then reopen your terminal.",
    )

    lesson = root / "codes" / "lecture-1"
    required = (
        root / "environment-student.yml",
        lesson / "household_saving.py",
        lesson / "project_running.ipynb",
        lesson / "data" / "raw" / "households.csv",
    )
    files_present = all(path.is_file() for path in required)
    report(
        "Starter files",
        files_present,
        "Extract the complete student ZIP; keep its folders together.",
    )

    if files_present and "pandas" in modules:
        try:
            households = modules["pandas"].read_csv(required[-1])
            valid = (
                len(households) == 4
                and households["household_id"].is_unique
            )
        except (OSError, ValueError, KeyError) as error:
            report("Read the synthetic CSV", False, str(error))
        else:
            report(
                "Read four synthetic households",
                valid,
                "Use the unchanged starter data supplied with the course.",
            )

    if files_present:
        output = StringIO()
        try:
            with redirect_stdout(output):
                runpy.run_path(str(lesson / "household_saving.py"))
        except Exception as error:
            report("Run the starter script", False, str(error))
        else:
            report(
                "Monthly saving (EUR): 200",
                output.getvalue().strip() == "Monthly saving (EUR): 200",
                "Restore the starter inputs: income 1000, consumption 800.",
            )

    print()
    if problems:
        print("SETUP NEEDS ATTENTION")
        print("Share the FIX lines and your operating system with the instructor.")
        return 1

    print("SETUP CHECK PASSED")
    print("Next: open the notebook and restart its kernel, then run all cells.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
