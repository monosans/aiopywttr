from __future__ import annotations

import keyword
import re

import pytest
from aiohttp import ClientSession, ClientTimeout

import aiopywttr


@pytest.mark.parametrize("language", aiopywttr.Language)
def test_language_value(language: aiopywttr.Language) -> None:
    assert language._name_ == language._value_.replace("-", "_").upper()


@pytest.mark.parametrize("language", aiopywttr.Language)
def test_language_model(language: aiopywttr.Language) -> None:
    name = language._name_.lower()
    # A keyword can't name a module, so `is` gets a trailing underscore.
    module = getattr(aiopywttr.models, f"{name}_" if keyword.iskeyword(name) else name)
    assert language._model_ is module.Model


async def test_language_matches_wttr_in() -> None:
    """wttr.in names the languages it supports when asked for one it doesn't."""
    async with (
        ClientSession(timeout=ClientTimeout(total=60)) as session,
        session.get("https://wttr.in/", params={"format": "j1", "lang": "invalid"}) as response,
    ):
        text = await response.text()
    supported = re.search(r"expected one of \[([^\]]*)\]", text)
    assert supported, text
    assert sorted(map(str, aiopywttr.Language)) == sorted(supported[1].split())
