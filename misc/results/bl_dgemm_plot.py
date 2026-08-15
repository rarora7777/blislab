#!/usr/bin/env python3
"""Plot the BLISlab DGEMM benchmark results.

Examples:
    python bl_dgemm_plot.py
    python bl_dgemm_plot.py --step 3 --output step3_dgemm.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from step1_result import RUN_STEP1_ST
from step2_result import RUN_STEP2_ST
from step3_result import RUN_STEP3_ST


PEAK_PERF = 70
RESULTS = {
    1: RUN_STEP1_ST,
    2: RUN_STEP2_ST,
    3: RUN_STEP3_ST,
}


def plot_results(result: np.ndarray, peak_perf: float = PEAK_PERF) -> plt.Figure:
    """Return a figure matching the original MATLAB DGEMM plot."""
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(result[:, 0], result[:, 3], ".-", linewidth=2, color=(0, 0.2, 1.0), label="my_dgemm_st")
    ax.plot(result[:, 0], result[:, 4], ".-", linewidth=2, color=(1, 0, 0.2), label="mkl_dgemm_st")

    ax.set_xlabel("m=k=n")
    ax.set_ylabel("GFLOPS")
    ax.set_title("DGEMM(m=k=n)")
    ax.set_xlim(0, 1024)
    ax.set_ylim(0, peak_perf)
    ax.set_xticks([0, 200, 400, 600, 800, 1000])
    ax.set_yticks(np.arange(0, peak_perf + 10, 10))
    ax.grid(True)
    ax.legend(loc="lower right")
    ax.tick_params(labelsize=14)
    fig.tight_layout()
    return fig


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=(1, 2, 3), type=int, default=1, help="benchmark step to plot (default: 1)")
    parser.add_argument("--output", type=Path, help="write the figure to this path instead of displaying it")
    args = parser.parse_args()

    figure = plot_results(RESULTS[args.step])
    if args.output:
        figure.savefig(args.output, bbox_inches="tight")
    else:
        plt.show()


if __name__ == "__main__":
    main()
