from __future__ import annotations

import asyncio
from typing import AsyncIterator, Iterator

import pydantic.v1 as pydantic
import pytest
from aiohttp import ClientSession


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def http_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as s:
        yield s


@pytest.fixture()
def location() -> str:
    return "Paris"


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.forbid)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_all", True)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_assignment", True)
