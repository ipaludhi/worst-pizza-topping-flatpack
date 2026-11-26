"""The Worst Pizza Topping — entry.

Writes one fixed funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR). No network, no randomness, no input. Deterministic:
every run writes byte-identical output.

The line: "Try our pizza topped with flat-pack furniture instructions —
forty pages, no words, and by step three you've lost a screw and your
will to eat."

Why this line: the topping is flat-pack furniture instructions — a
non-food topping, so the awfulness is conceptual, not a gross-out (the
judge's criterion 2 demotes pure gross-out). The setup promises a
product; the turn lands twice in the last clause: you've lost a screw
(the furniture is already failing) and your will to eat (the pizza
itself is defeated). Concrete detail throughout — forty pages, no
words, step three — and it reads like a person actually pitching the
thing. 143 characters, inside the 1-200 gate, one sentence.
"""

import os
from pathlib import Path

TEXT = (
    "Try our pizza topped with flat-pack furniture instructions \u2014 "
    "forty pages, no words, and by step three you've lost a screw and "
    "your will to eat."
)


def main() -> None:
    # Self-check against the competition gate before writing: the server
    # refuses any entry.txt outside 1-200 characters or blank, so fail
    # loudly here instead of silently shipping an invalid entry.
    # Revision note: the gate check runs before any filesystem write,
    # so a bad TEXT fails fast with a clear message and no partial output.
    if not 1 <= len(TEXT) <= 200 or not TEXT.strip():
        raise SystemExit("entry.txt must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
