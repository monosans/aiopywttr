from __future__ import annotations

import pytest
from aiohttp import ClientSession

import aiopywttr


@pytest.mark.parametrize(
    "language",
    [lang for lang in aiopywttr.Language if lang is not aiopywttr.Language.EN],
)
async def test_wttr_without_session(language: aiopywttr.Language) -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


async def test_wttr_with_session() -> None:
    language = aiopywttr.Language.EN

    async with ClientSession() as s:
        wttr = aiopywttr.Wttr(session=s)
        weather = await wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)
