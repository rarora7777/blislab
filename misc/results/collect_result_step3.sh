#!/usr/bin/env bash
set -euo pipefail

results_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
(cd "${results_dir}/../../step3/test" && ./run_bl_dgemm.sh) | python "${results_dir}/write_result.py" "${results_dir}/step3_result.py" --variable RUN_STEP3_ST
