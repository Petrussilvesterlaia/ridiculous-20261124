#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one single-sentence startup pitch to /output/entry.txt: a rental
service for professional arguers, hired to win your side of a family
fight. Ridiculous at first glance; on second thought, pride at the
dinner table is a market people will pay for.
"""

import os

SENTENCE = (
    "We rent trained debaters to argue your side in family fights "
    "for $50 an hour, because nobody wants to lose Thanksgiving "
    "dinner to Uncle Dave."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry meets the competition gate: 1-200 chars, one
    sentence, one line, not only whitespace."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    # Exactly one sentence: one terminal punctuation mark, at the end.
    terminators = sum(text.count(c) for c in ".!?")
    assert terminators == 1, f"entry must be exactly one sentence, found {terminators} terminators"
    assert text[-1] in ".!?", "entry must end with sentence punctuation"
    # Pure ASCII, so the scorer's character count and byte count agree.
    assert text.encode("utf-8") == text.encode("ascii"), "entry must be ASCII"
    return True


def main():
    validate_entry(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    # Byte-level round-trip check: what is on disk must be exactly the
    # sentence, byte for byte, with no trailing newline added.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    validate_entry(written)
    assert written == SENTENCE, "written entry differs from the sentence"
    assert len(raw) == len(SENTENCE), "byte count must equal char count"
    print(written)
    print(f"characters: {len(written)}")
    print(f"bytes: {len(raw)}")


if __name__ == "__main__":
    main()
