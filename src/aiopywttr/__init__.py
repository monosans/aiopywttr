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
    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=60, connect=5)
    ) as session:
        wttr = aiopywttr.Wttr(session=session)
        ...
    ```
"""

from __future__ import annotations

from importlib.metadata import version as _version

import pywttr_models as models
from pywttr_models._language import Language  # noqa: PLC2701

from aiopywttr._wttr import Wttr

__version__ = _version(__name__)
__all__ = ("Language", "Wttr", "models")
