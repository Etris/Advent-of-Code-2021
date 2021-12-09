import pytest
from main import (
    load_data,
    check_position_if_exists,
    evaluate_position,
    find_low_points
)

SAMPLE_DATA = load_data('test.txt')


def test_check_position_if_exists():
    x_pos = 0
    y_pos = 1
    # check top position
    assert check_position_if_exists(
        SAMPLE_DATA,
        x_pos - 1,
        y_pos,
        SAMPLE_DATA[x_pos][y_pos]
    )
    # left
    assert check_position_if_exists(
        SAMPLE_DATA,
        x_pos,
        y_pos - 1,
        SAMPLE_DATA[x_pos][y_pos]
    )
    # right
    assert check_position_if_exists(
        SAMPLE_DATA,
        x_pos,
        y_pos + 1,
        SAMPLE_DATA[x_pos][y_pos]
    )
    # bottom
    assert check_position_if_exists(
        SAMPLE_DATA,
        x_pos + 1,
        y_pos,
        SAMPLE_DATA[x_pos][y_pos]
    )


def test_evaluate_position():
    assert evaluate_position(
        SAMPLE_DATA, 0, 1
    )
    assert evaluate_position(
        SAMPLE_DATA, 0, 9
    )
    assert evaluate_position(
        SAMPLE_DATA, 2, 2
    )
    assert evaluate_position(
        SAMPLE_DATA, 4, 6
    )
    assert evaluate_position(
        SAMPLE_DATA, 3, 5
    ) is False
    assert evaluate_position(
        SAMPLE_DATA, 4, 7
    ) is False


def test_find_low_points():
    assert find_low_points(SAMPLE_DATA) == 15
