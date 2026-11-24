#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — one fixed line, written to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
The line is a fixed string in the source.
"""

import os
import tempfile

LINE = "I waited all morning for a library I invented to finish installing itself."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        # World-readable so the grader can read it (see past lesson:
        # mkstemp defaults to 0600, which got an entry rejected).
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
