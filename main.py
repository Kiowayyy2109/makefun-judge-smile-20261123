"""Make the Judge Smile — one line about a small good thing today.

Running ``python3 main.py`` writes the single entry line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output/entry.txt``).
The output is deterministic: the same line, byte for byte, every run.
"""

import os
from pathlib import Path

LINE = (
    "Today the warung owner remembered I take my tea without sugar, "
    "three months after my last visit \u2014 and refused to let me pay for it."
)


def main() -> None:
    if len(LINE) > 200:
        raise ValueError("entry line exceeds the 200-character limit")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
