from __future__ import annotations

import pytest

import aiopywttr


def test_language() -> None:
    assert (
        aiopywttr.Language.ZH_CN
        is aiopywttr.Language["ZH_CN"]
        is aiopywttr.Language("zh-cn")
    )


def test_language_model() -> None:
    assert aiopywttr.Language.EN._model_ is aiopywttr.models.en.Model


@pytest.mark.parametrize("lang", aiopywttr.Language)
def test_str(lang: aiopywttr.Language) -> None:
    assert lang._value_ == str(lang)
