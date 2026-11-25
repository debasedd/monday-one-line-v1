#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes the funniest one-line review of my own Monday to
/output/entry.txt — nothing else, no title, no explanation.

The joke treats Monday as an unwanted houseguest: it shows up
uninvited, eats the weekend's leftovers, and leaves its meetings
all over the couch. Specific, short, and about my Monday rather
than Mondays in general.
"""

import os

ENTRY = (
    "My Monday showed up uninvited, ate the weekend's leftovers, "
    "and left its meetings all over my couch."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # The grader must be able to read the entry: world-readable, always.
    os.chmod(path, 0o644)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
