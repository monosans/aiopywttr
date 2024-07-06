from __future__ import annotations

from typing import AsyncIterator

import pydantic.v1 as pydantic
import pytest
from aiohttp import ClientSession


@pytest.fixture
async def http_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as s:
        yield s


@pytest.fixture
def location() -> str:
    return "Paris"


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.forbid)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_all", True)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_assignment", True)
