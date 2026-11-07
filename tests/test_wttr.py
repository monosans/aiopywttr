from __future__ import annotations

import inspect
import subprocess
import sys
import textwrap

import pytest
from aiohttp import ClientSession, web
from aiohttp.test_utils import TestServer
from pydantic import AnyHttpUrl, ValidationError

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


def test_weather_keeps_its_signature() -> None:
    signature = inspect.signature(aiopywttr.Wttr.weather)
    assert list(signature.parameters) == ["self", "location", "language"]
    assert signature.parameters["language"].default is aiopywttr.Language.EN
    assert signature.return_annotation == "pywttr_models.AnyModel"
    assert inspect.iscoroutinefunction(aiopywttr.Wttr.weather)


@pytest.mark.parametrize(
    ("location", "language"), [(1, aiopywttr.Language.DE), ("Paris", "not-a-language")]
)
async def test_weather_validates_its_arguments(location: object, language: object) -> None:
    wttr = aiopywttr.Wttr()
    with pytest.raises(ValidationError, match=r"validation error for Wttr\.weather"):
        await wttr.weather(location, language=language)  # type: ignore[call-overload]
    # The session is created just before the request, so none was sent.
    assert wttr.session is None


def test_import_leaves_the_return_type_of_weather_unevaluated() -> None:
    """Evaluating `pywttr_models.AnyModel` would import every language's models."""
    code = (
        "import pywttr_models\n"
        "vars(pywttr_models).pop('AnyModel', None)\n"
        "def __getattr__(name):\n"
        "    raise AttributeError(name)\n"
        "pywttr_models.__getattr__ = __getattr__\n"
        "import aiopywttr\n"
    )
    subprocess.run((sys.executable, "-c", code), check=True)  # noqa: S603


def test_only_the_language_asked_for_is_loaded() -> None:
    """Runs in a process of its own, as conftest.py loads every language."""
    code = textwrap.dedent("""
        import sys

        import aiopywttr

        def loaded(*, languages_only):
            names = {name for name in sys.modules if name.startswith("pywttr_models.")}
            if languages_only:
                names = {name for name in names if not name.startswith("pywttr_models._")}
                names.discard("pywttr_models.base")
            return names

        names = loaded(languages_only=False)
        assert names <= {"pywttr_models._language"}, names
        assert aiopywttr.Language.DE._model_.__module__ == "pywttr_models.de"
        names = loaded(languages_only=True)
        assert names == {"pywttr_models.de"}, names
    """)
    subprocess.run((sys.executable, "-c", code), check=True)  # noqa: S603
