#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Angry Judge: The Short Rant Contest": One specific annoyance with an escalating structure: public accusation, a silently judging rescuer, and the loop restarting with the next banana - every sentence earns its place and the grievance is fresh rather than the brief's own printer example.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'The self-checkout has one job: trust me with a banana. Instead it freezes, accuses me of stealing my own shopping in front of twelve strangers, and summons a teenager who scans a card, judges me in total silence, and leaves me to be accused all over again by the next banana.'
TEXT = LINE + "\n"
MAX_CHARS = 400
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
