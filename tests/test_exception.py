# -*- coding: utf-8 -*-
import pytest
from aiohttp.client_exceptions import ClientResponseError

from aiopywttr import Wttr


@pytest.mark.asyncio()
async def test_exception() -> None:
    wttr = Wttr("sdlaghdsaklgthj")
    with pytest.raises(ClientResponseError):
        await wttr.en()
