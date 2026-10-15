# aiopywttr

Typed asyncio client for the [wttr.in](https://wttr.in) weather API. Without asyncio, use [pywttr](https://monosans.github.io/pywttr).

## Installation

=== "uv"

    ```bash
    uv add aiopywttr pywttr-models
    ```

=== "pip"

    ```bash
    pip install -U aiopywttr pywttr-models
    ```

## Quick start

```python
import asyncio

import aiopywttr


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Paris")

    now = weather.current_condition[0]
    print(f"{now.temp_c} °C, {now.weather_desc[0].value}")


asyncio.run(main())
```

## Next steps

- [Guide](guide.md): current weather, forecasts, languages, timeouts, errors.
- [API reference](api.md): every class, method and response field.
