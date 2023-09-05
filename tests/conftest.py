from __future__ import annotations

import asyncio
from typing import AsyncIterator, Iterator

import pytest
from aiohttp import ClientSession

try:
    from pydantic.v1 import BaseConfig, Extra
except ImportError:  # pragma: no cover
    from pydantic import BaseConfig, Extra  # type: ignore[assignment]


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def location() -> str:
    return "Paris"


@pytest.fixture(scope="session")
async def http_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as s:
        yield s


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(BaseConfig, "extra", Extra.forbid)
    monkeypatch.setattr(BaseConfig, "validate_all", True)
    monkeypatch.setattr(BaseConfig, "validate_assignment", True)
