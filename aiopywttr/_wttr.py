from __future__ import annotations

from typing import Any, Optional

import pywttr_models
from aiohttp import ClientResponse, ClientSession


class Wttr:
    """Asynchronous wrapper for wttr.in weather forecast API."""

    __slots__ = ("location", "session")

    def __init__(self, location: str, session: Optional[ClientSession] = None) -> None:
        self.location = location
        self.session = session

    async def af(self) -> pywttr_models.af.Model:
        return pywttr_models.af.Model.parse_obj(await self._get_json("af"))

    async def am(self) -> pywttr_models.am.Model:
        return pywttr_models.am.Model.parse_obj(await self._get_json("am"))

    async def ar(self) -> pywttr_models.ar.Model:
        return pywttr_models.ar.Model.parse_obj(await self._get_json("ar"))

    async def be(self) -> pywttr_models.be.Model:
        return pywttr_models.be.Model.parse_obj(await self._get_json("be"))

    async def bn(self) -> pywttr_models.bn.Model:
        return pywttr_models.bn.Model.parse_obj(await self._get_json("bn"))

    async def ca(self) -> pywttr_models.ca.Model:
        return pywttr_models.ca.Model.parse_obj(await self._get_json("ca"))

    async def da(self) -> pywttr_models.da.Model:
        return pywttr_models.da.Model.parse_obj(await self._get_json("da"))

    async def de(self) -> pywttr_models.de.Model:
        return pywttr_models.de.Model.parse_obj(await self._get_json("de"))

    async def el(self) -> pywttr_models.el.Model:
        return pywttr_models.el.Model.parse_obj(await self._get_json("el"))

    async def en(self) -> pywttr_models.en.Model:
        return pywttr_models.en.Model.parse_obj(await self._get_json("en"))

    async def et(self) -> pywttr_models.et.Model:
        return pywttr_models.et.Model.parse_obj(await self._get_json("et"))

    async def fa(self) -> pywttr_models.fa.Model:
        return pywttr_models.fa.Model.parse_obj(await self._get_json("fa"))

    async def fr(self) -> pywttr_models.fr.Model:
        return pywttr_models.fr.Model.parse_obj(await self._get_json("fr"))

    async def gl(self) -> pywttr_models.gl.Model:
        return pywttr_models.gl.Model.parse_obj(await self._get_json("gl"))

    async def hi(self) -> pywttr_models.hi.Model:
        return pywttr_models.hi.Model.parse_obj(await self._get_json("hi"))

    async def hu(self) -> pywttr_models.hu.Model:
        return pywttr_models.hu.Model.parse_obj(await self._get_json("hu"))

    async def ia(self) -> pywttr_models.ia.Model:
        return pywttr_models.ia.Model.parse_obj(await self._get_json("ia"))

    async def id(self) -> pywttr_models.id.Model:  # noqa: A003
        return pywttr_models.id.Model.parse_obj(await self._get_json("id"))

    async def it(self) -> pywttr_models.it.Model:
        return pywttr_models.it.Model.parse_obj(await self._get_json("it"))

    async def lt(self) -> pywttr_models.lt.Model:
        return pywttr_models.lt.Model.parse_obj(await self._get_json("lt"))

    async def mg(self) -> pywttr_models.mg.Model:
        return pywttr_models.mg.Model.parse_obj(await self._get_json("mg"))

    async def nb(self) -> pywttr_models.nb.Model:
        return pywttr_models.nb.Model.parse_obj(await self._get_json("nb"))

    async def nl(self) -> pywttr_models.nl.Model:
        return pywttr_models.nl.Model.parse_obj(await self._get_json("nl"))

    async def oc(self) -> pywttr_models.oc.Model:
        return pywttr_models.oc.Model.parse_obj(await self._get_json("oc"))

    async def pl(self) -> pywttr_models.pl.Model:
        return pywttr_models.pl.Model.parse_obj(await self._get_json("pl"))

    async def pt_br(self) -> pywttr_models.pt_br.Model:
        return pywttr_models.pt_br.Model.parse_obj(await self._get_json("pt-br"))

    async def ro(self) -> pywttr_models.ro.Model:
        return pywttr_models.ro.Model.parse_obj(await self._get_json("ro"))

    async def ru(self) -> pywttr_models.ru.Model:
        return pywttr_models.ru.Model.parse_obj(await self._get_json("ru"))

    async def ta(self) -> pywttr_models.ta.Model:
        return pywttr_models.ta.Model.parse_obj(await self._get_json("ta"))

    async def th(self) -> pywttr_models.th.Model:
        return pywttr_models.th.Model.parse_obj(await self._get_json("th"))

    async def tr(self) -> pywttr_models.tr.Model:
        return pywttr_models.tr.Model.parse_obj(await self._get_json("tr"))

    async def uk(self) -> pywttr_models.uk.Model:
        return pywttr_models.uk.Model.parse_obj(await self._get_json("uk"))

    async def vi(self) -> pywttr_models.vi.Model:
        return pywttr_models.vi.Model.parse_obj(await self._get_json("vi"))

    async def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return pywttr_models.zh_cn.Model.parse_obj(await self._get_json("zh-cn"))

    async def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return pywttr_models.zh_tw.Model.parse_obj(await self._get_json("zh-tw"))

    async def _get_json(self, lang: str) -> Any:
        if isinstance(self.session, ClientSession) and not self.session.closed:
            response = await self._fetch(lang, self.session)
        else:
            async with ClientSession() as session:
                response = await self._fetch(lang, session)
        return await response.json()

    async def _fetch(self, lang: str, session: ClientSession) -> ClientResponse:
        async with session.get(
            f"https://wttr.in/{self.location}",
            params={"format": "j1", "lang": lang},
            raise_for_status=True,
        ) as response:
            await response.read()
        return response
