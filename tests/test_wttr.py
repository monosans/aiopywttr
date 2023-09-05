from __future__ import annotations

import pytest
from aiohttp import ClientSession

import aiopywttr

pytestmark = pytest.mark.filterwarnings(
    "ignore::aiopywttr.WttrClassDeprecationWarning"
)


@pytest.mark.parametrize("language", aiopywttr.Language)
async def test_wttr(
    location: str, language: aiopywttr.Language, http_session: ClientSession
) -> None:
    wttr = aiopywttr.Wttr(location, session=http_session)
    model = await getattr(wttr, language._name_.lower())()
    assert isinstance(model, language._model_)


async def test_wttr_without_session(location: str) -> None:
    wttr = aiopywttr.Wttr(location)
    language = aiopywttr.Language.EN
    model = await getattr(wttr, language._name_.lower())()
    assert isinstance(model, language._model_)
