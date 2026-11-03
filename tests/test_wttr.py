from __future__ import annotations

import pytest
from aiohttp import ClientSession, web
from aiohttp.test_utils import TestServer
from pydantic import AnyHttpUrl

import aiopywttr


@pytest.mark.parametrize(
    "language", [lang for lang in aiopywttr.Language if lang is not aiopywttr.Language.EN]
)
async def test_wttr_without_session(language: aiopywttr.Language) -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


async def test_wttr_english_descriptions() -> None:
    """wttr.in sends no `lang_en` or `lang_xx` for English, so both give `weather_desc`."""
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Paris", language=aiopywttr.Language.EN)
    assert weather.current_condition
    for current in weather.current_condition:
        assert current.lang_en == current.lang_xx == current.weather_desc
    hours = [hour for day in weather.weather for hour in day.hourly]
    assert hours
    for hour in hours:
        assert hour.lang_en == hour.lang_xx == hour.weather_desc


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


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("", "/Paris?format=j1&lang=de"),
        ("/wttr", "/wttr/Paris?format=j1&lang=de"),
        ("/wttr/", "/wttr/Paris?format=j1&lang=de"),
    ],
)
async def test_wttr_request_url(path: str, expected: str) -> None:
    requests: list[web.Request] = []

    async def handler(request: web.Request) -> web.Response:  # noqa: RUF029
        requests.append(request)
        return web.json_response({
            "current_condition": [],
            "nearest_area": [],
            "request": [],
            "weather": [],
        })

    app = web.Application()
    app.router.add_get("/{tail:.*}", handler)
    async with TestServer(app) as server, ClientSession() as session:
        wttr = aiopywttr.Wttr(base_url=AnyHttpUrl(str(server.make_url(path))), session=session)
        await wttr.weather("Paris", language=aiopywttr.Language.DE)
    assert [request.path_qs for request in requests] == [expected]
