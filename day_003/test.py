import pytest

from main import (
    load_data,
    binary_to_decimal,
    calculate_most_common_on_position,
    calculate_gamma,
    calculate_power_consumption_base,
    calulate_oxygen_and_co_ratings,
    calculate_life_support_rating
)

SAMPLE_DATA = load_data('test.txt')


def test_binary_to_decimal_transformation():
    assert binary_to_decimal("10110") == 22
    assert binary_to_decimal("01001") == 9
    assert binary_to_decimal("1001111") == 79


def test_most_common_position():
    assert calculate_most_common_on_position(
        SAMPLE_DATA,
        0
    ) == 1


def test_least_common_position():
    assert calculate_most_common_on_position(
        SAMPLE_DATA,
        0,
        True
    ) == 0


def test_gamma():
    assert calculate_gamma(SAMPLE_DATA) == 22


def test_epsilon():
    assert calculate_gamma(SAMPLE_DATA, True) == 9


def test_power_consumption_base():
    assert calculate_power_consumption_base(SAMPLE_DATA) == 198


def test_oxygen_rating():
    assert calulate_oxygen_and_co_ratings(SAMPLE_DATA) == 23


def test_co2_rating():
    assert calulate_oxygen_and_co_ratings(SAMPLE_DATA, calculate_co=True) == 10


def test_life_support_rating():
    assert calculate_life_support_rating(SAMPLE_DATA) == 230
