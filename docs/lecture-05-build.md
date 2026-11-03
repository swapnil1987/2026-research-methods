# Lecture 5 — First steps with Git and GitHub

Draft authored and checked on 3 November 2026 in the course checkout, based on
commit `b9b477f6efd48bb82a5e8b3a7062c6043f3da8aa`. Rendering, visual review,
README integration, and publication are coordinated by the root agent. This
authoring task made no changes to the course repository's Git history or remote.

## Delivered sources

- `slides/lecture-05.qmd`: 26 slides for the one-hour Day 1 Git block. Every
  slide has speaker notes; contiguous minute:second Clock intervals total
  exactly 60 minutes, including a five-minute individual exercise and debrief.
- `codes/lecture-5/saving_start.py`: a minimal synthetic household calculation,
  to be copied into a student's personal practice folder before editing.
- `codes/lecture-5/README.md`: the complete classroom workflow, placeholders,
  authentication guidance, expected results, and primary references.

The deck inherits the existing Reveal.js template and
`theme/basic-python.css`. It does not modify shared styles. Each content slide
contains shell commands, Python, a diff, file content, or a workflow diagram.
No notebook is needed for this shell-and-browser lesson.

Students clone the public course repository, create a unique
`practice/YOUR-GITHUB-USERNAME` branch, and make
`practice/YOUR-GITHUB-USERNAME/saving.py`. They verify and commit the baseline,
change income from 1000 to 1200, inspect a bounded diff, commit the checked
change, push the personal branch, and open a browser PR to `main`. Only the
instructor may push or merge to `main`. Private grade IDs are never used in
public branch names or PRs. Classroom practice is distinguished from the graded
Exercise 1 task sheet.

## Verification

The course checkout was verified as `main` before authoring. Validation used
Git 2.43.0 and Python from the `research-methods` environment. The sandbox
command was:

```bash
~/miniconda3/envs/research-methods/bin/python \
  .cache/lecture-05/check_workflow.py
```

All Git mutations occurred under the isolated temporary directory
`/tmp/research-methods-lecture-05-gx4z0w4a`, using a local bare remote, seed
repository, and student clone. The 53 recorded commands verified:

- clone, remote inspection, clean status, switching from a previous personal
  branch to `main`, and fast-forward-only pull before a new practice branch;
- repository-local commit identity and personal branch creation;
- baseline script output `Monthly saving (EUR): 200`;
- explicit-path staging, staged addition and staged diff inspection;
- baseline commit and single-line income change, producing saving `400`;
- unstaged versus staged differences, second commit, and history inspection;
- first push with upstream, subsequent push, and matching local/remote branch;
- unchanged remote `main`, an unrelated untracked file preserved and excluded
  from commits, and the course's generated-output ignore pattern.

All 22 shell command blocks passed `bash -n`. The starter's output, code or
commands on every content slide, 26 speaker-note intervals, 60-minute duration,
and scoped Git whitespace checks passed. The command transcript, Git version,
mock commit hashes and checks are recorded in
`.cache/lecture-05/validation.json` (ignored by Git).

No real GitHub push, invitation, authentication attempt, or PR was performed.
The actual classroom push requires the student's accepted collaborator
invitation and prepared HTTPS credentials. Browser labels and authentication
guidance were checked against official GitHub documentation. Git command
semantics were checked against official Git documentation. References are
linked in the handout and relevant speaker notes.

The fenced example `## main...origin/main` is Git output, not a slide heading.
Count actual parsed/rendered slides rather than raw `^## ` lines.
