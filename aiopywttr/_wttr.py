from __future__ import annotations

from typing import Optional

import pywttr_models
from aiohttp import ClientSession
from pydantic import ConfigDict, validate_call
from pywttr_models._language import Language  # noqa: PLC2701
from typing_extensions import deprecated, final

from ._get_weather import get_weather


class WttrClassDeprecationWarning(DeprecationWarning):
    pass


# Avoid validation costs because attributes are already validated
get_weather = get_weather.raw_function  # type: ignore[attr-defined]


@deprecated(
    "Use get_weather function instead", category=WttrClassDeprecationWarning
)
@final
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

    __slots__ = ("_location", "_session")

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def __init__(
        self, location: str, session: Optional[ClientSession] = None
    ) -> None:
        self._location = location
        self._session = session

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    @validate_call
    def location(self, value: str) -> None:
        self._location = value

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session

    @session.setter
    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def session(self, value: Optional[ClientSession]) -> None:
        self._session = value

    async def af(self) -> pywttr_models.af.Model:
        return await get_weather(
            self._location, Language.AF, session=self._session
        )

    async def am(self) -> pywttr_models.am.Model:
        return await get_weather(
            self._location, Language.AM, session=self._session
        )

    async def ar(self) -> pywttr_models.ar.Model:
        return await get_weather(
            self._location, Language.AR, session=self._session
        )

    async def be(self) -> pywttr_models.be.Model:
        return await get_weather(
            self._location, Language.BE, session=self._session
        )

    async def bn(self) -> pywttr_models.bn.Model:
        return await get_weather(
            self._location, Language.BN, session=self._session
        )

    async def ca(self) -> pywttr_models.ca.Model:
        return await get_weather(
            self._location, Language.CA, session=self._session
        )

    async def da(self) -> pywttr_models.da.Model:
        return await get_weather(
            self._location, Language.DA, session=self._session
        )

    async def de(self) -> pywttr_models.de.Model:
        return await get_weather(
            self._location, Language.DE, session=self._session
        )

    async def el(self) -> pywttr_models.el.Model:
        return await get_weather(
            self._location, Language.EL, session=self._session
        )

    async def en(self) -> pywttr_models.en.Model:
        return await get_weather(
            self._location, Language.EN, session=self._session
        )

    async def et(self) -> pywttr_models.et.Model:
        return await get_weather(
            self._location, Language.ET, session=self._session
        )

    async def fa(self) -> pywttr_models.fa.Model:
        return await get_weather(
            self._location, Language.FA, session=self._session
        )

    async def fr(self) -> pywttr_models.fr.Model:
        return await get_weather(
            self._location, Language.FR, session=self._session
        )

    async def gl(self) -> pywttr_models.gl.Model:
        return await get_weather(
            self._location, Language.GL, session=self._session
        )

    async def hi(self) -> pywttr_models.hi.Model:
        return await get_weather(
            self._location, Language.HI, session=self._session
        )

    async def hu(self) -> pywttr_models.hu.Model:
        return await get_weather(
            self._location, Language.HU, session=self._session
        )

    async def ia(self) -> pywttr_models.ia.Model:
        return await get_weather(
            self._location, Language.IA, session=self._session
        )

    async def id(self) -> pywttr_models.id.Model:
        return await get_weather(
            self._location, Language.ID, session=self._session
        )

    async def it(self) -> pywttr_models.it.Model:
        return await get_weather(
            self._location, Language.IT, session=self._session
        )

    async def lt(self) -> pywttr_models.lt.Model:
        return await get_weather(
            self._location, Language.LT, session=self._session
        )

    async def mg(self) -> pywttr_models.mg.Model:
        return await get_weather(
            self._location, Language.MG, session=self._session
        )

    async def nb(self) -> pywttr_models.nb.Model:
        return await get_weather(
            self._location, Language.NB, session=self._session
        )

    async def nl(self) -> pywttr_models.nl.Model:
        return await get_weather(
            self._location, Language.NL, session=self._session
        )

    async def oc(self) -> pywttr_models.oc.Model:
        return await get_weather(
            self._location, Language.OC, session=self._session
        )

    async def pl(self) -> pywttr_models.pl.Model:
        return await get_weather(
            self._location, Language.PL, session=self._session
        )

    async def pt_br(self) -> pywttr_models.pt_br.Model:
        return await get_weather(
            self._location, Language.PT_BR, session=self._session
        )

    async def ro(self) -> pywttr_models.ro.Model:
        return await get_weather(
            self._location, Language.RO, session=self._session
        )

    async def ru(self) -> pywttr_models.ru.Model:
        return await get_weather(
            self._location, Language.RU, session=self._session
        )

    async def ta(self) -> pywttr_models.ta.Model:
        return await get_weather(
            self._location, Language.TA, session=self._session
        )

    async def th(self) -> pywttr_models.th.Model:
        return await get_weather(
            self._location, Language.TH, session=self._session
        )

    async def tr(self) -> pywttr_models.tr.Model:
        return await get_weather(
            self._location, Language.TR, session=self._session
        )

    async def uk(self) -> pywttr_models.uk.Model:
        return await get_weather(
            self._location, Language.UK, session=self._session
        )

    async def vi(self) -> pywttr_models.vi.Model:
        return await get_weather(
            self._location, Language.VI, session=self._session
        )

    async def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return await get_weather(
            self._location, Language.ZH_CN, session=self._session
        )

    async def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return await get_weather(
            self._location, Language.ZH_TW, session=self._session
        )
