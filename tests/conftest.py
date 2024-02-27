from __future__ import annotations

from typing import AsyncIterator, Iterator, Type

import pydantic
import pytest
from aiohttp import ClientSession

import aiopywttr


@pytest.fixture()
async def http_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as s:
        yield s


@pytest.fixture()
def location() -> str:
    return "Paris"


def _get_models(
    cls: Type[pydantic.BaseModel] = pydantic.BaseModel, /
) -> Iterator[Type[pydantic.BaseModel]]:
    for subclass in cls.__subclasses__():
        if subclass.__module__.startswith(f"{aiopywttr.models.__name__}."):
            yield subclass
        yield from _get_models(subclass)


@pytest.fixture()
def _pydantic_ignore_extra(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    with monkeypatch.context() as m:
        for model in _get_models():
            m.setitem(model.model_config, "extra", "ignore")
            model.model_rebuild(force=True)
        yield
    for model in _get_models():
        model.model_rebuild(force=True)


@pytest.fixture(autouse=True)
def _pydantic_forbid_extra(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    with monkeypatch.context() as m:
        for model in _get_models():
            m.setitem(model.model_config, "extra", "forbid")
            model.model_rebuild(force=True)
        yield
    for model in _get_models():
        model.model_rebuild(force=True)
