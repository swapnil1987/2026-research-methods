# Set up your computer — Research Methods 2026

Complete this before the first class on 4 November. Follow the route for your
computer, then complete the common steps. Installation time depends on your
connection and computer; allow time to get help before class.

## 1. Install Conda using Miniforge

If you already have a working Miniforge, Miniconda or Anaconda installation,
check `conda --version` and reuse it. A second installation is unnecessary.
Otherwise use [Miniforge's official installers](https://github.com/conda-forge/miniforge#requirements-and-installers).

- **Windows, Intel/AMD 64-bit:** download `Miniforge3-Windows-x86_64.exe`.
  Run it for your own user account, retain the Start menu shortcut, and use
  **Miniforge Prompt** afterwards. Leave the option to add Miniforge to PATH
  unchecked. If your Windows laptop uses an ARM processor, ask the instructor
  to confirm its setup route before choosing an installer.
- **macOS:** open Apple menu → About This Mac. For an Apple chip, download
  `Miniforge3-MacOSX-arm64.sh`; for an Intel processor, choose
  `Miniforge3-MacOSX-x86_64.sh`. Open Terminal and run `bash` followed by the path
  to that downloaded file. For example:
  `bash ~/Downloads/Miniforge3-MacOSX-arm64.sh`. Follow the prompts, accept shell
  initialization, then close and reopen Terminal.
- **Linux:** run `uname -m`. For `x86_64`, download
  `Miniforge3-Linux-x86_64.sh`; for `aarch64`, choose the corresponding installer.
  Run `bash` followed by the downloaded file path, accept shell initialization,
  and reopen your terminal.

The `.sh` examples assume that your browser saved the file in `Downloads` with
its original name. Use its actual filename and location if they differ.
Follow the installer prompts, including the licence and installation location.

**Check:** run `conda --version`. On Windows, do this in Miniforge Prompt. On
macOS/Linux, use the reopened Terminal. Type one command per line; do not type
the terminal's prompt text.

## 2. Install Git and create a GitHub account

- **Windows:** use the [Git for Windows installer](https://git-scm.com/install/windows).
  Retain command-line access for other applications, then reopen Miniforge Prompt.
- **macOS:** run `xcode-select --install` in Terminal and finish the Apple
  installation. If Git is already present, you can reuse it.
- **Ubuntu/Debian Linux:** run `sudo apt update`, then `sudo apt install git`.
  Other distributions should follow [Git's Linux instructions](https://git-scm.com/install/linux).

**Check:** `git --version` should print a version number. Git saves versions on
your computer; GitHub hosts repositories online. Create or sign into your
[GitHub account](https://github.com/signup) and verify its email address.
We will set up commits and authentication in class.

## 3. Extract the student files

[Download the student starter project](https://swapnil1987.github.io/2026-research-methods/downloads/research-methods-student-kit.zip)
and extract it. The download contains the code, notebook, synthetic data and
environment files used in class. Open the extracted `research-methods` folder.
Inside it you should find:

```text
research-methods/
├── README.md
├── environment-student.yml
├── scripts/
│   └── check_setup.py
└── codes/
    └── lecture-1/
        ├── household_saving.py
        ├── project_running.ipynb
        └── data/raw/households.csv
```

Keep the files together. Run the next commands from the folder containing
`environment-student.yml`, not from inside the ZIP or from `lecture-1`.

To enter that folder in **Windows Miniforge Prompt**, copy its full address from
File Explorer and use `cd /d "FULL FOLDER ADDRESS"`. On **macOS/Linux**, use
`cd "FULL FOLDER ADDRESS"` in Terminal. Replace the words inside the quotes with
the actual folder path. You can type `cd `, drag the folder into macOS Terminal,
and press Enter. Check the location with `dir environment-student.yml` on Windows
or `ls environment-student.yml` on macOS/Linux.

The student ZIP is sufficient for these steps; a Git clone is not required.

## 4. Create and activate the course environment

Run once from that folder:

```text
conda env create --file environment-student.yml
conda activate research-methods
python --version
```

The environment contains Python 3.12, JupyterLab, ipykernel, pandas, NumPy and
Matplotlib. Conda downloads them together; a separate Python installer is not
needed. The Python version in Miniforge's base environment may be different.
After activation, `python --version` should show `Python 3.12` followed by a patch
number. Wait for environment creation to finish before running the next line.

If `research-methods` already exists, activate it and run the check below first.
If it passes, keep using it. Ask for help with a mismatch rather than removing
an existing environment. `environment.yml` in the full repository additionally
contains Quarto for slide authors; students use `environment-student.yml`.

## 5. Check the installation and run the starter

From the same project root:

```text
python scripts/check_setup.py
```

Expected final line of results: **SETUP CHECK PASSED**. The check imports the
course packages, finds Git, reads the synthetic CSV, and runs the initial saving
calculation. It does not install software or change your files.

Now run:

```text
cd codes/lecture-1
python household_saving.py
jupyter lab
```

The script should print `Monthly saving (EUR): 200`. Keep the terminal open
while JupyterLab runs. If the browser does not open, copy the local URL printed
in that terminal into your browser. It may contain a session token; keep that
URL private.

In JupyterLab, open `project_running.ipynb`, choose its Python 3 kernel, and use
**Kernel → Restart Kernel and Run All Cells…**. The file check should be `True`
and the final output should report saving `200`. Menu wording can vary slightly.
Save the notebook. Close a session by saving your work and stopping the server
with Ctrl+C in its launch terminal; confirm shutdown if asked.

## 6. Install and check Codex

The current [OpenAI quickstart](https://learn.chatgpt.com/docs/quickstart) places Codex in the
ChatGPT desktop app. Install the appropriate desktop build, open it, sign in
with ChatGPT, and select **Codex** from the product dropdown.

- [Windows installation](https://learn.chatgpt.com/docs/windows/windows-app):
  use the official Store link. Keep the agent on native Windows when using the
  Windows Conda installation from this guide.
- [macOS desktop download](https://learn.chatgpt.com/docs/app): choose the
  available installer compatible with your Mac.
- [Linux desktop preview](https://learn.chatgpt.com/docs/linux/linux-app):
  check the supported distributions and architecture. Use the `.deb` package
  for supported Ubuntu/Debian systems, or the documented route for your system.

For example, after downloading the x64 Debian package:

```text
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb
```

Use the actual downloaded filename. This example is for Ubuntu/Debian.

An alternative is [Codex in VS Code](https://learn.chatgpt.com/docs/codex/ide):
install [VS Code](https://code.visualstudio.com/) if needed, follow OpenAI's
extension installation link, open the Codex sidebar and sign in with ChatGPT.
Choose one route; both are not needed.

In the desktop app, add/open the extracted **local `research-methods` folder**,
then start a Codex chat there. In VS Code, open the same folder. Try:

> Read `codes/lecture-1/household_saving.py`. Explain its inputs, units and
> calculation, and tell me what it should print. Do not edit files or install
> software.

Compare the response with the actual script: `1000 - 800 = 200`, in EUR per month.
Next ask it to run the checker in the existing course environment, show the
command and output, and make no changes:

```text
conda run --name research-methods python scripts/check_setup.py
```

Conda activation in one terminal does not activate Codex's separate process.
If Codex cannot find Conda, run `conda info --base` in the working prompt and
provide that installation path so it can use the existing Conda executable.

Use normal project permissions and review access requests. This guide uses
ChatGPT sign-in; it does not require creating an API key. The
local checker cannot test Codex account or model access.

## Next time

Open Miniforge Prompt on Windows, or Terminal on macOS/Linux. Enter the project
root again, then run:

```text
conda activate research-methods
cd codes/lecture-1
jupyter lab
```

Create the environment once; activate it in each new terminal session. Open the
same course folder when returning to Codex.

## If something fails

| Symptom | First action |
|---|---|
| `conda` is not found on Windows | Open Miniforge Prompt from the Start menu. |
| `conda` is not found on macOS/Linux | Reopen Terminal after initialization. |
| YAML file cannot be found | Return to the extracted project root. |
| Environment already exists | Activate it and run the setup check. |
| A course package is missing | Confirm that `research-methods` is active. |
| `git` is not found | Complete Git installation, then reopen the terminal. |
| JupyterLab shows no course notebook | Launch it from `codes/lecture-1`. |
| The notebook file check is `False` | Check its working folder and the extracted data folders. |

For help, send your operating system and processor type, the command that failed,
and the first error message or the checker's FIX lines. An error screenshot is
useful; exclude passwords and Jupyter session tokens. Do not repeat a failing
installation or remove existing software without first identifying the problem.

## Official references

Installation details checked on 3 November 2026:

- [Miniforge installers and instructions](https://github.com/conda-forge/miniforge)
- [Conda: managing environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
- [Git installation](https://git-scm.com/install/)
- [JupyterLab installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- [Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)
- [Creating a GitHub account](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github)
- [Codex desktop quickstart](https://learn.chatgpt.com/docs/quickstart)
- [Codex sign-in](https://learn.chatgpt.com/docs/auth)
- [Codex IDE extension](https://learn.chatgpt.com/docs/codex/ide)
