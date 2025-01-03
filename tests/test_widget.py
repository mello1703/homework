import pytest

from src.masks import get_mask_card_number
from src.widget import get_data, get_mask_account, mask_account_card

"""Параметризация функции get_mask_account"""


@pytest.mark.parametrize("value, expected", [
    ("Счет 35383033474447895560", "Счет **5560"),
])
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.fixture
def date() -> str:
    return "2018-07-11T02:26:18.671407"


"""Тесты для функции get_data"""


def test_get_data(date: str) -> None:
    assert get_data(date) == "11.07.2018"


"""Тесты для функции mask_account_card"""


@pytest.mark.parametrize("value, expected", [
    ("7158300734726758", "7158 30** **** 6758"),
    ("7158300734726759", "7158 30** **** 6759"),
])
def test_get_mask_card_number(value: str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("12345678901234567340", "**7340"),
    ("12345678901234567890", "**7890"),
])
def test_get_mask_account(value: str, expected: str) -> None:
    assert get_mask_account(value) == expected
