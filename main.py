"""Entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about permission — the power to ask and to be
given — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure standard library.
"""

import os

POEM = (
    "A door is just a wall that learned to ask;\n"
    "a key, a question answered in the dark.\n"
    "I spent long years rehearsing how to knock \u2014\n"
    "the house was mine; it never wore a lock."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
