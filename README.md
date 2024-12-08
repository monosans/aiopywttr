# aiopywttr

[![CI](https://github.com/monosans/aiopywttr/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/aiopywttr/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/aiopywttr)](https://pepy.tech/project/aiopywttr)

Asynchronous wrapper for [wttr.in](https://wttr.in) weather API.

Synchronous version [here](https://github.com/monosans/pywttr).

## Installation

```bash
pip install -U aiopywttr pywttr-models
```

## Documentation

<https://aiopywttr.readthedocs.io>

## Simple example

```python
async with aiopywttr.Wttr() as wttr:
    weather = await wttr.weather("Paris", language=aiopywttr.Language.EN)
print(weather.weather[0].avgtemp_c)
```

## License

[MIT](https://github.com/monosans/aiopywttr/blob/main/LICENSE)
