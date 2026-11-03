# Lecture 2 — Basic Python

Built and checked on 3 November 2026, originally based on course commit
`b9b477f6efd48bb82a5e8b3a7062c6043f3da8aa`. This lecture is part of the
six-lecture Day 1 release. See [integrated build checks](day-1-build.md) and the
repository README for the browser links.

## Teaching material

- `slides/lecture-02.qmd`: 43 slides for the syllabus's two-hour Basic Python
  block, with speaker notes and contiguous timing from 00:00 to 120:00
  (minutes:seconds). Practice and debriefs are included; breaks are additional.
- Topics: variables and assignment, comments and units, arithmetic and numeric
  types, shares and percentages, floating-point representation, strings,
  conversions, formatting, comparisons, Boolean combinations, lists, indexing,
  slicing, changes, copying, and simple summaries.
- Code appears on every content slide. Worked outputs, prediction questions,
  five numbered notebook exercises, an additional tracing activity, and a final
  household report use synthetic amounts in EUR per month.
- `codes/lecture-2/basic_python.ipynb`: 44 code cells, supplied without saved
  output. The deliberate TypeError is shown as Markdown. Worked answers are
  visible because this is classroom practice, separate from graded take-home work.
- `codes/lecture-2/basic_python.py`: a runnable worked script using built-in
  Python tools, with no extra data files or packages.
- `codes/lecture-2/README.md`: setup, individual-file download instructions,
  expected results, exercise checks, and Python 3.12 references.

The shared econometrics-derived theme is unchanged. The deck-specific
`slides/theme/basic-python.css` sets both input and output code to 30 pixels
for projection. The notebook and script are linked directly; no slide archive
was created and the existing first-lesson starter ZIP was not changed.

## Build and checks

Quarto 1.9.38 in the existing compatible `topics-econometrics` environment:

```bash
XDG_CACHE_HOME=/tmp/research-methods-quarto-cache \
RESEARCH_METHODS_ENV=topics-econometrics bash scripts/render-slides.sh
```

For a subsequent change affecting only this deck:

```bash
XDG_CACHE_HOME=/tmp/research-methods-quarto-cache \
~/miniconda3/bin/conda run --no-capture-output \
  --name topics-econometrics quarto render slides/lecture-02.qmd
```

Local verification used Python 3.12.16 in `research-methods`. All 43 Python
slide blocks were executed and compared with their displayed outputs or an
explicit expected answer; the single deliberate TypeError occurred as intended.
The runnable script passed its baseline and changed-consumption checks.

All 44 notebook code cells executed in a fresh `research-methods` Jupyter kernel
without errors. The executed copy is retained only under `.cache/lecture-02/`.
The distributed notebook is still unexecuted, and its code matches that checked
copy. Notebook structure, 43 speaker-note intervals totalling 120 minutes, and
Git whitespace checks passed.

The final local HTML was checked in Chromium/Playwright at 1600 × 900 and
390 × 844. All 43 slides were captured. Automated checks found no slide-boundary
overflows, JavaScript exceptions, failed requests, or mobile document overflow.
Every code block computes to 30 pixels. Keyboard navigation, overview and the
slide menu worked. The PDF export contains 43 pages.

Outputs are `slides/_site/lecture-02.html` and `slides/_site/lecture-02.pdf`.
Browser reports, screenshots, contact sheets and PDF previews are under
`slides/_site/qa-lecture-02/` and `.cache/lecture-02/`. All generated artifacts
and QA evidence are ignored by Git.

Slide 8's exercise instructions were clarified into separate predictions for
the first and second `print`, followed by running and explaining the result.
The notebook mirrors that change. The executable code is unchanged.
