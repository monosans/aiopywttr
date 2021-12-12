# -*- coding: utf-8 -*-
from typing import Optional as _Optional

import pywttr_models as _pywttr_models
from aiohttp import ClientSession as _ClientSession

from aiopywttr.http import get_json as _get_json


async def get_forecast(
    location: str, *, session: _Optional[_ClientSession] = None
) -> _pywttr_models.zh.Model:
    return _pywttr_models.zh.Model(
        **(await _get_json(location, session, "zh"))
    )
