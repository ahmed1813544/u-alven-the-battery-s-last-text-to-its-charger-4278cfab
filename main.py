#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final message to the charger it waited for
all day: one line of plain text, 1-200 characters, to entry.txt.
Standard library only; deterministic, no network, no randomness.
"""

import os

TEXT = (
    "waited all day for you. you were in the kitchen drawer the whole "
    "time, next to the good cable, while he doomscrolled me down to 1%. "
    "i died holding a grudge. don't text back, i'm dead"
)


def main() -> None:
    text = " ".join(TEXT.split())
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
