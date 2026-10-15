from __future__ import annotations

from typing import Final, Literal, Self, final, overload

import pywttr_models
from aiohttp import ClientSession, ClientTimeout, hdrs
from pydantic import AnyHttpUrl, validate_call
from pywttr_models._language import Language  # noqa: PLC2701


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
        import aiopywttr

        async with aiopywttr.Wttr() as wttr:
            weather = await wttr.weather("Paris")
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
        self, location: str, /, *, language: Literal[Language.BE]
    ) -> pywttr_models.be.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.BN]
    ) -> pywttr_models.bn.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.CA]
    ) -> pywttr_models.ca.Model: ...
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
        self, location: str, /, *, language: Literal[Language.EN] = ...
    ) -> pywttr_models.en.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.ET]
    ) -> pywttr_models.et.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.FA]
    ) -> pywttr_models.fa.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.FR]
    ) -> pywttr_models.fr.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.GL]
    ) -> pywttr_models.gl.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HI]
    ) -> pywttr_models.hi.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.HU]
    ) -> pywttr_models.hu.Model: ...
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
        self, location: str, /, *, language: Literal[Language.IT]
    ) -> pywttr_models.it.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.LT]
    ) -> pywttr_models.lt.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.MG]
    ) -> pywttr_models.mg.Model: ...
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
        self, location: str, /, *, language: Literal[Language.OC]
    ) -> pywttr_models.oc.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.PL]
    ) -> pywttr_models.pl.Model: ...
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
        self, location: str, /, *, language: Literal[Language.TA]
    ) -> pywttr_models.ta.Model: ...
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
        self, location: str, /, *, language: Literal[Language.UK]
    ) -> pywttr_models.uk.Model: ...
    @overload
    async def weather(
        self, location: str, /, *, language: Literal[Language.VI]
    ) -> pywttr_models.vi.Model: ...
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
        self, location: str, /, *, language: Language
    ) -> pywttr_models.AnyModel: ...

    @validate_call(config={"arbitrary_types_allowed": True})
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
            import aiopywttr

            async with aiopywttr.Wttr() as wttr:
                weather = await wttr.weather(
                    "Paris", language=aiopywttr.Language.DE
                )
            print(weather.current_condition[0].lang_de[0].value)
            ```
        """
        if self._session is None:
            self._session = ClientSession(
                timeout=ClientTimeout(total=60, connect=5)
            )
        async with self._session.get(
            f"{self._base_url}/{location}",
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
