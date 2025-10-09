# Changelog

[Semantic Versioning](https://semver.org/)

## [3.0.2] - 2025-10-09

- Improve JSON parsing performance.

## [3.0.1] - 2024-12-12

- Add stricter default request timeout.

## [3.0.0] - 2024-12-08

- New context manager based API focusing on correct and performant HTTP session management.
- Switch to Pydantic v2. This also improves performance.
- Previously all model fields were strings, now some are int or float.

## [2.3.0] - 2023-09-05

- Raise the minimum required version of Python from 3.7 to 3.8.
- Add a new more flexible and simpler API consisting of `aiopywttr.get_weather` function and `aiopywttr.Language` enum. The old `aiopywttr.Wttr` API still works, but is marked deprecated.

## [2.2.2] - 2023-07-08

- Lower minimum required Python version from 3.7.2 to 3.7.

## [2.2.1] - 2023-07-06

- Add documentation.

## [2.2.0] - 2023-04-22

- Reexport models from pywttr-models.

## [2.1.0] - 2022-11-26

- Add support for Galician language.

## [2.0.2] - 2022-11-26

- Allow keyword-only arguments of public methods to be positional.

## [2.0.1] - 2022-08-15

- Raise minimum required Python version from 3.7 to 3.7.2.
- Add docstring to `__init__.py`.
- Add `from __future__ import annotations` to all modules.
- Use relative imports.

## [2.0.0] - 2022-06-13

- Remove unsupported languages.

## [1.0.2] - 2022-06-03

- Update dependencies.

## [1.0.1] - 2022-04-16

- Use `__slots__`.

## [1.0.0] - 2022-02-21

- Rewrite everything.

## [0.1.3] - 2022-01-26

- Use `parse_obj` method for models.
- Automatically call `raise_for_status`.
- Check if session is not closed.

## [0.1.2] - 2022-01-02

- Raise `ClientResponseError` if status_code >= 400.

## [0.1.1] - 2021-12-12

- Initial release.
