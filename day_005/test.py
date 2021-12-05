import pytest
from main import (
    load_data,
    find_min_and_max_coordinates,
    check_if_horizontal_or_verical_allowed,
    draw_empty_schema,
    make_drawing_iteration,
    return_number_of_fields_equal_to_two_or_greater,
    first_part_loop
)


def test_load_data_length():
    assert len(load_data('test.txt')) == 10


def test_load_data_verify_example():
    loaded_data = load_data('test.txt')
    assert loaded_data[0] == [[0, 9], [5, 9]]


def test_verify_min_max_points():
    loaded_data = load_data('test.txt')
    point_min, point_max = find_min_and_max_coordinates(loaded_data)
    assert point_min == [0, 0]
    assert point_max == [9, 9]


def test_verify_min_max_points_empty_list():
    with pytest.raises(ValueError):
        find_min_and_max_coordinates([])


def test_if_horizontal_or_vertical_line_can_be_created():
    can_be_created, type_of_line = check_if_horizontal_or_verical_allowed(
        [[3, 0], [3, 2]]
    )
    assert can_be_created is True
    assert type_of_line == 'vertical'
    can_be_created, type_of_line = check_if_horizontal_or_verical_allowed(
        [[1, 2], [3, 2]]
    )
    assert can_be_created is True
    assert type_of_line == 'horizontal'
    can_be_created, type_of_line = check_if_horizontal_or_verical_allowed(
        [[1, 2], [3, 4]]
    )
    assert can_be_created is False
    assert type_of_line == ''


def test_make_single_iteration():
    can_be_created, type_of_line = check_if_horizontal_or_verical_allowed(
        [[1, 1], [1, 3]]
    )
    assert can_be_created is True
    schema = make_drawing_iteration(
        [[1, 1], [1, 3]],
        type_of_line,
        draw_empty_schema([0, 0], [5, 5])
    )
    assert schema[1][1] == 1
    assert schema[1][2] == 1
    assert schema[1][3] == 1


def test_if_number_of_crosses_is_correctly_estimated():
    assert return_number_of_fields_equal_to_two_or_greater(
        [
            [0, 0, 1, 0, 1],
            [0, 0, 2, 1, 2],
            [2, 1, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [2, 1, 1, 1, 1]
        ]
    ) == 5


def test_verify_first_part_loop_result():
    loaded_data = load_data('test.txt')
    assert first_part_loop(loaded_data) == 5
