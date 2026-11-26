#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes a single original fortune cookie message for a software
engineer to /output/entry.txt. The output is deterministic: the
same line, byte for byte, on every run.
"""

import os

FORTUNE = "You will deploy on Friday and nothing will break. This cookie is lying, obviously."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")
    print(FORTUNE)


if __name__ == "__main__":
    main()
