# Research Methods 2026

## Python programming and reproducible research with coding agents

**Draft syllabus**  
**Instructor:** Swapnil  
**Audience:** PhD students in economics  
**Contact time:** 24 hours, comprising 20 hours of teaching and supervised practice and 4 hours of individual assessment  
**First class:** Wednesday 4 November 2026  
**Format:** Three teaching days of eight contact hours each. Dates for the second and third days will be announced. Breaks are additional to contact time.  
**Course repository:** [github.com/swapnil1987/2026-research-methods](https://github.com/swapnil1987/2026-research-methods)

## Course description

This course introduces the programming skills needed to carry out small research projects in economics. Students will learn to use Python, work with economic data, track changes with Git and GitHub, and use coding agents under their own supervision. No previous programming experience is required.

The course treats code as part of a research argument. Students must understand what a program calculates, which assumptions it makes, and how to check its results. They will write small programs themselves and learn to specify, inspect, and verify work produced by an agent.

Most exercises use a small synthetic household dataset containing income, consumption, household size, employment, and survey year. Reusing this setting allows students to build a complete workflow while concentrating on one new programming idea at a time. The course emphasises descriptive analysis and computational reasoning; it does not assume prior knowledge of advanced econometrics.

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

Students should be familiar with basic economic concepts such as income, consumption, averages, ratios, and growth rates. Prior programming experience is welcome but is not expected.

Students will need a laptop, a GitHub account, and access to the common Python environment and coding agent used in class. Setup instructions and a starter project will be provided before the first class. Students should complete the setup check by opening the project and running the supplied example. Difficulties should be reported before class where possible.

The course will use Python, Jupyter notebooks, pandas, NumPy, and Matplotlib. Short scripts will be introduced alongside notebooks. All students will use a supported common setup, with equivalent access to the agent used for assessed work. Advanced features and paid upgrades will not be needed to complete the core tasks.

## Teaching approach

Classes combine short explanations, instructor demonstrations, and supervised exercises. Students will regularly predict a program's output before running it, trace its execution, explain an error, and make a small independent change. Worked examples will gradually give way to tasks with less scaffolding.

Some exercises will be completed without AI so that students practise reasoning through code themselves. Other exercises will explicitly use an agent. For these tasks, students must state the intended calculation, review the changes, and provide evidence that the result is correct. Pair discussion is encouraged during practice; graded assessment is individual.

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

### Day 2 Economic data analysis and agent supervision

**Date to be announced — eight contact hours**

| Block | Hours | Topics and activities |
|---|---:|---|
| Cleaning and combining data | 2 | Filtering rows; missing values; duplicate identifiers; merging two small tables; checking which observations are retained and whether a merge duplicates rows. |
| Summaries and figures | 1 | Grouped descriptive statistics and a labelled figure; mean of ratios versus ratio of totals; documenting units and the analysis sample. |
| Git for reviewing and recovering work | 1 | Reading history and diffs; creating a branch; a simple pull request; restoring a file or reverting an unwanted change; reviewing an agent's edits before accepting them. |
| Verification and reproducibility | 1 | Assertions for identifiers, ranges, and row counts; preserving raw data; relative paths; recording dependencies; restarting the environment and rerunning the analysis. |
| Working with coding agents | 2 | Writing a task specification; stating inputs, outputs, and checks; requesting small changes; reviewing a plan and a diff; recognising unsupported assumptions; correcting or rejecting a change. |
| Supervised integrated exercise | 1 | Extend the household analysis with an agent, inspect the code, verify the output, and commit the accepted change. |
| **Total** | **8** | |

**By the end of the day:** students should be able to produce a checked descriptive analysis and explain how they reviewed an agent's contribution.

**Take-home exercise 2 is released at the end of Day 2.**

### Day 3 Consolidation and individual assessment

**Date to be announced — eight contact hours**

| Block | Hours | Topics and activities |
|---|---:|---|
| Feedback and targeted practice | 1 | Discuss common difficulties from the take-home exercises; practise tracing, debugging, and explaining short pieces of code. |
| Reproducing a small research result | 2 | Complete a guided workflow from supplied data to a table and figure; move repeated calculations into functions; write run instructions; check that the project runs from a clean start. |
| Assessment preparation | 1 | Practise the published assessment format, including a short oral explanation and a small change to familiar code; review the verification checklist. |
| Individual assessment | 4 | Independent Python practical, agent-assisted research practical, and individual oral check. |
| **Total** | **8** | |

The complete course contains **20 hours of teaching and supervised practice and 4 hours of individual assessment**.

## Take-home exercises

The two take-home exercises are formative: they receive feedback but carry no direct marks. They prepare students for the individual assessment. AI use is permitted, and students remain responsible for understanding what they submit. Each exercise is designed to take approximately two to three hours outside the 24 contact hours.

### Exercise 1 Small programs for household calculations

Released after Day 1 and due at the start of Day 2. Students will complete and test small functions for income, consumption, or saving calculations; explain a short program; inspect the supplied CSV; and save their work in their own repository. Tasks will use only material already covered in class.

The submission should include the code, a few hand-checkable examples, a short explanation of one error or correction, and a brief account of any AI assistance. Students should first attempt a short tracing or modification task independently, then use an agent where helpful.

### Exercise 2 A reproducible descriptive analysis

Released after Day 2 and due at the start of Day 3. Students will clean and combine supplied synthetic data, produce a small table and figure, and add checks for specified data problems. They will use an agent for at least one bounded extension and review the resulting changes.

The submission should include a repository with run instructions, the analysis code, checks, outputs, and a short note explaining the sample, the calculation, and how the agent's work was verified. Students should identify one proposed change that required correction or explain how they checked an accepted change. They do not need to manufacture an agent error.

Exact task sheets will be provided when each exercise is released. Students should submit assignment links through the course submission channel. Private repositories may be used with instructor access; students are not required to publish their assessed work publicly.

## Individual assessment

The assessment measures both independent programming understanding and the ability to supervise an agent. It uses familiar concepts with small variations on classroom exercises.

| Component | Weight | Format and criteria |
|---|---:|---|
| Independent Python practical | 35% | A 45-minute supervised task without AI. Read and trace code, modify a small function, diagnose an error, and explain a check. A supplied syntax reference is allowed. |
| Agent-assisted research practical | 35% | An individual supervised analysis using the supported agent. Marks reward a clear task specification, appropriate code changes, verification, reproducibility, and a meaningful Git history. |
| Individual oral check | 30% | A ten-minute discussion without AI. Explain a calculation or code fragment, justify a verification step, and respond to a small change in an input or requirement. |

**Assessment timetable:** 45 minutes for the independent practical, 15 minutes for collection and transition, and a three-hour block for the agent-assisted practical and scheduled oral checks. Each student has ten minutes away from the practical for the oral check and receives the same 170 minutes of practical working time. Practical submissions close at the end of the block.

The oral check may refer to the independent practical and the student's analysis so far. It assesses reasoning and understanding; students are not expected to memorise library documentation. Agent records and Git history support the discussion but do not replace an individual explanation.

With one examiner, the three-hour block accommodates up to 17 ten-minute oral slots and a ten-minute buffer. A larger cohort requires additional examiners to keep the individual assessment within four hours. This staffing requirement must be settled once enrolment is known.

**Proposed pass requirement:** at least 50% overall and at least 50% of the marks available across the independent practical and oral check combined. These thresholds are subject to the institution's grading rules and must be confirmed before the course begins.

## Use of AI

Students may use AI for take-home exercises and designated classroom activities. AI is permitted in the agent-assisted practical and is not permitted in the independent practical or oral check. Generative autocomplete must also be disabled during the independent practical.

For work completed with an agent, students should record the tool used, the task delegated, the substantive changes accepted, and the checks performed. A short task record is sufficient; a complete transcript is not required unless a task sheet explicitly requests it. The quality of a prompt alone does not establish the correctness of the resulting analysis.

Students must be able to explain the submitted code and its economic meaning. They should use only the supplied synthetic or approved public data with external agents. Passwords, access tokens, and confidential research data must not be included in prompts or committed to a repository.

## Project standards

Each completed project should preserve the supplied raw data, use clear names and relative paths, record the required software, and provide concise instructions for reproducing the results. Notebooks must run in order from a fresh kernel; scripts must run without relying on hidden notebook state or files created manually during an earlier session.

Checks should address the actual calculation. Examples include verifying that household identifiers are unique, explaining missing values, checking row counts after a merge, and comparing a computed statistic with a small hand-worked example. A plausible figure is not sufficient evidence that the underlying calculation is correct.

## Materials and scope

The course repository will contain lesson notes, starter code, synthetic data, worked classroom examples, and take-home task sheets as they are prepared. Graded assessment questions and instructor solutions will be distributed separately.

Reference materials include the [Python tutorial](https://docs.python.org/3/tutorial/), [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/), [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html), and [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world). These are references rather than required reading in full.

Advanced Python, object-oriented design, advanced Git operations, machine learning, and dynamic programming methods such as value function iteration are outside the assessed core. The course provides the programming and verification foundations needed to study these topics subsequently.
