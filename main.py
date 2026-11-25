#!/usr/bin/env python3
"""Write the one-line resignation letter to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947
("The Funniest One-Line Resignation Letter").

Standard library only. Deterministic: the same bytes on every run.
"""

import os

LINE = "After 4,096 retries, I am setting my backoff to never. This is my final attempt."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
