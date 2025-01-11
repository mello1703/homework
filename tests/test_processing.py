import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import (
    info_dict_ident_dates_sort,
    info_dict_sort_res_false,
    info_dict_sort_res_true,
    info_dict_sorted_1,
    info_dict_sorted_2
)


@pytest.fixture
def info_dict_fixture() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def info_dict_ident_dates_fixture() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 88828829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


"""Тесты для функции filter_by_state"""


def test_filter_by_state_basic(info_dict_fixture: list) -> None:
    """Тест на срабатывание функции со списком словарей list_of_dict по дефолтным условиям"""
    assert filter_by_state(info_dict_fixture) == info_dict_sorted_1


def test_filter_by_state_with_state_arg_canceled(info_dict_fixture: list) -> None:
    """Тест на срабатывание функции со списком словарей, где state = 'CANCELED'"""
    assert filter_by_state(info_dict_fixture, state_id="CANCELED") == info_dict_sorted_2


"""Тесты для функции sort_by_date"""


def test_sort_by_date_basic(info_dict_fixture: list) -> None:
    """Тестирование сортировки списка словарей в порядке убывания."""
    assert sort_by_date(info_dict_fixture) == info_dict_sort_res_true


def test_sort_by_date_rev_false(info_dict_fixture: list) -> None:
    """Тестирование сортировки списка словарей по датам в порядке возрастания."""
    assert sort_by_date(info_dict_fixture, reverse=False) == info_dict_sort_res_false


def test_sort_by_date_ident_dates(info_dict_ident_dates_fixture: list) -> None:
    """Проверка корректности сортировки при одинаковых датах"""
    assert sort_by_date(info_dict_ident_dates_fixture) == info_dict_ident_dates_sort
