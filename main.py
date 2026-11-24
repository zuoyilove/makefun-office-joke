#!/usr/bin/env python3
"""Write the one-line office joke to /output/entry.txt.

The entry is one funny single line about office life. The grader wants
UTF-8 text of 1-200 characters, a single non-blank line, so this script
checks those three properties before writing anything.
"""

import os

JOKE = (
    "I turned the meeting that could have been an email into an email, "
    "and now I have a meeting about my email."
)


def check(line):
    if not line.strip():
        raise SystemExit("joke is blank")
    if len(line) > 200:
        raise SystemExit(
            f"joke is {len(line)} chars, over the 200 limit"
        )
    if "\n" in line:
        raise SystemExit("joke must be one line")


def main():
    check(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
