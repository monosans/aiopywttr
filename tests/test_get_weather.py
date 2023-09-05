from __future__ import annotations

import pytest
from aiohttp import ClientSession

import aiopywttr


@pytest.mark.parametrize("language", aiopywttr.Language)
async def test_get_weather(
    location: str, language: aiopywttr.Language, http_session: ClientSession
) -> None:
    model = await aiopywttr.get_weather(
        location, language, session=http_session
    )
    assert isinstance(model, language._model_)


async def test_get_weather_without_session(location: str) -> None:
    language = aiopywttr.Language.EN
    model = await aiopywttr.get_weather(location, language)
    assert isinstance(model, language._model_)


async def test_language_type_error(location: str) -> None:
    msg = "Invalid language 'en'. Must be a member of aiopywttr.Language enum."
    with pytest.raises(TypeError, match=msg):
        await aiopywttr.get_weather(  # type: ignore[call-overload]
            location, "en"
        )
