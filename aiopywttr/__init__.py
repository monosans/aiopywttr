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
from __future__ import annotations

import pywttr_models as models
from pywttr_models._language import Language

from ._get_weather import get_weather
from ._wttr import Wttr, WttrClassDeprecationWarning

__all__ = (
    "models",
    "Language",
    "get_weather",
    "Wttr",
    "WttrClassDeprecationWarning",
)
