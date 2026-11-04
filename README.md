# Research Methods 2026

Python programming and reproducible research with coding agents, for PhD
students in economics. 

Instructor: Swapnil Singh.

[Syllabus](syllabus.md)

##  Lecture Slides


| Session | Time | Slides |
|---|---|---|
| Before the first class | Self-paced | [Set up your computer](https://swapnil1987.github.io/2026-research-methods/student-setup.html) |
| Day 1, Lecture 1 | 1 hour | [Getting a project running](https://swapnil1987.github.io/2026-research-methods/lecture-01.html) |
| Day 1, Lecture 2 | 2 hours | [Basic Python](https://swapnil1987.github.io/2026-research-methods/lecture-02.html) |
| Day 1, Lecture 3 | 2 hours | [Conditions, loops and functions](https://swapnil1987.github.io/2026-research-methods/lecture-03.html) |
| Day 1, Lecture 4 | 1 hour | [Reading errors and checking calculations](https://swapnil1987.github.io/2026-research-methods/lecture-04.html) |
| Day 1, Lecture 5 | 1 hour | [First steps with Git and GitHub](https://swapnil1987.github.io/2026-research-methods/lecture-05.html) |
| Day 1, Lecture 6 | 1 hour | [First look at a dataset](https://swapnil1987.github.io/2026-research-methods/lecture-06.html) |

Day 1 contains eight contact hours. Open each lecture directly in your browser.

Lecture 3 covers regular functions after loops, followed by
[inline functions (`lambda`)](https://swapnil1987.github.io/2026-research-methods/lecture-03.html#/inline-functions-with-lambda).

## Grading at a glance

![Grading: programming and research 67%, writing 33%. Each exercise contributes 10% for the submission and 15% for an individual test; the final practical contributes 17%. Passing requires at least 50/100 overall and 23.5/47 across the independent assessments combined.](docs/figures/grading-overview.png)

[Assessment details](syllabus.md#assessment-and-grading) · [Open the figure as a PDF](docs/figures/grading-overview.pdf)

## Code and data

- [Download the Day 1 code and data](https://swapnil1987.github.io/2026-research-methods/downloads/research-methods-student-kit.zip)
- [Browse the starter code, notebook and synthetic data](codes/lecture-1/)
- [Exercise instructions](codes/lecture-1/README.md)
- [Basic Python notebook, worked script, and classroom exercises](codes/lecture-2/)
- [Conditions, loops and functions](codes/lecture-3/)
- [Reading errors and checking calculations](codes/lecture-4/)
- [Git and GitHub classroom practice](codes/lecture-5/)
- [First dataset notebook, script, and CSV](codes/lecture-6/)

The ZIP contains the files students run on their computers: code, notebooks,
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
