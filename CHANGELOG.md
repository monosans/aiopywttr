# Changelog

We follow [Semantic Versioning](https://semver.org/).

## [0.1.3] - 2022-01-26

- Use `parse_obj` method for models.
- Automatically call `raise_for_status`.
- Check if session is not closed.

## [0.1.2] - 2022-01-02

- Raise `ClientResponseError` if status_code >= 400.

## [0.1.1] - 2021-12-12

- Initial release.
