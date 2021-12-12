# aiopywttr

[![Build Status](https://github.com/monosans/aiopywttr/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopywttr/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/aiopywttr/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiopywttr)
[![Python Version](https://img.shields.io/pypi/pyversions/aiopywttr.svg)](https://pypi.org/project/aiopywttr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/monosans/aiopywttr/blob/main/LICENSE)

Asynchronous wrapper for [wttr.in](https://wttr.in) weather forecast.

Synchronous version [here](https://github.com/monosans/pywttr).

## Installation

```bash
pip install aiopywttr
```

## Example

This example prints the average temperature in New York today.

```python
import asyncio

import aiopywttr


async def main():
    forecast = await aiopywttr.en.get_forecast("New York")
    print(forecast.weather[0].avgtemp_c)


asyncio.run(main())
```

Other languages may also be used instead of `en`. For a complete list of supported languages, see the [file names](https://github.com/monosans/aiopywttr/tree/main/aiopywttr) or follow the code completion in your IDE.

## Documentation

There is no documentation, just follow the code completion from your IDE. I'd recommend [Visual Studio Code](https://code.visualstudio.com) (with [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)) or [PyCharm](https://jetbrains.com/pycharm).
