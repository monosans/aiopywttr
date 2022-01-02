# -*- coding: utf-8 -*-
import pytest
from aiohttp.client_exceptions import ClientResponseError

import aiopywttr


@pytest.mark.asyncio()
async def test_validation() -> None:
    location = "sdlaghdsaklgthj"
    with pytest.raises(ClientResponseError):
        await aiopywttr.en.get_forecast(location)
