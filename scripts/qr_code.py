"""QR code for the talk's repository, used by ::: {.qr} ::: blocks.

Reads `repo:` from the YAML header of each deck (*.qmd) in the folder above
this script and writes figures/qr-repo.svg. Pass a URL to override:

    python scripts/qr_code.py                       # from the deck's repo:
    python scripts/qr_code.py github.com/org/repo   # explicit
"""

import re
import sys
from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "qr-repo.svg"


def repo_from_decks():
    for qmd in sorted(ROOT.glob("*.qmd")):
        header = qmd.read_text().split("---")[1] if qmd.read_text().startswith("---") else ""
        m = re.search(r'^repo:\s*["\']?([^"\'\s#]+)', header, re.M)
        if m:
            return m.group(1)
    return None


repo = sys.argv[1] if len(sys.argv) > 1 else repo_from_decks()
if not repo:
    print("no repo: in any deck's YAML; nothing to do")
    sys.exit(0)
url = repo if repo.startswith("http") else "https://" + repo

OUT.parent.mkdir(exist_ok=True)
segno.make(url, error="m").save(OUT, scale=10, border=2, dark="#17212B", light="#FFFFFF")
print(f"wrote {OUT} for {url}")
