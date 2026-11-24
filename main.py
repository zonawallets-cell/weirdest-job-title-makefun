"""Weirdest Job Title: Blind Judge Showdown.

Writes exactly one job title (at most 60 characters) -- the weirdest one
we could think of -- to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same title,
byte for byte, on every run.
"""

import os

LINE = "Senior Lighthouse Keeper (Inland, No Sea)"

MAX_CHARS = 60


def validate(text):
    """Gate: 1-60 chars, UTF-8, a single line, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("title must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("title exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("title must not contain a newline")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    text = validate(LINE.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back what was written: the file on disk must be exactly the
    # validated title plus its trailing newline, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        raise SystemExit("entry.txt on disk differs from the validated title")
    print(text)


if __name__ == "__main__":
    main()
