# aiopywttr

[![CI](https://github.com/monosans/aiopywttr/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopywttr/actions/workflows/ci.yml?query=event%3Apush+branch%3Amain)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/aiopywttr/main.svg)](https://results.pre-commit.ci/latest/github/monosans/aiopywttr/main)
[![Coverage](https://img.shields.io/codecov/c/github/monosans/aiopywttr/main?logo=codecov)](https://codecov.io/gh/monosans/aiopywttr)
[![PyPI Downloads](https://img.shields.io/pypi/dm/aiopywttr?logo=pypi)](https://pypi.org/project/aiopywttr/)

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
