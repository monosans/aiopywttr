from __future__ import annotations

from typing import Dict

from mypyc.build import mypycify
from typing_extensions import Any


def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs["ext_modules"] = mypycify([
        "aiopywttr/__init__.py",
        "aiopywttr/_get_weather.py",
        "aiopywttr/_http.py",
        "aiopywttr/_wttr.py",
    ])
