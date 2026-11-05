# Coding Assignment 1

Student task sheet: [Assignment 1 (PDF)](assignment-01.pdf).
Editable LaTeX source: `main.tex`.

The assignment uses Day 1 Lectures 1–4: project execution, basic Python,
conditions, loops, functions, lambda expressions, debugging, and checks.
It uses hard-coded synthetic lists rather than the dataset lesson. Git is
not assessed; students submit a notebook and README through a pull request.

Deadline: Monday 9 November 2026 at 23:59, Europe/Vilnius time.
The submission is marked out of 100 and contributes 10% of the whole course;
the separate individual test contributes 15%.

The task sheet contains no instructor solution or answer key. Validation
solutions are kept outside the public repository.

Build from this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.build main.tex
```

The compiled assignment is `.build/main.pdf`; build intermediates are ignored.
The reviewed student PDF is published as `assignment-01.pdf`.
