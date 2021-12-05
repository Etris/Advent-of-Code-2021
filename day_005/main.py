from typing import Tuple, List


def load_data(file_path: str) -> List:
    result_list = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            left_part, right_part = line.strip().split('->')
            left_part = [int(x) for x in str(left_part).strip().split(',')]
            right_part = [int(x) for x in str(right_part).strip().split(',')]
            result_list.append(
                [left_part, right_part]
            )
    return result_list


def find_min_and_max_coordinates(loaded_data: List) -> Tuple[List, List]:
    if len(loaded_data) > 0:
        point_max = [0, 0]
        for row in loaded_data:
            start_pos = row[0]
            last_pos = row[1]
            # x position
            if start_pos[0] > point_max[0] or last_pos[0] > point_max[0]:
                if start_pos[0] > last_pos[0]:
                    point_max[0] = start_pos[0]
                else:
                    point_max[0] = last_pos[0]
            # y position
            if start_pos[1] > point_max[1] or last_pos[1] > point_max[1]:
                if start_pos[1] > last_pos[1]:
                    point_max[1] = start_pos[1]
                else:
                    point_max[1] = last_pos[1]
        return [0, 0], point_max
    else:
        raise ValueError('Input list is empty')


def check_if_horizontal_or_verical_allowed(
        current_vent_line: List
) -> Tuple[bool, str]:
    if current_vent_line[0][0] == current_vent_line[1][0]:
        return True, 'vertical'
    elif current_vent_line[0][1] == current_vent_line[1][1]:
        return True, 'horizontal'
    else:
        return False, ''


def draw_empty_schema(starting_point: List, finish_point: List) -> List[List]:
    empty_schema = [
        [
            0 for iy in range(starting_point[1], finish_point[1] + 1)
        ] for ix in range(starting_point[0], finish_point[0] + 1)
    ]
    return empty_schema


def make_drawing_iteration(
    current_vent_line: List,
    current_vent_type: str,
    current_schema: List
) -> List:
    working_schema = current_schema.copy()
    if current_vent_type == 'horizontal':
        for ix in range(
          min(current_vent_line[0][0], current_vent_line[1][0]),
          max(current_vent_line[0][0]+1, current_vent_line[1][0]+1)
        ):
            working_schema[ix][current_vent_line[0][1]] += 1
        return working_schema
    elif current_vent_type == 'vertical':
        for ix in range(
                min(current_vent_line[0][1], current_vent_line[1][1]),
                max(current_vent_line[0][1]+1, current_vent_line[1][1] + 1)
        ):
            working_schema[current_vent_line[0][0]][ix] += 1
        return working_schema
    else:
        raise ValueError("Unknown type of vent")


def return_number_of_fields_equal_to_two_or_greater(
        current_schema: List
) -> int:
    result = 0
    for ix in range(len(current_schema)):
        for iy in range(len(current_schema[ix])):
            if current_schema[ix][iy] > 1:
                result += 1
    return result


def first_part_loop(list_of_all_vents: List) -> int:
    min_point, max_point = find_min_and_max_coordinates(list_of_all_vents)
    current_schema = draw_empty_schema(
        min_point, max_point
    )
    for vent in list_of_all_vents:
        status, type_of = check_if_horizontal_or_verical_allowed(vent)
        if status:
            current_schema = make_drawing_iteration(
                vent,
                type_of,
                current_schema
            )
    return return_number_of_fields_equal_to_two_or_greater(
        current_schema
    )


if __name__ == '__main__':
    test_vents = load_data("test.txt")
    submission_vents = load_data("submission.txt")
    print(f'Test_1: '
          f'{first_part_loop(test_vents)}')
    print(f'Task_1: '
          f'{first_part_loop(submission_vents)}')