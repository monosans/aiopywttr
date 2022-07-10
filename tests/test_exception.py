from __future__ import annotations

import pytest
from aiohttp.client_exceptions import ClientResponseError

from aiopywttr import Wttr


async def test_exception() -> None:
    wttr = Wttr("sdlaghdsaklgthj")
    with pytest.raises(ClientResponseError):
        await wttr.en()
