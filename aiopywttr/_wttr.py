from __future__ import annotations

from typing import Final, Optional

import pywttr_models
from aiohttp import ClientSession, hdrs
from pydantic import AnyHttpUrl, validate_call
from pywttr_models._language import Language  # noqa: PLC2701
from typing_extensions import Literal, Self, final, overload


@final
class Wttr:
    """Asynchronous wrapper for wttr.in weather API.

    Examples:
        Choose language. First option is preferred because of type safety.

        ```python
        language = aiopywttr.Language.ZH_CN
        language = aiopywttr.Language["ZH_CN"]
        language = aiopywttr.Language("zh-cn")
        ```

        Print the average temperature in Paris today:

        ```python
        async with aiopywttr.Wttr() as wttr:
            weather = await wttr.weather("Paris", language=language)
        print(weather.weather[0].avgtemp_c)
        ```

        Custom aiohttp.ClientSession:

        ```python
        async with aiohttp.ClientSession() as session:
            wttr = aiopywttr.Wttr(session=session)
            ...
        ```

        Custom base url:

        ```python
        async with aiopywttr.Wttr(
            base_url=pydantic.AnyHttpUrl("https://example.com")
        ) as wttr:
            ...
        ```
    """

    __slots__ = ("_base_url", "_session")

    @validate_call(config={"arbitrary_types_allowed": True})
    def __init__(
        self,
        *,
        base_url: AnyHttpUrl = AnyHttpUrl.build(scheme="https", host="wttr.in"),  # noqa: B008
        session: Optional[ClientSession] = None,
    ) -> None:
        self._base_url: Final = base_url
        self._session = session

    @property
    def base_url(self) -> AnyHttpUrl:
        return self._base_url

    @property
    def session(self) -> Optional[ClientSession]:
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

    @validate_call
    async def weather(
        self, location: str, /, *, language: Language = Language.EN
    ) -> pywttr_models.AnyModel:
        """Asynchronous wrapper for wttr.in weather API.

        Examples:
            Choose language. First option is preferred because of type safety.

            ```python
            language = aiopywttr.Language.ZH_CN
            language = aiopywttr.Language["ZH_CN"]
            language = aiopywttr.Language("zh-cn")
            ```

            Print the average temperature in Paris today:

            ```python
            async with aiopywttr.Wttr() as wttr:
                weather = await wttr.weather("Paris", language=language)
            print(weather.weather[0].avgtemp_c)
            ```

            Custom base url:

            ```python
            async with aiopywttr.Wttr(
                base_url=pydantic.AnyHttpUrl("https://example.com")
            ) as wttr:
                ...
            ```

            Custom aiohttp.ClientSession:

            ```python
            async with aiohttp.ClientSession() as session:
                wttr = aiopywttr.Wttr(session=session)
                ...
            ```
        """
        if self._session is None:
            self._session = ClientSession()
        async with self._session.get(
            f"{self._base_url}/{location}",
            params={"format": "j1", "lang": language},
            headers={hdrs.ACCEPT: "application/json"},
            raise_for_status=True,
        ) as response:
            await response.read()
        return language._model_.model_validate_json(await response.text())

    async def close(self) -> None:
        """Close HTTP session."""
        if self._session is not None:
            await self._session.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
