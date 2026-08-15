#!/usr/bin/env bash
set -euo pipefail

results_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
(cd "${results_dir}/../../step1/test" && ./run_bl_dgemm.sh) | python "${results_dir}/write_result.py" "${results_dir}/step1_result.py" --variable RUN_STEP1_ST
