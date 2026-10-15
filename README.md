# aiopywttr

[![Downloads](https://static.pepy.tech/badge/aiopywttr)](https://pepy.tech/project/aiopywttr)

Typed asyncio client for the [wttr.in](https://wttr.in) weather API. Without asyncio, use [pywttr](https://github.com/monosans/pywttr).

## Installation

```bash
uv add aiopywttr pywttr-models
# or
pip install -U aiopywttr pywttr-models
```

## Example

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

## Documentation

<https://monosans.github.io/aiopywttr>

## License

[MIT](https://github.com/monosans/aiopywttr/blob/main/LICENSE)
