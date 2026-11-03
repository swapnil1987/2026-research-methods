# Day 1 course materials — 3 November 2026

The repository README links to six HTML lectures using the existing Quarto
Reveal.js course template. The preparation deck is separate.

| Lecture | Topic | Slides | Contact minutes |
|---|---|---:|---:|
| 1 | Getting a project running | 27 | 60 |
| 2 | Basic Python | 43 | 120 |
| 3 | Conditions, loops and functions | 39 | 120 |
| 4 | Reading errors and checking calculations | 25 | 60 |
| 5 | First steps with Git and GitHub | 26 | 60 |
| 6 | First look at a dataset | 26 | 60 |
| **Total** | | **186** | **480** |

Breaks are additional. No Day 2 or Day 3 teaching schedule has been reinstated.
Classroom practice and visible worked answers are separate from the graded
Exercise 1 task sheet and unreleased individual assessment questions.

## Build

Quarto 1.9.38 in the repository's documented compatible environment:

```bash
XDG_CACHE_HOME=/tmp/research-methods-quarto-cache \
RESEARCH_METHODS_ENV=topics-econometrics bash scripts/render-slides.sh
python3 scripts/package-student-kit.py
```

All seven presentations, including the setup guide, render successfully.
Generated HTML, PDF previews, download archives and QA evidence stay under
ignored paths. Slide sources and classroom inputs remain in Git.

## Code and data verification

The new teaching code was checked in Python 3.12.16 using `research-methods`.
The distributed notebooks contain no saved output. Their executable cells
match copies run in fresh course kernels:

| Notebook | Executed code cells |
|---|---:|
| Basic Python | 44 |
| Conditions, loops and functions | 37 |
| Errors and checks | 20 |
| First dataset | 24 |
| **Total** | **125** |

Slide outputs, intentional exceptions, function boundaries and worked script
results were checked by each lesson's author. Read-only cross-review corrected
the indentation wording, local-variable terminology and existing-clone Git
starting sequence. The shared `saving_share` contract is explicit in Lectures
3 and 4: numeric finite non-negative inputs are assumed; negative amounts are
rejected, zero income produces `None`, and negative saving is allowed.

Git practice was tested with 53 commands in an isolated local clone and bare
remote. Its `main` stayed unchanged. Student classroom instructions use unique
public-username branches and files; only the instructor may update course
`main`. No real student PR or collaborator invitation was created during tests.

The Lecture 6 CSV is a byte-identical copy of the original synthetic fixture.
Savings are `[200, 400, 500, -50]`, total 1050 EUR/month, mean 262.50
EUR/household/month. Script and notebook exports have four rows and two columns;
raw inputs remain unchanged.

## Rendered review

The five new decks, Lectures 2–6, were inspected at 1600 × 900 and 390 × 844.
All 159 slides have notes, 30-pixel code, working navigation and PDF page counts
matching their slide counts. Automated checks cover slide/footer boundaries,
actual text ranges within code blocks, JavaScript exceptions, requests, menu,
overview and horizontal document overflow.

All new slides were visually reviewed through contact sheets, with full-size
inspection of dense code, traceback, Git and exercise examples. Two clipped
examples were fixed: Lecture 3's reporting loop now uses the full slide width;
Lecture 4's calculation and traceback use compact lines with matching frame
numbers. Lecture 2's clarified prediction instructions were also checked.

The narrow-screen footer is hidden to avoid the menu collision. Reveal's
standard mobile scroll navigation is retained. The shared course SCSS is
unchanged; these adjustments live in the lesson-specific code stylesheet.

## Student delivery and publication

The classroom download contains exactly 24 explicitly listed code, notebook,
CSV, environment and instruction files. It contains no slides, PDFs, caches,
executed notebooks or the owner's unrelated `Untitled.ipynb`.

The GitHub Pages workflow renders all lectures and packages the classroom
files on the publishing push. Deployment validation checks the workflow
conclusion, all seven HTML routes, representative desktop/mobile rendered
states, and the downloaded archive's contents against the source files.
Exact release commit, run and live-check evidence is retained locally under
`.cache/day-1-release/` and in GitHub Actions.
