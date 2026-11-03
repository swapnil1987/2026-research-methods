# Research Methods 2026

Python programming and reproducible research with coding agents, for PhD
students in economics. 

Instructor: Swapnil Singh.

[Syllabus](syllabus.md)

##  Lecture Slides


| Session | Slides |
|---|---|
| Before the first class | [Set up your computer](https://swapnil1987.github.io/2026-research-methods/student-setup.html) |
| Day 1, Lecture 1 | [Getting a project running](https://swapnil1987.github.io/2026-research-methods/lecture-01.html) |

## Grading at a glance

![Grading: programming and research 67%, writing 33%. Each exercise contributes 10% for the submission and 15% for an individual test; the final practical contributes 17%. Passing requires at least 50/100 overall and 23.5/47 across the independent assessments combined.](docs/figures/grading-overview.png)

[Assessment details](syllabus.md#assessment-and-grading) · [Open the figure as a PDF](docs/figures/grading-overview.pdf)

## Code and data

- [Download the student starter project](https://swapnil1987.github.io/2026-research-methods/downloads/research-methods-student-kit.zip)
- [Browse the starter code, notebook and synthetic data](codes/lecture-1/)
- [Exercise instructions](codes/lecture-1/README.md)

The ZIP contains the files students run on their computers: code, a notebook,
synthetic data, an environment specification, and setup instructions. Slides are
provided through the browser links above.

## Environment setup

The common local setup uses Python 3.12 and JupyterLab. Follow the
[student setup guide](docs/student-setup.md) to install Miniforge and Git, or
reuse an existing Conda installation. From the extracted starter project or full
repository root:

```bash
conda env create --file environment-student.yml
conda activate research-methods
python scripts/check_setup.py
cd codes/lecture-1
python household_saving.py
jupyter lab
```

The script should print `Monthly saving (EUR): 200`. Open
`project_running.ipynb` in JupyterLab. Codex installation, sign-in and a local
project check are included in the setup guide.
