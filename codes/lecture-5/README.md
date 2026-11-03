# First steps with Git and GitHub — Lecture 5

This one-hour lesson practises one public-repository workflow: work on a
personal branch, record checked changes, push that branch, and open a pull
request. It is classroom practice. The graded Exercise 1 will have its own
task sheet, rubric, paths, and deadline.

The course repository is public. Only the instructor may push or merge to
`main`. Students need their own GitHub accounts, accepted collaborator
invitations, and prepared Git authentication to push a branch.

## Before you start

Use the prepared terminal for Git commands. Use the course Python environment
when running Python. Do not enter Git commands into a Python code cell.

Replace `YOUR-GITHUB-USERNAME` in every path and branch name below with your
public GitHub username. Do not substitute the private grade ID.

If you have a Git clone already, open its repository root. If you only have a
downloaded starter ZIP, make a separate clone from its intended parent folder:

```bash
git clone https://github.com/swapnil1987/2026-research-methods.git
cd 2026-research-methods
```

Check the starting point:

```bash
git status --short --branch
git remote get-url origin
```

A clean clone starts on `main` with remote
`https://github.com/swapnil1987/2026-research-methods.git`. For an existing clone,
inspect any changes first. Preserve unexplained changes and ask for help;
do not discard them to match an example. When the working tree is clean,
switch to `main` and update it before creating the practice branch:

```bash
git switch main
git pull --ff-only
```

Configure the identity recorded in commits if necessary. Replace the quoted
placeholders with your actual details:

```bash
git config --local user.name "YOUR NAME"
git config --local user.email "YOUR COMMIT EMAIL"
```

For email privacy, copy the exact no-reply address from GitHub's email settings.
Commit identity does not authenticate you. For HTTPS, use the prepared
credential setup, such as Git Credential Manager. GitHub account passwords do
not authenticate Git HTTPS operations. If authentication fails, keep your local
commits and ask for setup help; never put a token in a command or shared file.

## 1. Create a personal branch and file

```bash
git switch -c practice/YOUR-GITHUB-USERNAME
git branch --show-current
```

In the editor or JupyterLab file browser, create
`practice/YOUR-GITHUB-USERNAME/saving.py` inside this clone. Copy the contents
of [`saving_start.py`](saving_start.py) into it. Keep the shared starter file
unchanged. From the repository root, run:

```bash
python practice/YOUR-GITHUB-USERNAME/saving.py
```

Expected output:

```text
Monthly saving (EUR): 200
```

This is one synthetic household: income 1000 and consumption 800 EUR per month.
Check `1000 - 800 = 200` by hand.

## 2. Record the baseline

```bash
git status --short
git add -- practice/YOUR-GITHUB-USERNAME/saving.py
git diff --cached -- practice/YOUR-GITHUB-USERNAME/saving.py
git commit -m "Add baseline household saving calculation"
git status --short
git log --oneline -1
```

Stage only the intended file. `git add` stages its current content, `git diff
--cached` shows the staged change, and `git commit` records it locally. A clean
`git status --short` prints no changed paths. Commit hashes differ between
students. If unrelated files remain listed, preserve them and inspect them.

## 3. Make, check, and record one change

Change income from `1000` to `1200` in your own `saving.py`; leave consumption
at `800`. Save the file, predict the answer, then run:

```bash
python practice/YOUR-GITHUB-USERNAME/saving.py
git diff -- practice/YOUR-GITHUB-USERNAME/saving.py
git status --short
```

Expected saving is `400`. The diff should show the income line changing from
1000 to 1200. Plain `git diff` shows unstaged changes; after staging, inspect
the staged diff instead:

```bash
git add -- practice/YOUR-GITHUB-USERNAME/saving.py
git diff --cached -- practice/YOUR-GITHUB-USERNAME/saving.py
git commit -m "Check saving with income of 1200 EUR"
git log --oneline -2
```

If you edit again after staging, repeat `git add` for that file and inspect the
staged diff before committing. A commit records the staged version, not every
edit in the working folder.

## 4. Push your branch and open a PR

```bash
git branch --show-current
git push -u origin practice/YOUR-GITHUB-USERNAME
git status --short --branch
```

On GitHub, open the course repository, choose **Pull requests → New pull
request**, and select:

```text
base: main
compare: practice/YOUR-GITHUB-USERNAME
```

Check **Files changed** contains only your practice file. Use a clear title
and describe the input change, the hand calculation, and the result of running
the script. Open the PR and leave it for instructor review. Do not merge it.

For an instructor-requested correction, edit and test the file on the same
branch, make another bounded commit, and run `git push`. The existing PR then
includes that commit. For graded work, the syllabus's captured deadline version
remains the original submission; a later push does not change that version.

## Before sharing

Review `git status --short` and `git diff --cached --name-only`. Keep private
grade IDs, credentials, and confidential data out of public files and PRs.
Preserve supplied source data. The course `.gitignore` excludes several caches
and generated output paths; it does not replace inspection of what is staged
or remove files already tracked.

## References

- [Git: staging with git add](https://git-scm.com/docs/git-add)
- [Git: comparing changes](https://git-scm.com/docs/git-diff)
- [GitHub: cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [GitHub: setting a commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)
- [GitHub: credential storage and authentication](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)
- [GitHub: creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)
