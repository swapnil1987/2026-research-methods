# Slide authoring

## Template provenance

The reference is the instructor's local checkout of
`swapnil1987/2026-topics-in-econometrics-1`, at commit
`6fbedda750a41091d322c5fddf44e3a91b7f072a`.
The design follows `slides/template.qmd` and `slides/_quarto.yml`:

- Quarto Reveal.js, 1600 × 900 (16:9), linear navigation and fade transitions.
- Exact copies of `theme/course.scss`, `theme/math-font.html`, the Latin Modern
  Math font, and its accompanying GUST licence.
- White, charcoal, coral, dark red and warm grey; serif headings; large type.
- `.key-idea`, `.definition`, `.exercise`, `.answer`, and `.section-slide`
  teaching components; fragments, code highlighting, and speaker notes.

The reference repository's R-specific settings are replaced with non-executing
Python examples. Their matching script and notebook are checked separately.
`theme/lesson.scss` adds a file-tree style, contrasting terminal output, hides
inactive slides' copy buttons, and preserves the coral section slide when
printing. The shared theme itself is unchanged.
The chalkboard plugin is disabled because Quarto does not support embedding it
in standalone HTML. For an asset-folder build with classroom annotation, set
`embed-resources: false` and `chalkboard: true` in `_quarto.yml`.

## Build and present

The declared course environment is `research-methods` in `../environment.yml`.
Create it using the root README instructions, then run from the repository root:

```bash
bash scripts/render-slides.sh
```

To use an existing compatible Conda environment without changing it:

```bash
RESEARCH_METHODS_ENV=topics-econometrics bash scripts/render-slides.sh
```

Output: `slides/_site/student-setup.html` and the six Day 1 decks,
`slides/_site/lecture-01.html` through `slides/_site/lecture-06.html`.
Resources are embedded for a single-file
handoff. Use a browser for presenting; the `.qmd` is the editable source.
To print, open the HTML with `?print-pdf` appended and print to PDF with browser
headers and footers disabled and background graphics enabled.

If a restricted session cannot write the usual Quarto cache, scope
`XDG_CACHE_HOME` to a writable temporary directory for the build. Do not change
the shared Conda environment to fix a cache permission problem.

## Delivery

`student-setup.qmd` is the self-paced pre-class installation guide. It covers
Miniforge/Conda, Git and GitHub, the student Python environment, JupyterLab, and
Codex desktop installation/sign-in with an IDE alternative. Its sources are
linked on the slides and in `docs/student-setup.md`. Students use
`environment-student.yml`; the full `environment.yml` also includes Quarto for
authors. Both define the environment name `research-methods`.

Link each rendered lecture from the repository's main README. Students open the
slides in their browser. Only the classroom runtime files are packaged for
download. Build that archive with:

```bash
python scripts/package-student-kit.py
```

The result is `slides/_site/downloads/research-methods-student-kit.zip`. It contains only
the installation instructions, student environment, checker and all six lessons'
runtime files, under a single `research-methods/` folder. It contains no slides
or PDFs. GitHub Pages publishes the archive alongside the rendered HTML decks;
build output is ignored by Git.

`lecture-01.qmd` has a 60-minute clock in its speaker notes. It assumes the
instructor's common Python environment is already prepared. Launch JupyterLab
from `codes/lecture-1/`; that folder is the project root in every lesson example.
Keep the slide deck and the live editor side by side. Exercises include time to
predict, run, compare and discuss. Installation troubleshooting should be handled
before class or with a prepared working copy.

For another block, copy `template.qmd`, update its metadata and notes, add
the file to `project.render` in `_quarto.yml`, and add its GitHub Pages browser
link to the main README. Keep generated HTML, PDF, ZIP files and caches under
`_site/` and out of commits.

`lecture-02.qmd` covers the two-hour Basic Python block. Every slide has speaker
notes with a contiguous 120-minute clock. Worked code, expected outputs,
prediction questions, and five numbered notebook exercises use only built-in
Python tools and synthetic household amounts. Its companion notebook and
worked script are in `codes/lecture-2/`; the notebook is distributed without
saved output. Deliberate errors appear as Markdown rather than executable
notebook cells. These classroom materials are linked directly from the README.
`theme/basic-python.css` enlarges code to 30 pixels in Lectures 2–6 for classroom
projection; the original template, setup guide and Lecture 1 retain their styles.

Lectures 3–6 cover the rest of Day 1: conditions, loops and functions (120 minutes),
errors and checks (60), Git and GitHub (60), and reading a dataset (60). Each deck
has timed speaker notes, worked code and outputs, and classroom exercises. The
Python lessons have unexecuted notebooks and runnable scripts; the Git lesson
uses a terminal/browser handout and a practice starter. Class code and data live
under the matching `codes/lecture-N/` folders. They are separate from the graded
Exercise 1 task sheet.
