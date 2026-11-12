"""Shim: load the matplotlib style that ships with the talk extension.

Figure scripts do `from talk_style import apply_style, SERIES, FULL`. The real
module is _extensions/<name>/talk_style.py, so updating or switching the theme
(`quarto add ...`) updates figure styling too. Set TALK_THEME to pick a theme
when more than one is installed (default: talk).
"""

import importlib.util
import os
from pathlib import Path

_theme = os.environ.get("TALK_THEME", "talk")


def _find():
    for parent in Path(__file__).resolve().parents:
        ext = parent / "_extensions"
        if ext.is_dir():
            hits = sorted(ext.glob(f"**/{_theme}/talk_style.py"))
            if hits:
                return hits[0]
    raise FileNotFoundError(f"No _extensions/**/{_theme}/talk_style.py above {__file__}")


_spec = importlib.util.spec_from_file_location("_talk_style", _find())
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

globals().update({k: v for k, v in vars(_mod).items() if not k.startswith("_")})
