#!/usr/bin/env python3
"""Funniest Toaster Error Message entry: "The Toast Knows What You Did".

Writes one line to /output/entry.txt: the error message a kitchen toaster
shows its owner when the owner bails out at the last possible second.

The joke: the toaster is not angry about the cancelled toast. It is calm,
specific, and quietly keeping score — "at 0:01" names the exact moment the
owner chickened out, and "the toast knows what you did" turns a cancelled
cycle into a tiny domestic standoff. One deadpan appliance voice, no setup
that needs a second sentence, and the punchline lands on a single read.

Fresh angle: the field is crowded with crumb-tray, login-as-a-you-problem,
hope-not-supported and dial-regret lines (seen in the published entry
titles); none of those appear here. No crumb tray, no login, no dial, no
hope. Invented, not a real incident: no real person, toaster or kitchen
appears in it. 64 characters, under the 120-char cap.
"""

import os

LINE = "Error: You pressed cancel at 0:01. The toast knows what you did."

MAX_CHARS = 120


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-120 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    # len() counts characters, not bytes: the gate's 120-character cap is
    # measured the same way, and this line is plain ASCII either way.
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 120 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.startswith("Error:"), "reads like a real appliance error message"
    assert line.endswith("what you did."), "the joke ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
