from __future__ import annotations

from typing import Optional

from aiohttp import ClientResponse, ClientSession


async def get_json(
    *, location: str, language: str, session: Optional[ClientSession]
) -> str:
    if isinstance(session, ClientSession) and not session.closed:
        response = await fetch(
            location=location, language=language, session=session
        )
    else:
        async with ClientSession() as session:  # noqa: PLR1704
            response = await fetch(
                location=location, language=language, session=session
            )
    return await response.text()


async def fetch(
    *, location: str, language: str, session: ClientSession
) -> ClientResponse:
    async with session.get(
        f"https://wttr.in/{location}",
        params={"format": "j1", "lang": language},
        raise_for_status=True,
    ) as response:
        await response.read()
    return response
