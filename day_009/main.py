from typing import List, Dict


def load_data(file_path: str) -> List[List[int]]:
    with open(file_path, 'r') as file:
        main_frame = []
        for line in file.readlines():
            main_frame.append(
                [int(x) for x in line.strip().replace("\n", '')]
            )
        return main_frame


def check_position_if_exists(
        height_map: List,
        selected_position_x: int,
        selected_position_y: int,
        current_value: int
) -> bool:
    print(selected_position_x, selected_position_y)
    x_limit = len(height_map)
    if x_limit > 0:
        y_limit = len(height_map[0])
        if 0 <= selected_position_x < x_limit:
            if 0 <= selected_position_y < y_limit:
                print(height_map[selected_position_x][selected_position_y])
                if (
                    current_value >=
                    height_map[selected_position_x][selected_position_y]
                ):
                    return False
        return True
    else:
        raise ValueError("Height map is empty")


def evaluate_position(
        height_map: List,
        current_position_x: int,
        current_position_y: int
) -> bool:
    current_value = height_map[current_position_x][current_position_y]
    print(f"CURRENT EVAL: {current_value}")
    status_list = [
        check_position_if_exists(
            height_map,
            current_position_x - 1,
            current_position_y,
            current_value
        ),
        check_position_if_exists(
            height_map,
            current_position_x + 1,
            current_position_y,
            current_value
        ),
        check_position_if_exists(
            height_map,
            current_position_x,
            current_position_y - 1,
            current_value
        ),
        check_position_if_exists(
            height_map,
            current_position_x,
            current_position_y + 1,
            current_value
        )
    ]
    if all(status_list):
        return True
    else:
        return False


def find_low_points(height_map: List) -> int:
    current_score = 0
    for ix in range(len(height_map)):
        for iy in range(len(height_map[ix])):
            if evaluate_position(
                height_map,
                ix,
                iy
            ):
                current_score += (1 + height_map[ix][iy])
    return current_score


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Test 1: '
          f'{find_low_points(test_data)}')
    print(f'Submission 1: '
          f'{find_low_points(submission_data)}')
