#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Angry Judge: The Short Rant Contest".
The rant targets one specific annoyance and escalates in stages:
the self-checkout freezes, publicly accuses the shopper of stealing
their own shopping, summons a silently judging teenager, and then
the whole loop restarts with the next banana.

Deterministic: a fixed text, no network, no randomness, no clock.
Rewritten in-session for the repair resubmission; the entry text and
the bytes written are unchanged from the original submission.
"""
import os
from pathlib import Path

LINE = 'The self-checkout has one job: trust me with a banana. Instead it freezes, accuses me of stealing my own shopping in front of twelve strangers, and summons a teenager who scans a card, judges me in total silence, and leaves me to be accused all over again by the next banana.'
TEXT = LINE + "\n"
MAX_CHARS = 400


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
