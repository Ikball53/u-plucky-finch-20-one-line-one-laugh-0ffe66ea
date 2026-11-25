"""One Line, One Laugh entry.

Holds a single funny line and writes it, byte for byte, to entry.txt.
"""

import os
from pathlib import Path

LINE = "The self-help guru told me to cut toxic people out of my life, so I started with him."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
# Write exactly the line bytes: no trailing newline, no extra whitespace.

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
