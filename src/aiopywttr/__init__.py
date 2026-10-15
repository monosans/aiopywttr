"""Asynchronous wrapper for the [wttr.in](https://wttr.in) weather API.

Examples:
    ```python
    import asyncio

    import aiopywttr


    async def main() -> None:
        async with aiopywttr.Wttr() as wttr:
            weather = await wttr.weather("Paris")
        print(weather.current_condition[0].temp_c)


    asyncio.run(main())
    ```
"""

from __future__ import annotations

import pywttr_models as models
from pywttr_models._language import Language  # noqa: PLC2701

from aiopywttr._wttr import Wttr

__version__ = "3.0.7"
__all__ = ("Language", "Wttr", "models")
