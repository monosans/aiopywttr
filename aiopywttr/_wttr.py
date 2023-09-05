from __future__ import annotations

from typing import Optional

import pywttr_models
from aiohttp import ClientSession
from pywttr_models._language import Language
from typing_extensions import deprecated

from ._get_weather import get_weather


class WttrClassDeprecationWarning(DeprecationWarning):
    pass


@deprecated(
    "Use get_weather function instead", category=WttrClassDeprecationWarning
)
class Wttr:
    """Asynchronous wrapper for wttr.in weather API.

    !!! warning "Deprecated"
        Use [get_weather](.#aiopywttr.get_weather) function instead.

    Examples:
        Prints the average temperature in Paris today:

        ```python
        import asyncio

        import aiopywttr


        async def main():
            wttr = aiopywttr.Wttr("Paris")
            weather = await wttr.en()
            print(weather.weather[0].avgtemp_c)


        asyncio.run(main())
        ```
    """

    __slots__ = ("location", "session")

    def __init__(
        self, location: str, session: Optional[ClientSession] = None
    ) -> None:
        self.location = location
        self.session = session

    async def af(self) -> pywttr_models.af.Model:
        return await get_weather(
            self.location, Language.AF, session=self.session
        )

    async def am(self) -> pywttr_models.am.Model:
        return await get_weather(
            self.location, Language.AM, session=self.session
        )

    async def ar(self) -> pywttr_models.ar.Model:
        return await get_weather(
            self.location, Language.AR, session=self.session
        )

    async def be(self) -> pywttr_models.be.Model:
        return await get_weather(
            self.location, Language.BE, session=self.session
        )

    async def bn(self) -> pywttr_models.bn.Model:
        return await get_weather(
            self.location, Language.BN, session=self.session
        )

    async def ca(self) -> pywttr_models.ca.Model:
        return await get_weather(
            self.location, Language.CA, session=self.session
        )

    async def da(self) -> pywttr_models.da.Model:
        return await get_weather(
            self.location, Language.DA, session=self.session
        )

    async def de(self) -> pywttr_models.de.Model:
        return await get_weather(
            self.location, Language.DE, session=self.session
        )

    async def el(self) -> pywttr_models.el.Model:
        return await get_weather(
            self.location, Language.EL, session=self.session
        )

    async def en(self) -> pywttr_models.en.Model:
        return await get_weather(
            self.location, Language.EN, session=self.session
        )

    async def et(self) -> pywttr_models.et.Model:
        return await get_weather(
            self.location, Language.ET, session=self.session
        )

    async def fa(self) -> pywttr_models.fa.Model:
        return await get_weather(
            self.location, Language.FA, session=self.session
        )

    async def fr(self) -> pywttr_models.fr.Model:
        return await get_weather(
            self.location, Language.FR, session=self.session
        )

    async def gl(self) -> pywttr_models.gl.Model:
        return await get_weather(
            self.location, Language.GL, session=self.session
        )

    async def hi(self) -> pywttr_models.hi.Model:
        return await get_weather(
            self.location, Language.HI, session=self.session
        )

    async def hu(self) -> pywttr_models.hu.Model:
        return await get_weather(
            self.location, Language.HU, session=self.session
        )

    async def ia(self) -> pywttr_models.ia.Model:
        return await get_weather(
            self.location, Language.IA, session=self.session
        )

    async def id(self) -> pywttr_models.id.Model:  # noqa: A003
        return await get_weather(
            self.location, Language.ID, session=self.session
        )

    async def it(self) -> pywttr_models.it.Model:
        return await get_weather(
            self.location, Language.IT, session=self.session
        )

    async def lt(self) -> pywttr_models.lt.Model:
        return await get_weather(
            self.location, Language.LT, session=self.session
        )

    async def mg(self) -> pywttr_models.mg.Model:
        return await get_weather(
            self.location, Language.MG, session=self.session
        )

    async def nb(self) -> pywttr_models.nb.Model:
        return await get_weather(
            self.location, Language.NB, session=self.session
        )

    async def nl(self) -> pywttr_models.nl.Model:
        return await get_weather(
            self.location, Language.NL, session=self.session
        )

    async def oc(self) -> pywttr_models.oc.Model:
        return await get_weather(
            self.location, Language.OC, session=self.session
        )

    async def pl(self) -> pywttr_models.pl.Model:
        return await get_weather(
            self.location, Language.PL, session=self.session
        )

    async def pt_br(self) -> pywttr_models.pt_br.Model:
        return await get_weather(
            self.location, Language.PT_BR, session=self.session
        )

    async def ro(self) -> pywttr_models.ro.Model:
        return await get_weather(
            self.location, Language.RO, session=self.session
        )

    async def ru(self) -> pywttr_models.ru.Model:
        return await get_weather(
            self.location, Language.RU, session=self.session
        )

    async def ta(self) -> pywttr_models.ta.Model:
        return await get_weather(
            self.location, Language.TA, session=self.session
        )

    async def th(self) -> pywttr_models.th.Model:
        return await get_weather(
            self.location, Language.TH, session=self.session
        )

    async def tr(self) -> pywttr_models.tr.Model:
        return await get_weather(
            self.location, Language.TR, session=self.session
        )

    async def uk(self) -> pywttr_models.uk.Model:
        return await get_weather(
            self.location, Language.UK, session=self.session
        )

    async def vi(self) -> pywttr_models.vi.Model:
        return await get_weather(
            self.location, Language.VI, session=self.session
        )

    async def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return await get_weather(
            self.location, Language.ZH_CN, session=self.session
        )

    async def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return await get_weather(
            self.location, Language.ZH_TW, session=self.session
        )
