"""news-image-20261119 entry: write the day's news image to /output/entry.png.

The image is held in the repository as entry.png (drawn in code with PIL at
build time); this program copies it byte-for-byte to the output directory.
Standard library only, no network, deterministic: the same bytes every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    if len(sys.argv) > 1:
        out = Path(sys.argv[1])
    else:
        out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out)


if __name__ == "__main__":
    main()
