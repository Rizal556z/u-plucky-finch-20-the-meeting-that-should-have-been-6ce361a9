#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one joke, one line, at most 200 characters, to entry.txt.
Pure Python standard library only.
"""

import os

ENTRY = (
    "We held a 45-minute meeting that could have been an email, "
    "then scheduled a follow-up to discuss why the email never arrived."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: single line, 1-200 chars, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
