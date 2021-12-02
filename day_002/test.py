import pytest

from main import move_ship, move_ship_with_aim, load_data

SAMPLE_DATA = load_data('test.txt')


def test_first_part():
    horizontal, depth = move_ship(SAMPLE_DATA)
    assert horizontal == 15
    assert depth == 10


def test_second_part():
    horizontal, depth = move_ship_with_aim(SAMPLE_DATA)
    assert horizontal == 15
    assert depth == 60


def test_check_if_error_will_be_thrown_if_new_unknown_position_added():
    with pytest.raises(ValueError):
        tmp_data = SAMPLE_DATA.copy()
        tmp_data.append(
            {
                'direction': "XD",
                'scale': -1
            }
        )
        move_ship(tmp_data)
