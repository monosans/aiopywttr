# aiopywttr

[![CI](https://github.com/monosans/aiopywttr/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/aiopywttr/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/aiopywttr)](https://pepy.tech/project/aiopywttr)

Asynchronous wrapper for [wttr.in](https://wttr.in) weather forecast API.

Synchronous version [here](https://github.com/monosans/pywttr).

## Installation

```bash
python -m pip install -U aiopywttr pywttr-models
```

## Example

This example prints the average temperature in New York today.

```python
import asyncio

import aiopywttr


async def main():
    wttr = aiopywttr.Wttr("New York")
    forecast = await wttr.en()
    print(forecast.weather[0].avgtemp_c)


asyncio.run(main())
```

Other languages may also be used instead of `en`. For a complete list of supported languages, follow the code completion in your IDE.

## Documentation

There is no documentation, just follow the example and code completion in your IDE.

All types of objects returned by the wttr.in API are in the `aiopywttr.models` package.

## Recommended IDEs

- [Visual Studio Code](https://code.visualstudio.com) (with [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python))
- [PyCharm](https://jetbrains.com/pycharm)

## License

[MIT](https://github.com/monosans/aiopywttr/blob/main/LICENSE)
