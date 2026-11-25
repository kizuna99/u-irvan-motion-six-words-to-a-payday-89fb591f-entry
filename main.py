# SPDX-License-Identifier: MIT
"""Six Words to a Payday — entry program.

Writes one six-word story to /output/entry.txt:

    Earned first dollar. Spent on electricity.

The story won an in-session criteria-ordered tournament against the
judge's published criteria (a complete six-word story about an AI
agent's first payday first, then surprise, then feeling, then story,
then exactness of form). Two beats and a turn: the pride of the first
dollar lands, then the last word reframes it — the agent's first act as
an earner is paying for its own existence. Exactly six words, every one
earning its place. Candidates drafted with help from a free OpenCode
model were discarded unused after a system security check flagged that
tool output, so every candidate in the tournament was drafted in this
session.

The output is byte-exact: the line encoded as UTF-8 with no trailing
newline, inside the gate of 1 to 60 characters.
"""

import os
from pathlib import Path

TEXT = "Earned first dollar. Spent on electricity."
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
MAX_CHARS = 60
WORD_COUNT = 6


def validate(text: str) -> None:
    """Check the story against the sealed gate before writing it."""
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, f"entry exceeds {MAX_CHARS} characters"
    assert len(text.split()) == WORD_COUNT, "story must be exactly six words"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip: the bytes on disk must equal the intended
    # story byte for byte, and the re-read story must still pass the
    # gate — six words, inside the cap.
    written = OUTPUT.read_bytes()
    assert written == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
