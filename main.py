#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's dying one-liner to entry.txt under $MAKEFUN_OUTPUT_DIR
(default /output). Deterministic, no network, no randomness.

Gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 199 characters,
not only white space, a single line.
"""

import os
import sys

# The phone's last words at 1 percent: it warned the owner twice, was
# dismissed as dramatic, and gets the last word. The third beat echoes
# the accusation ("being dramatic") so the punchline answers it directly.
LINE = "I warned you at 20 percent. I warned you at 10. You said I was being dramatic. Who's dramatic now?"

MAX_CHARS = 199


def validate(line: str) -> None:
    """Enforce every gate rule from RULES.txt before writing."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    # Must round-trip as UTF-8.
    line.encode("utf-8")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
