"""QR code for the poster header.

Reads `qr-url:` (or else `repo:`) from the YAML header of poster.qmd and
writes figures/qr_code.svg. Pass a URL to override:

    python scripts/qr_code.py
    python scripts/qr_code.py https://example.org/project
"""

import re
import sys
from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "qr_code.svg"


def url_from_yaml():
    for qmd in sorted(ROOT.glob("*.qmd")):
        text = qmd.read_text()
        header = text.split("---")[1] if text.startswith("---") else ""
        for key in ("qr-url", "repo"):
            m = re.search(rf'^{key}:\s*["\']?([^"\'\s#]+)', header, re.M)
            if m:
                return m.group(1)
    return None


url = sys.argv[1] if len(sys.argv) > 1 else url_from_yaml()
if not url:
    print("no qr-url: or repo: in the poster's YAML; nothing to do")
    sys.exit(0)
if not url.startswith("http"):
    url = "https://" + url

OUT.parent.mkdir(exist_ok=True)
segno.make(url, error="m").save(OUT, scale=10, border=0)
print(f"wrote {OUT} for {url}")
