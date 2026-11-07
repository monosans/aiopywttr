from __future__ import annotations

import functools
import types
from typing import TYPE_CHECKING, Final, Literal, Self, TypeVar, cast, final, overload

import pywttr_models
from aiohttp import ClientSession, ClientTimeout, hdrs
from pydantic import AnyHttpUrl, validate_call
from pywttr_models._language import Language  # noqa: PLC2701

if TYPE_CHECKING:
    from collections.abc import Callable

_F = TypeVar("_F", bound="Callable[..., object]")


def _validate_arguments(func: _F, /) -> _F:
    """Validate the arguments of `func` as `validate_call` does.

    `validate_call` evaluates the return annotation too, though it doesn't
    validate the return value, and `pywttr_models.AnyModel` imports the models
    of all 76 languages, where a request needs those of one. So it is handed a
    copy of `func` without the return annotation.
    """
    function = cast("types.FunctionType", func)
    copy = types.FunctionType(
        function.__code__,
        function.__globals__,
        function.__name__,
        function.__defaults__,
        function.__closure__,
    )
    copy.__kwdefaults__ = function.__kwdefaults__
    copy.__qualname__ = function.__qualname__
    copy.__annotations__ = {
        name: value for name, value in function.__annotations__.items() if name != "return"
    }
    validated = validate_call(config={"arbitrary_types_allowed": True})(copy)
    return cast("_F", functools.update_wrapper(validated, function))


