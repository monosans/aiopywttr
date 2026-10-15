# Guide

Every example is a complete script: copy it and run it.

## What's in a response

[`Wttr.weather`][aiopywttr.Wttr.weather] returns a [`Model`][aiopywttr.models.base.Model]:

- `current_condition[0]`: the weather now ([`CurrentConditionItem`][aiopywttr.models.base.CurrentConditionItem]).
- `weather[0]` to `weather[2]`: today, tomorrow and the day after ([`WeatherItem`][aiopywttr.models.base.WeatherItem]).
- `weather[i].hourly`: that day in 3-hour steps ([`HourlyItem`][aiopywttr.models.base.HourlyItem]).
- `weather[i].astronomy[0]`: sunrise, sunset and the moon ([`AstronomyItem`][aiopywttr.models.base.AstronomyItem]).
- `nearest_area[0]`: the place wttr.in found ([`NearestAreaItem`][aiopywttr.models.base.NearestAreaItem]).

Most values come in metric and imperial units, e.g. `temp_c` and `temp_f`.

## Current weather

```python
import asyncio

import aiopywttr


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("London")

    now = weather.current_condition[0]
    print(f"{now.temp_c} °C, feels like {now.feels_like_c} °C")
    print(now.weather_desc[0].value)
    print(f"Wind {now.windspeed_kmph} km/h {now.winddir16_point}")


asyncio.run(main())
```

## Forecast for tomorrow

`weather[1]` is tomorrow, `weather[2]` is the day after.

```python
import asyncio

import aiopywttr


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Tokyo")

    tomorrow = weather.weather[1]
    print(tomorrow.date, f"{tomorrow.mintemp_c}..{tomorrow.maxtemp_c} °C")
    print("Sunrise:", tomorrow.astronomy[0].sunrise)


asyncio.run(main())
```

## Hourly forecast

`hourly` has 8 items, from 00:00 to 21:00 local time. [`time`][aiopywttr.models.base.HourlyItem.time] is a number: `0`, `300`, ..., `2100`.

```python
import asyncio

import aiopywttr


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Berlin")

    for hour in weather.weather[0].hourly:
        time = f"{hour.time // 100:02}:00"
        print(time, f"{hour.temp_c} °C", f"rain {hour.chanceofrain}%")


asyncio.run(main())
```

## Several locations

wttr.in accepts cities, coordinates, airport codes and landmarks after `~`. Reuse one [`Wttr`][aiopywttr.Wttr] for many requests and run them concurrently.

```python
import asyncio

import aiopywttr

locations = ["Paris", "48.8567,2.3508", "CDG", "~Eiffel Tower"]


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        requests = [wttr.weather(location) for location in locations]
        weathers = await asyncio.gather(*requests)

    for location, weather in zip(locations, weathers, strict=True):
        area = weather.nearest_area[0]
        print(location, "->", area.area_name[0].value, area.country[0].value)


asyncio.run(main())
```

## Weather in another language

Pass a [`Language`][aiopywttr.Language]. The translated description is in `lang_<code>`, e.g. `lang_fr`; `weather_desc` stays in English.

```python
import asyncio

import aiopywttr


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        weather = await wttr.weather("Paris", language=aiopywttr.Language.FR)

    now = weather.current_condition[0]
    print(now.lang_fr[0].value)
    print(now.weather_desc[0].value)


asyncio.run(main())
```

If the language is only known at runtime, e.g. `aiopywttr.Language("fr")`, read [`lang_xx`](api.md#response-models): every language has it.

## Custom HTTP client and timeouts

Pass your own [`aiohttp.ClientSession`][aiohttp.ClientSession] to change timeouts, proxies or headers. The default session has a 60 s total timeout (5 s to connect).

```python
import asyncio

import aiohttp
import aiopywttr


async def main() -> None:
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        wttr = aiopywttr.Wttr(session=session)
        weather = await wttr.weather("Oslo")

    print(weather.current_condition[0].temp_c)


asyncio.run(main())
```

!!! warning

    [`Wttr.close`][aiopywttr.Wttr.close] closes the session you passed, and leaving `async with aiopywttr.Wttr(...)` calls it.

## Self-hosted wttr.in

Point `base_url` at your own [wttr.in server](https://github.com/chubin/wttr.in#installation).

```python
import asyncio

import aiopywttr
import pydantic

base_url = pydantic.AnyHttpUrl("https://wttr.example.com")


async def main() -> None:
    async with aiopywttr.Wttr(base_url=base_url) as wttr:
        weather = await wttr.weather("Paris")

    print(weather.current_condition[0].temp_c)


asyncio.run(main())
```

## Handling errors

wttr.in answers an unknown location with an error status, which raises [`aiohttp.ClientResponseError`][aiohttp.ClientResponseError]. Network errors raise other [`aiohttp.ClientError`][aiohttp.ClientError] subclasses, and timeouts raise [`TimeoutError`][TimeoutError].

```python
import asyncio

import aiohttp
import aiopywttr


async def main() -> None:
    async with aiopywttr.Wttr() as wttr:
        try:
            weather = await wttr.weather("qwertyuiopasdf")
        except aiohttp.ClientResponseError as e:
            print("wttr.in error:", e.status)
        except (aiohttp.ClientError, TimeoutError) as e:
            print("Network error:", e)
        else:
            print(weather.current_condition[0].temp_c)


asyncio.run(main())
```
