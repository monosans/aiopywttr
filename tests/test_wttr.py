from __future__ import annotations

import pytest
from aiohttp import ClientSession, ClientTimeout
from pydantic import AnyHttpUrl

import aiopywttr


@pytest.mark.parametrize(
    "language", [lang for lang in aiopywttr.Language if lang is not aiopywttr.Language.EN]
)
async def test_wttr_without_session(language: aiopywttr.Language) -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


async def test_wttr_with_session() -> None:
    language = aiopywttr.Language.EN

    async with ClientSession(timeout=ClientTimeout(total=60, connect=5)) as s:
        wttr = aiopywttr.Wttr(session=s)
        weather = await wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


def test_wttr_base_url_default() -> None:
    assert aiopywttr.Wttr().base_url == AnyHttpUrl("https://wttr.in")


def test_wttr_base_url_custom() -> None:
    base_url = AnyHttpUrl("https://example.com/wttr")
    assert aiopywttr.Wttr(base_url=base_url).base_url == base_url


async def test_wttr_close_without_session() -> None:
    wttr = aiopywttr.Wttr()
    assert wttr.session is None
    await wttr.close()
    assert wttr.session is None


async def test_wttr_close_closes_passed_session() -> None:
    session = ClientSession()
    async with aiopywttr.Wttr(session=session) as wttr:
        assert wttr.session is session
    assert session.closed
