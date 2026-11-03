#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
environment_name="${RESEARCH_METHODS_ENV:-research-methods}"

if command -v conda >/dev/null 2>&1; then
  conda_command="$(command -v conda)"
elif [[ -x "${HOME}/miniconda3/bin/conda" ]]; then
  conda_command="${HOME}/miniconda3/bin/conda"
else
  echo "Miniconda was not found. Put conda on PATH or install it under ~/miniconda3." >&2
  exit 1
fi

exec "${conda_command}" run --no-capture-output \
  --name "${environment_name}" \
  quarto render "${repo_root}/slides" "$@"
