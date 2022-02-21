# -*- coding: utf-8 -*-
from typing import Any, Optional

import pywttr_models
from aiohttp import ClientSession


class Wttr:
    """Asynchronous wrapper for wttr.in weather forecast."""

    def __init__(
        self, location: str, *, session: Optional[ClientSession] = None
    ) -> None:
        self.location = location
        self.session = session

    async def af(self) -> pywttr_models.af.Model:
        return pywttr_models.af.Model.parse_obj(await self._get_json("af"))

    async def am(self) -> pywttr_models.am.Model:
        return pywttr_models.am.Model.parse_obj(await self._get_json("am"))

    async def ar(self) -> pywttr_models.ar.Model:
        return pywttr_models.ar.Model.parse_obj(await self._get_json("ar"))

    async def az(self) -> pywttr_models.az.Model:
        return pywttr_models.az.Model.parse_obj(await self._get_json("az"))

    async def be(self) -> pywttr_models.be.Model:
        return pywttr_models.be.Model.parse_obj(await self._get_json("be"))

    async def bg(self) -> pywttr_models.bg.Model:
        return pywttr_models.bg.Model.parse_obj(await self._get_json("bg"))

    async def bn(self) -> pywttr_models.bn.Model:
        return pywttr_models.bn.Model.parse_obj(await self._get_json("bn"))

    async def bs(self) -> pywttr_models.bs.Model:
        return pywttr_models.bs.Model.parse_obj(await self._get_json("bs"))

    async def ca(self) -> pywttr_models.ca.Model:
        return pywttr_models.ca.Model.parse_obj(await self._get_json("ca"))

    async def cs(self) -> pywttr_models.cs.Model:
        return pywttr_models.cs.Model.parse_obj(await self._get_json("cs"))

    async def cy(self) -> pywttr_models.cy.Model:
        return pywttr_models.cy.Model.parse_obj(await self._get_json("cy"))

    async def da(self) -> pywttr_models.da.Model:
        return pywttr_models.da.Model.parse_obj(await self._get_json("da"))

    async def de(self) -> pywttr_models.de.Model:
        return pywttr_models.de.Model.parse_obj(await self._get_json("de"))

    async def el(self) -> pywttr_models.el.Model:
        return pywttr_models.el.Model.parse_obj(await self._get_json("el"))

    async def en(self) -> pywttr_models.en.Model:
        return pywttr_models.en.Model.parse_obj(await self._get_json("en"))

    async def eo(self) -> pywttr_models.eo.Model:
        return pywttr_models.eo.Model.parse_obj(await self._get_json("eo"))

    async def es(self) -> pywttr_models.es.Model:
        return pywttr_models.es.Model.parse_obj(await self._get_json("es"))

    async def et(self) -> pywttr_models.et.Model:
        return pywttr_models.et.Model.parse_obj(await self._get_json("et"))

    async def eu(self) -> pywttr_models.eu.Model:
        return pywttr_models.eu.Model.parse_obj(await self._get_json("eu"))

    async def fa(self) -> pywttr_models.fa.Model:
        return pywttr_models.fa.Model.parse_obj(await self._get_json("fa"))

    async def fi(self) -> pywttr_models.fi.Model:
        return pywttr_models.fi.Model.parse_obj(await self._get_json("fi"))

    async def fr(self) -> pywttr_models.fr.Model:
        return pywttr_models.fr.Model.parse_obj(await self._get_json("fr"))

    async def fy(self) -> pywttr_models.fy.Model:
        return pywttr_models.fy.Model.parse_obj(await self._get_json("fy"))

    async def ga(self) -> pywttr_models.ga.Model:
        return pywttr_models.ga.Model.parse_obj(await self._get_json("ga"))

    async def he(self) -> pywttr_models.he.Model:
        return pywttr_models.he.Model.parse_obj(await self._get_json("he"))

    async def hi(self) -> pywttr_models.hi.Model:
        return pywttr_models.hi.Model.parse_obj(await self._get_json("hi"))

    async def hr(self) -> pywttr_models.hr.Model:
        return pywttr_models.hr.Model.parse_obj(await self._get_json("hr"))

    async def hu(self) -> pywttr_models.hu.Model:
        return pywttr_models.hu.Model.parse_obj(await self._get_json("hu"))

    async def hy(self) -> pywttr_models.hy.Model:
        return pywttr_models.hy.Model.parse_obj(await self._get_json("hy"))

    async def ia(self) -> pywttr_models.ia.Model:
        return pywttr_models.ia.Model.parse_obj(await self._get_json("ia"))

    async def id(self) -> pywttr_models.id.Model:
        return pywttr_models.id.Model.parse_obj(await self._get_json("id"))

    async def is_(self) -> pywttr_models.is_.Model:
        return pywttr_models.is_.Model.parse_obj(await self._get_json("is"))

    async def it(self) -> pywttr_models.it.Model:
        return pywttr_models.it.Model.parse_obj(await self._get_json("it"))

    async def ja(self) -> pywttr_models.ja.Model:
        return pywttr_models.ja.Model.parse_obj(await self._get_json("ja"))

    async def jv(self) -> pywttr_models.jv.Model:
        return pywttr_models.jv.Model.parse_obj(await self._get_json("jv"))

    async def kk(self) -> pywttr_models.kk.Model:
        return pywttr_models.kk.Model.parse_obj(await self._get_json("kk"))

    async def ko(self) -> pywttr_models.ko.Model:
        return pywttr_models.ko.Model.parse_obj(await self._get_json("ko"))

    async def lt(self) -> pywttr_models.lt.Model:
        return pywttr_models.lt.Model.parse_obj(await self._get_json("lt"))

    async def lv(self) -> pywttr_models.lv.Model:
        return pywttr_models.lv.Model.parse_obj(await self._get_json("lv"))

    async def mg(self) -> pywttr_models.mg.Model:
        return pywttr_models.mg.Model.parse_obj(await self._get_json("mg"))

    async def mk(self) -> pywttr_models.mk.Model:
        return pywttr_models.mk.Model.parse_obj(await self._get_json("mk"))

    async def mr(self) -> pywttr_models.mr.Model:
        return pywttr_models.mr.Model.parse_obj(await self._get_json("mr"))

    async def nb(self) -> pywttr_models.nb.Model:
        return pywttr_models.nb.Model.parse_obj(await self._get_json("nb"))

    async def nl(self) -> pywttr_models.nl.Model:
        return pywttr_models.nl.Model.parse_obj(await self._get_json("nl"))

    async def nn(self) -> pywttr_models.nn.Model:
        return pywttr_models.nn.Model.parse_obj(await self._get_json("nn"))

    async def oc(self) -> pywttr_models.oc.Model:
        return pywttr_models.oc.Model.parse_obj(await self._get_json("oc"))

    async def pl(self) -> pywttr_models.pl.Model:
        return pywttr_models.pl.Model.parse_obj(await self._get_json("pl"))

    async def pt(self) -> pywttr_models.pt.Model:
        return pywttr_models.pt.Model.parse_obj(await self._get_json("pt"))

    async def pt_br(self) -> pywttr_models.pt_br.Model:
        return pywttr_models.pt_br.Model.parse_obj(
            await self._get_json("pt-br")
        )

    async def ro(self) -> pywttr_models.ro.Model:
        return pywttr_models.ro.Model.parse_obj(await self._get_json("ro"))

    async def ru(self) -> pywttr_models.ru.Model:
        return pywttr_models.ru.Model.parse_obj(await self._get_json("ru"))

    async def sk(self) -> pywttr_models.sk.Model:
        return pywttr_models.sk.Model.parse_obj(await self._get_json("sk"))

    async def sl(self) -> pywttr_models.sl.Model:
        return pywttr_models.sl.Model.parse_obj(await self._get_json("sl"))

    async def sr(self) -> pywttr_models.sr.Model:
        return pywttr_models.sr.Model.parse_obj(await self._get_json("sr"))

    async def sr_lat(self) -> pywttr_models.sr_lat.Model:
        return pywttr_models.sr_lat.Model.parse_obj(
            await self._get_json("sr-lat")
        )

    async def sv(self) -> pywttr_models.sv.Model:
        return pywttr_models.sv.Model.parse_obj(await self._get_json("sv"))

    async def ta(self) -> pywttr_models.ta.Model:
        return pywttr_models.ta.Model.parse_obj(await self._get_json("ta"))

    async def te(self) -> pywttr_models.te.Model:
        return pywttr_models.te.Model.parse_obj(await self._get_json("te"))

    async def th(self) -> pywttr_models.th.Model:
        return pywttr_models.th.Model.parse_obj(await self._get_json("th"))

    async def tr(self) -> pywttr_models.tr.Model:
        return pywttr_models.tr.Model.parse_obj(await self._get_json("tr"))

    async def uk(self) -> pywttr_models.uk.Model:
        return pywttr_models.uk.Model.parse_obj(await self._get_json("uk"))

    async def uz(self) -> pywttr_models.uz.Model:
        return pywttr_models.uz.Model.parse_obj(await self._get_json("uz"))

    async def vi(self) -> pywttr_models.vi.Model:
        return pywttr_models.vi.Model.parse_obj(await self._get_json("vi"))

    async def zh(self) -> pywttr_models.zh.Model:
        return pywttr_models.zh.Model.parse_obj(await self._get_json("zh"))

    async def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return pywttr_models.zh_cn.Model.parse_obj(
            await self._get_json("zh-cn")
        )

    async def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return pywttr_models.zh_tw.Model.parse_obj(
            await self._get_json("zh-tw")
        )

    async def zu(self) -> pywttr_models.zu.Model:
        return pywttr_models.zu.Model.parse_obj(await self._get_json("zu"))

    async def _fetch(self, lang: str, session: ClientSession) -> Any:
        async with session.get(
            f"https://wttr.in/{self.location}",
            params={"format": "j1", "lang": lang},
            raise_for_status=True,
        ) as r:
            return await r.json()

    async def _get_json(self, lang: str) -> Any:
        if isinstance(self.session, ClientSession) and not self.session.closed:
            return await self._fetch(lang, self.session)
        async with ClientSession() as session:
            return await self._fetch(lang, session)
