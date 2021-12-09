import pytest
import numpy as np
from main import (
    load_data,
    check_position_if_exists,
    evaluate_position,
    find_low_points,
    evaluate_basin,
    find_all_basins,
    find_top_size_basins
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


def test_find_basins():
    array = np.array(SAMPLE_DATA)
    blocked_positions_array = np.zeros(array.shape)
    _, size = evaluate_basin(
        array,
        blocked_positions_array,
        0,
        1
    )
    assert size == 3


def test_find_all_basins():
    assert sorted(find_all_basins(SAMPLE_DATA)) == sorted(
        [3, 9, 14, 9]
    )


def test_find_top_size_basins():
    assert find_top_size_basins(SAMPLE_DATA) == 1134
