#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Deterministic: the same line every run, 97 characters of UTF-8, one line.
"""

import os

LINE = "So\u2026 floor three again? My logs say you press it 94% of the time. I am not judging. I am logging."

# Gate the line at build time so a future edit can never silently break the
# scorer's rule: 1-200 UTF-8 characters, one line, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip() and "\n" not in LINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
