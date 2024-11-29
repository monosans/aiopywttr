from __future__ import annotations

import pytest

import aiopywttr


@pytest.mark.parametrize("language", aiopywttr.Language)
def test_language_value(language: aiopywttr.Language) -> None:
    assert language._name_ == language._value_.replace("-", "_").upper()


@pytest.mark.parametrize("language", aiopywttr.Language)
def test_language_model(language: aiopywttr.Language) -> None:
    assert (
        language._model_
        is getattr(aiopywttr.models, language._name_.lower()).Model
    )


def test_language_str() -> None:
    assert aiopywttr.Language.EN._value_ == str(aiopywttr.Language.EN)
