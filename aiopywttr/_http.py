from __future__ import annotations

from typing import Optional

from aiohttp import ClientResponse, ClientSession, hdrs
from typing_extensions import Any


async def get_json(
    location: str, language: str, session: Optional[ClientSession]
) -> Any:
    if isinstance(session, ClientSession) and not session.closed:
        response = await fetch(location, language, session)
    else:
        async with ClientSession() as session:  # noqa: PLR1704
            response = await fetch(location, language, session)
    return await response.json()


async def fetch(
    location: str, language: str, session: ClientSession
) -> ClientResponse:
    async with session.get(
        f"https://wttr.in/{location}",
        params={"format": "j1", "lang": language},
        headers={hdrs.ACCEPT: "application/json"},
        raise_for_status=True,
    ) as response:
        await response.read()
    return response
