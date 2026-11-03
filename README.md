# Research Methods 2026

Python programming and reproducible research with coding agents, for PhD
students in economics. Instructor: Swapnil Singh.

[Draft syllabus](syllabus.md)

## Slides

Open the slides directly in your browser. Use the arrow keys, space bar, or swipe
to move through them. No slide download, installation, or compilation is required.

| Session | Slides |
|---|---|
| Before the first class | [Set up your computer](https://swapnil1987.github.io/2026-research-methods/student-setup.html) |
| Day 1, first hour | [Getting a project running](https://swapnil1987.github.io/2026-research-methods/lecture-01.html) |

The setup guide covers Windows, macOS and Linux, Python/JupyterLab, Git, and
Codex installation and sign-in. The first lesson introduces files and folders,
relative paths, running a script, notebook state, and reviewing a small agent
change. No previous Python knowledge is assumed.

## Classroom code and data

- [Download the student starter project](https://swapnil1987.github.io/2026-research-methods/downloads/research-methods-student-kit.zip)
- [Browse the starter code, notebook and synthetic data](codes/lecture-1/)
- [Exercise instructions](codes/lecture-1/README.md)

The ZIP contains the files students run on their computers: code, a notebook,
synthetic data, an environment specification, and setup instructions. Slides are
provided through the browser links above.

## Student setup

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

## Render the slides

Slide authors use the full `environment.yml`, which includes Quarto. If the
student environment is already installed, add the authoring dependencies with
`conda env update --name research-methods --file environment.yml`.

The decks use the Quarto Reveal.js template from
[`2026-topics-in-econometrics-1`](https://github.com/swapnil1987/2026-topics-in-econometrics-1),
including its shared theme and local maths font. See
[slide authoring instructions](slides/README.md).

```bash
bash scripts/render-slides.sh
```

Open `slides/_site/student-setup.html` or `slides/_site/lecture-01.html` locally.
**S** opens speaker notes and **O** opens the overview. Editable sources are
[student-setup.qmd](slides/student-setup.qmd) and
[lecture-01.qmd](slides/lecture-01.qmd).

The GitHub Pages workflow renders the slides and packages the student runtime
files on each relevant push to `main`. It publishes the HTML pages and the code
and data download; generated output remains ignored by Git. For each new
lecture, add its source to `slides/_quarto.yml` and its browser link to this README.