@final
class Wttr:
    """Asynchronous client for the wttr.in weather API.

    Use it as an async context manager or call `close` when done.

    Args:
        base_url: Server to send requests to, e.g. a self-hosted wttr.in.
        session: HTTP client to send requests with. If `None`, one is
            created on the first request, with a 60 s total timeout
            (5 s to connect). `close` closes it either way.

    Examples:
        ```python
        import asyncio

        import aiopywttr


        async def main() -> None:
            async with aiopywttr.Wttr() as wttr:
                weather = await wttr.weather("Paris")


        asyncio.run(main())
        ```
    """

    __slots__ = ("_base_url", "_session")

    @validate_call(config={"arbitrary_types_allowed": True})
    def __init__(
        self,
        *,
        base_url: AnyHttpUrl = AnyHttpUrl.build(  # noqa: B008
            scheme="https", host="wttr.in"
        ),
        session: ClientSession | None = None,
    ) -> None:
        self._base_url: Final = base_url
        self._session = session

    @property
    def base_url(self) -> AnyHttpUrl:
        """Server the requests go to."""
        return self._base_url

    @property
    def session(self) -> ClientSession | None:
        """HTTP client; `None` until the first request if none was passed."""
        return self._session

    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.AF]
    ) -> pywttr_models.af.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.AM]
    ) -> pywttr_models.am.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.AR]
    ) -> pywttr_models.ar.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.AZ]
    ) -> pywttr_models.az.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BA]
    ) -> pywttr_models.ba.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BE]
    ) -> pywttr_models.be.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BG]
    ) -> pywttr_models.bg.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BN]
    ) -> pywttr_models.bn.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BS]
    ) -> pywttr_models.bs.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BY]
    ) -> pywttr_models.by.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.CA]
    ) -> pywttr_models.ca.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.CRK]
    ) -> pywttr_models.crk.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.CS]
    ) -> pywttr_models.cs.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.CY]
    ) -> pywttr_models.cy.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.DA]
    ) -> pywttr_models.da.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.DE]
    ) -> pywttr_models.de.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.EL]
    ) -> pywttr_models.el.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.EN]
    ) -> pywttr_models.en.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.EO]
    ) -> pywttr_models.eo.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ES]
    ) -> pywttr_models.es.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ET]
    ) -> pywttr_models.et.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.EU]
    ) -> pywttr_models.eu.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.FA]
    ) -> pywttr_models.fa.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.FI]
    ) -> pywttr_models.fi.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.FR]
    ) -> pywttr_models.fr.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.FY]
    ) -> pywttr_models.fy.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.GA]
    ) -> pywttr_models.ga.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.GL]
    ) -> pywttr_models.gl.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HE]
    ) -> pywttr_models.he.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HI]
    ) -> pywttr_models.hi.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HR]
    ) -> pywttr_models.hr.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HU]
    ) -> pywttr_models.hu.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HY]
    ) -> pywttr_models.hy.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.IA]
    ) -> pywttr_models.ia.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ID]
    ) -> pywttr_models.id.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.IS]
    ) -> pywttr_models.is_.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.IT]
    ) -> pywttr_models.it.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.JA]
    ) -> pywttr_models.ja.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.JV]
    ) -> pywttr_models.jv.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.KA]
    ) -> pywttr_models.ka.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.KK]
    ) -> pywttr_models.kk.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.KO]
    ) -> pywttr_models.ko.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.KY]
    ) -> pywttr_models.ky.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.LT]
    ) -> pywttr_models.lt.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.LV]
    ) -> pywttr_models.lv.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.MG]
    ) -> pywttr_models.mg.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.MK]
    ) -> pywttr_models.mk.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ML]
    ) -> pywttr_models.ml.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.MR]
    ) -> pywttr_models.mr.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.NB]
    ) -> pywttr_models.nb.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.NL]
    ) -> pywttr_models.nl.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.NN]
    ) -> pywttr_models.nn.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.OC]
    ) -> pywttr_models.oc.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.PA]
    ) -> pywttr_models.pa.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.PL]
    ) -> pywttr_models.pl.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.PT]
    ) -> pywttr_models.pt.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.PT_BR]
    ) -> pywttr_models.pt_br.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.RO]
    ) -> pywttr_models.ro.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.RU]
    ) -> pywttr_models.ru.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.SK]
    ) -> pywttr_models.sk.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.SL]
    ) -> pywttr_models.sl.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.SR]
    ) -> pywttr_models.sr.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.SR_LAT]
    ) -> pywttr_models.sr_lat.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.SV]
    ) -> pywttr_models.sv.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.SW]
    ) -> pywttr_models.sw.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.TA]
    ) -> pywttr_models.ta.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.TE]
    ) -> pywttr_models.te.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.TH]
    ) -> pywttr_models.th.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.TR]
    ) -> pywttr_models.tr.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.TS]
    ) -> pywttr_models.ts.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.UK]
    ) -> pywttr_models.uk.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.VI]
    ) -> pywttr_models.vi.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ZH]
    ) -> pywttr_models.zh.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ZH_CN]
    ) -> pywttr_models.zh_cn.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ZH_TW]
    ) -> pywttr_models.zh_tw.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ZU]
    ) -> pywttr_models.zu.Model: ...
    @overload
    async def weather(self, location: str, /, *, language: Language) -> pywttr_models.AnyModel: ...

    @_validate_arguments
    async def weather(
        self, location: str, /, *, language: Language = Language.EN
    ) -> pywttr_models.AnyModel:
        """Get the current weather and a forecast for 3 days.

        Raises `aiohttp.ClientResponseError` if wttr.in responds with an error
        status, e.g. for an unknown location.

        Args:
            location: City, airport code, `~landmark`, `latitude,longitude`
                or anything else [wttr.in](https://wttr.in/:help) accepts.
            language: Language of the weather description. It also selects
                the return type, e.g. `Language.RU` gives
                `aiopywttr.models.ru.Model`.

        Examples:
            ```python
            import asyncio

            import aiopywttr


            async def main() -> None:
                async with aiopywttr.Wttr() as wttr:
                    weather = await wttr.weather("Paris", language=aiopywttr.Language.DE)
                print(weather.current_condition[0].lang_de[0].value)


            asyncio.run(main())
            ```
        """
        if self._session is None:
            self._session = ClientSession(timeout=ClientTimeout(total=60, connect=5))
        async with self._session.get(
            f"{str(self._base_url).rstrip('/')}/{location}",
            params={"format": "j1", "lang": language},
            headers={hdrs.ACCEPT: "application/json"},
            raise_for_status=True,
        ) as response:
            content = await response.read()
        return language._model_.model_validate_json(content)

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._session is not None:
            await self._session.close()

    async def __aenter__(self) -> Self:
        """Return the client itself."""
        return self

    async def __aexit__(self, *_: object) -> None:
        """Close the HTTP client."""
        await self.close()
