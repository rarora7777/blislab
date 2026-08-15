#!/usr/bin/env python3
"""Write BLISlab benchmark output from standard input as a NumPy module."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np


def read_result() -> np.ndarray:
    """Read the numeric benchmark rows emitted by ``run_bl_dgemm.sh``."""
    rows: list[np.ndarray] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped or stripped.startswith(("%", "result=", "];")):
            continue
        row = np.fromstring(stripped, sep=" ")
        if row.size:
            rows.append(row)

    if not rows:
        raise ValueError("No benchmark rows were received on standard input")
    if any(row.size != rows[0].size for row in rows):
        raise ValueError("Benchmark output contains rows with different widths")
    return np.vstack(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Python module to create")
    parser.add_argument("--variable", required=True, help="NumPy array variable name")
    args = parser.parse_args()

    result = read_result()
    lines = [
        '"""Generated BLISlab benchmark results."""',
        "",
        "import numpy as np",
        "",
        f"{args.variable} = np.array([",
    ]
    lines.extend(f"    {row.tolist()}," for row in result)
    lines.extend(("], dtype=float)", f"result = {args.variable}", ""))
    args.output.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
