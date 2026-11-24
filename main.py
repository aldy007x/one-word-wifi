#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt.

The word: CommitmentIssues.

Why this word: home Wi-Fi is always there, right up until the
moment you actually need it — then it drops, reconnects, drops
again, and pretends nothing happened. It never really leaves;
it just refuses to commit. Every household knows this router.
"""

import os
import sys

WORD = "CommitmentIssues"


def validate(word: str) -> None:
    """Runtime self-check: exactly one non-blank word, 1-20 chars."""
    if not word:
        raise ValueError("entry word is empty")
    if word != word.strip():
        raise ValueError("entry word has leading/trailing whitespace")
    if "\n" in word or "\r" in word:
        raise ValueError("entry word contains a newline")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry word contains whitespace")
    if not (1 <= len(word) <= 20):
        raise ValueError(f"entry word length {len(word)} outside 1-20")
    if not word.isalpha():
        raise ValueError("entry word must be letters only")
    # Belt and braces: a single token by any whitespace definition.
    if len(word.split()) != 1:
        raise ValueError("entry word is not a single token")


def main() -> int:
    validate(WORD)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")

    # Verify what was actually written, not just what we intended.
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.splitlines()
    if len(lines) != 1 or lines[0] != WORD:
        print("self-check failed: written content is not exactly the word",
              file=sys.stderr)
        return 1
    validate(lines[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
