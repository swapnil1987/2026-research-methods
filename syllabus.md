# Research Methods 2026

## Python programming and reproducible research with coding agents

**Instructor:** [Swapnil  Singh](https://swapnil1987.github.io)
**Contact time:** 24 hours, comprising 20 hours of teaching and supervised practice and 4 hours of individual assessment  
**First class:** Wednesday 4 November 2026  
**Course repository:** [github.com/swapnil1987/2026-research-methods](https://github.com/swapnil1987/2026-research-methods)

## Course description

This course introduces the basic programming skills needed to carry out research projects in economics. Students will learn to use Python, work with economic data, track changes with Git and GitHub, and use coding agents under their own supervision.

## Learning outcomes

By the end of the course, students should be able to:

1. Read a short Python program, predict its output, and explain how its variables change during execution.
2. Write and modify small programs using basic data types, collections, conditions, loops, and functions.
3. Load a dataset, inspect its structure, handle specified data problems, calculate descriptive statistics, and produce a clear figure.
4. Diagnose common programming errors and use small examples, assertions, and economic reasoning to check results.
5. Use Git and GitHub to save meaningful versions, inspect changes, collaborate through a simple branch and pull request, and recover an earlier working version.
6. Give a coding agent a bounded task, inspect the proposed changes, and verify that the result satisfies the specification.
7. Organise a small research project so that another person can reproduce its outputs from the supplied data and instructions.

## Preparation and software

Students will need a laptop, a GitHub account, and access to the common Python environment and coding agent used in class. Setup instructions and a starter project will be provided before the first class. Students should complete the setup check by opening the project and running the supplied example. **IT IS THE RESPONSIBILITY OF A STUDENT TO ENSURE SOFTWARES RUN ON HIS/HER COMPUTER.**

The course will use Python, Jupyter notebooks, pandas, NumPy, and Matplotlib. Short scripts will be introduced alongside notebooks. All students will use a supported common setup, with equivalent access to the agent used for assessed work. Advanced features and paid upgrades will not be needed to complete the core tasks.

## Teaching schedule

### Day 1 Python foundations and a first research project

**Wednesday 4 November 2026 — eight contact hours**

| Block | Hours | Topics and activities |
|---|---:|---|
| Getting a project running | 1 | Files and folders; relative paths; editor, notebook, and script; running code; notebook execution order; a short demonstration of a coding agent. |
| Basic Python | 2 | Variables, numbers, strings, booleans, lists, and indexing; arithmetic and comparisons; tracing short programs; calculating household income and saving. |
| Conditions loops and functions | 2 | Conditional statements; iteration; small functions with inputs and return values; handling zero income and invalid inputs; testing a function on a few households. |
| Reading errors and checking calculations | 1 | Common exceptions and tracebacks; distinguishing a program that crashes from one that gives a wrong answer; hand calculations and small test cases. |
| First steps with Git and GitHub | 1 | Repository, working copy, and remote; inspecting a diff; creating a meaningful commit; pushing a change; keeping source data separate from generated outputs. |
| First look at a dataset | 1 | Reading a CSV with pandas; inspecting rows, columns, and data types; selecting variables; connecting a household-level calculation to the dataset. |
| **Total** | **8** | |

**By the end of the day:** students should be able to run the starter project, explain and modify a small function, inspect a dataset, and save a change in Git.

**Take-home exercise 1 is released at the end of Day 1.**

The schedule for the remaining teaching days will be added closer to their dates.

The complete course contains **20 hours of teaching and supervised practice and 4 hours of individual assessment**.


## Take-home exercise

Take-home submissions contribute to the course grade as set out below. AI use is permitted, and students remain responsible for understanding and checking what they submit. Each exercise is designed to take approximately two to three hours outside the 24 contact hours. Only Exercise 1 is described here; later tasks will be added when they are released.

### Exercise 1 Small programs for household calculations

Released at the end of Day 1, Wednesday 4 November 2026. **Submission deadline: Monday 9 November 2026 at 23:59, Europe/Vilnius time.** Students will complete and test small functions for income, consumption, or saving calculations; explain a short program; inspect the supplied CSV; and save their work on their own assignment branch in the course repository. Tasks will use only material already covered in class.

The submission should include the code, a few hand-checkable examples, a short explanation of one error or correction, and a brief account of any AI assistance. Students should first attempt a short tracing or modification task independently, then use an agent where helpful.

The task sheet and marking rubric will be provided when the exercise is released. Submit by pushing the assignment branch and opening a pull request to `main` in the course repository before the deadline. The instructor will record the latest commit pushed to the pull request by the deadline as the submission version. Students must not merge their own submissions; only the instructor may update `main`.

The repository and pull requests are public. Detailed individual feedback and official marks will be provided privately. The review of Exercise 1 is planned for Tuesday 10 November 2026.

## Assessment and grading

The Python programming and reproducible research component contributes **67% of the final course grade**. The writing component, taught and assessed by another lecturer, contributes **33%**. All weights below are percentages of the whole course.

![Grading: programming and research 67%, writing 33%. Each exercise contributes 10% for the submission and 15% for an individual test; the final practical contributes 17%. Passing requires at least 50/100 overall and 23.5/47 across the independent assessments combined.](docs/figures/grading-overview.png)

[Open the grading figure as a PDF](docs/figures/grading-overview.pdf).

| Component | Weight | Format and criteria |
|---|---:|---|
| Exercise 1 submission | 10% | Individual take-home work submitted through a pull request. AI assistance is permitted. Marks reward correctness, runnable code, appropriate checks, and clear explanations under the published rubric. |
| Exercise 1 individual test | 15% | Supervised multiple-choice questions without AI, assessing understanding of the exercise and the concepts taught. |
| Exercise 2 submission | 10% | Individual take-home work submitted through a pull request. AI assistance is permitted. The task, rubric, and deadline will be announced when it is released. |
| Exercise 2 individual test | 15% | Supervised multiple-choice questions without AI, assessing understanding of the exercise and the concepts taught. |
| Day 3 individual practical | 17% | A supervised task without AI: read and modify a short program, diagnose an error, check a result, and explain the output. |
| Writing component | 33% | Assessed by the other lecturer under the writing component's published requirements. |
| **Total** | **100%** | |

**Marks are additive.** Each exercise contributes up to 25 percentage points: 10 from the submission and 15 from its individual test. For example, full marks on a submission contribute 10 points; a score of 40% on the associated test contributes 6 points. Together, they contribute 16 out of the exercise's 25 points.

Individual tests will use submissions to identify relevant approaches and common difficulties. Questions will follow a common assessment blueprint with comparable difficulty for all students. They may ask students to trace code, predict the effect of changed inputs, diagnose a bug, select a useful check, or interpret a calculation. Tasks will assess material already taught. Dates, durations, permitted reference materials, and sample formats will be announced before each assessment.

**Pass requirements:** at least 50% overall and at least 50% of the marks available across the two individual tests and the Day 3 practical combined. These independent assessments contribute 47 percentage points to the course grade, so the independent-assessment requirement is at least **23.5 out of 47 points in aggregate**. A separate pass in each individual test is not required. These requirements remain subject to the institution's grading rules and confirmation.

AI tools may assist the instructor in checking submissions against the rubric and drafting questions. The instructor reviews the evidence, confirms the marks, and approves the assessment questions and answer keys.

### Grade IDs and feedback

Each student will privately receive a randomly assigned grade ID, separate from their name, official student number, and GitHub username. Grade summaries may be displayed using these IDs. Students must keep their grade ID out of public branches, pull requests, commits, and assignment files.

The mapping between students and grade IDs will be kept privately outside the public repository. Public summaries will contain only grade IDs and component marks, with no links to student submissions. Detailed individual feedback and official marks will be provided privately. These IDs reduce direct identification; they do not guarantee anonymity where public submissions or other information allow a student to be identified.

Unreleased assessment questions, answer keys, and instructor grading records will remain outside the public repository.

## Use of AI

Students may use AI for take-home exercises and designated classroom activities. AI is not permitted in either individual test or the Day 3 individual practical. Generative autocomplete must also be disabled during these independent assessments.

Permitted AI assistance does not reduce a submission's mark. Submissions are assessed against the published rubric; individual tests and the practical assess the student's independent understanding. A low individual-test score does not by itself establish academic misconduct.

For work completed with an agent, students should record the tool used, the task delegated, the substantive changes accepted, and the checks performed. A short task record is sufficient; a complete transcript is not required unless a task sheet explicitly requests it. The quality of a prompt alone does not establish the correctness of the resulting analysis.

Students must be able to explain the submitted code and its economic meaning. They should use only the supplied synthetic or approved public data with external agents. Passwords, access tokens, and confidential research data must not be included in prompts or committed to a repository.

## Project standards

Each completed project should preserve the supplied raw data, use clear names and relative paths, record the required software, and provide concise instructions for reproducing the results. Notebooks must run in order from a fresh kernel; scripts must run without relying on hidden notebook state or files created manually during an earlier session.

Checks should address the actual calculation. Examples include verifying that household identifiers are unique, explaining missing values, checking row counts after a merge, and comparing a computed statistic with a small hand-worked example. A plausible figure is not sufficient evidence that the underlying calculation is correct.

## Materials and scope

The course repository will contain lesson notes, starter code, synthetic data, worked classroom examples, and take-home task sheets as they are prepared. Graded assessment questions and instructor solutions will be distributed separately.

Reference materials include the [Python tutorial](https://docs.python.org/3/tutorial/), [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/), [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html), and [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world). These are references rather than required reading in full.

Advanced Python, object-oriented design, advanced Git operations, machine learning, and dynamic programming methods such as value function iteration are outside the assessed core. The course provides the programming and verification foundations needed to study these topics subsequently.
