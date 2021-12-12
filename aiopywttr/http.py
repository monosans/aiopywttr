# -*- coding: utf-8 -*-
from typing import Any as _Any
from typing import Optional as _Optional

from aiohttp import ClientSession as _ClientSession


async def _fetch(location: str, session: _ClientSession, lang: str) -> _Any:
    async with session.get(
        f"https://wttr.in/{location}", params={"format": "j1", "lang": lang}
    ) as r:
        return await r.json()


async def get_json(
    location: str, session: _Optional[_ClientSession], lang: str
) -> _Any:
    if session:
        return await _fetch(location, session, lang)
    async with _ClientSession() as session:
        return await _fetch(location, session, lang)
