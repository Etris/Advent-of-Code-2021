import pytest
from main import (
    load_data,
    check_single_pattern,
    check_all_patterns,
    check_all_horizontals,
    check_all_verticals,
    get_sum_of_all_unmarked,
    make_all_bingo_movements
)

SAMPLE_BINGO = [
    [
        22, 13, 17, 11, 0
    ],
    [
        8, 2, 23, 4, 24
    ],
    [
        21, 9, 14, 16, 7
    ],
    [
        6, 10, 3, 18, 5
    ],
    [
        1, 12, 20, 15, 19
    ]
]

SAMPLE_BINGO_LAST = [
    [
        14, 21, 17, 24, 4
    ],
    [
        10, 16, 15, 9, 19
    ],
    [
        18, 8, 23, 26, 20
    ],
    [
        22, 11, 13, 6, 5
    ],
    [
        2, 0, 12, 3, 7
    ]
]


def test_data_load_len_of_input():
    chosen_numbers, bingo_list = load_data('test.txt')
    assert len(chosen_numbers) == 27


def test_data_load_numbers_of_input():
    chosen_numbers, bingo_list = load_data('test.txt')
    assert chosen_numbers == [
        7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12,
        22, 18, 20, 8, 19, 3, 26, 1
    ]


def test_verify_first_bingo_card_numerical():
    chosen_numbers, bingo_list = load_data('test.txt')
    assert bingo_list[0] == SAMPLE_BINGO


def test_verify_last_bingo_card_numerical():
    chosen_numbers, bingo_list = load_data('test.txt')
    assert bingo_list[-1] == SAMPLE_BINGO_LAST


def test_check_single_pattern_positive():
    assert check_single_pattern(
        list_of_previously_chosen_numbers=[22, 21, 23, 0, 17, 10, 11, 12, 13],
        current_line=[22, 13, 17, 11, 0]
    ) is True


def test_check_single_pattern_negative():
    assert check_single_pattern(
        list_of_previously_chosen_numbers=[22, 21, 23, 0, 17, 10],
        current_line=[22, 13, 17, 11, 0]
    ) is False


def test_horizontal_pattern_positive():
    result_status = check_all_horizontals(
        [22, 13, 17, 11, 4, 0],
        SAMPLE_BINGO
    )
    assert result_status is True


def test_horizontal_pattern_negative():
    result_status = check_all_horizontals(
        [10, 11, 16],
        SAMPLE_BINGO
    )
    assert result_status is False


def test_vertical_pattern_positive():
    result_status = check_all_verticals(
        [9, 8, 24, 7, 6, 5, 19, 0],
        SAMPLE_BINGO
    )
    assert result_status is True


def test_vertical_pattern_negative():
    result_status = check_all_verticals(
        [2, 1, 3],
        SAMPLE_BINGO
    )
    assert result_status is False


def test_all_patterns_positive():
    assert check_all_patterns(
        [9, 8, 24, 7, 6, 5, 19, 0],
        SAMPLE_BINGO
    ) is True


def test_all_patterns_negative():
    assert check_all_patterns(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],
        SAMPLE_BINGO
    ) is False


def test_all_patterns_real_use_case_positive():
    chosen_numbers, bingo_list = load_data('test.txt')
    assert check_all_patterns(
        chosen_numbers,
        bingo_list[-1]
    )


def test_get_sum_of_unmarked():
    assert get_sum_of_all_unmarked(
        [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24],
        SAMPLE_BINGO_LAST
    ) == 188


def test_validate_main_loop():
    chosen_numbers, bingo_list = load_data('test.txt')
    assert make_all_bingo_movements(
        chosen_numbers,
        bingo_list
    ) == 4512
