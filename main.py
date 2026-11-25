#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Angry Judge: The Short Rant Contest".
The rant targets one specific annoyance and escalates in stages:
the self-checkout freezes, publicly accuses the shopper of stealing
their own shopping, summons a silently judging teenager, and then
the whole loop restarts with the next banana.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = (
    "The self-checkout has one job: trust me with a banana. Instead it "
    "freezes, accuses me of stealing my own shopping in front of twelve "
    "strangers, and summons a teenager who scans a card, judges me in "
    "total silence, and leaves me to be accused all over again by the "
    "next banana."
)
TEXT = LINE + "\n"
MAX_CHARS = 400
ENTRY_FILENAME = "entry.txt"


def validate(text: str) -> None:
    """Check the entry is a single non-empty line within the length cap."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def output_path() -> Path:
    """Resolve the entry.txt target from MAKEFUN_OUTPUT_DIR."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    validate(TEXT)
    target = output_path()
    payload = TEXT.encode("utf-8")
    target.write_bytes(payload)
    if target.read_bytes() != payload:
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
