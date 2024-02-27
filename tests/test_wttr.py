from __future__ import annotations

import pytest
from aiohttp import ClientSession

import aiopywttr


@pytest.mark.parametrize("language", aiopywttr.Language)
async def test_wttr(
    location: str, language: aiopywttr.Language, http_session: ClientSession
) -> None:
    with pytest.warns(aiopywttr.WttrClassDeprecationWarning):
        wttr = aiopywttr.Wttr(location, session=http_session)
    model = await getattr(wttr, language._name_.lower())()
    assert isinstance(model, language._model_)


async def test_wttr_without_session(location: str) -> None:
    with pytest.warns(aiopywttr.WttrClassDeprecationWarning):
        wttr = aiopywttr.Wttr(location)
    model = await wttr.en()
    assert isinstance(model, aiopywttr.Language.EN._model_)
