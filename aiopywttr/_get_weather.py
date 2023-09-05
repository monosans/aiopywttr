from __future__ import annotations

from typing import Optional

import pywttr_models
from aiohttp import ClientSession
from pywttr_models._language import Language
from typing_extensions import Literal, overload

from ._http import get_json


@overload
async def get_weather(
    location: str,
    language: Literal[Language.AF],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.af.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.AM],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.am.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.AR],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.ar.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.BE],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.be.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.BN],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.bn.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.CA],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.ca.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.DA],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.da.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.DE],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.de.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.EL],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.el.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.EN] = ...,
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.en.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.ET],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.et.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.FA],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.fa.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.FR],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.fr.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.GL],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.gl.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.HI],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.hi.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.HU],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.hu.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.IA],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.ia.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.ID],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.id.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.IT],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.it.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.LT],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.lt.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.MG],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.mg.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.NB],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.nb.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.NL],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.nl.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.OC],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.oc.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.PL],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.pl.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.PT_BR],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.pt_br.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.RO],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.ro.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.RU],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.ru.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.TA],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.ta.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.TH],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.th.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.TR],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.tr.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.UK],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.uk.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.VI],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.vi.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.ZH_CN],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.zh_cn.Model:
    ...


@overload
async def get_weather(
    location: str,
    language: Literal[Language.ZH_TW],
    *,
    session: Optional[ClientSession] = ...,
) -> pywttr_models.zh_tw.Model:
    ...


@overload
async def get_weather(
    location: str, language: Language, *, session: Optional[ClientSession] = ...
) -> pywttr_models.AnyModel:
    ...


async def get_weather(
    location: str,
    language: Language = Language.EN,
    *,
    session: Optional[ClientSession] = None,
) -> pywttr_models.AnyModel:
    """Asynchronous wrapper for wttr.in weather API.

    Examples:
        Prints the average temperature in Paris today:

        ```python
        import asyncio

        import aiopywttr


        async def main():
            # Choose language. First option is preferred for typing.
            language = aiopywttr.Language.ZH_CN
            language = aiopywttr.Language["ZH_CN"]
            language = aiopywttr.Language("zh-cn")
            weather = await aiopywttr.get_weather("Paris", language)
            print(weather.weather[0].avgtemp_c)


        asyncio.run(main())
        ```
    """
    try:
        model = language._model_
        lang = language._value_
    except AttributeError as e:
        msg = (
            f"Invalid language {language!r}. "
            "Must be a member of aiopywttr.Language enum."
        )
        raise TypeError(msg) from e
    response = await get_json(location, lang, session)
    return model.parse_obj(response)
