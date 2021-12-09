from typing import List, Tuple
import numpy as np


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
    x_limit = len(height_map)
    if x_limit > 0:
        y_limit = len(height_map[0])
        if 0 <= selected_position_x < x_limit:
            if 0 <= selected_position_y < y_limit:
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


def evaluate_basin(
        height_map: np.array,
        blocked_positions_array: np.array,
        current_position_x: int,
        current_position_y: int,
        current_size: int = 0
) -> Tuple[np.array, int]:
    if height_map[current_position_x][current_position_y] != 9 and \
            blocked_positions_array[current_position_x][
                current_position_y] == 0:
        current_size += 1
        blocked_positions_array[current_position_x][current_position_y] = 1
        # top
        if 0 <= current_position_x - 1 < height_map.shape[0]:
            blocked_positions_array, current_size = evaluate_basin(
                height_map,
                blocked_positions_array,
                current_position_x - 1,
                current_position_y,
                current_size
            )
        # bottom
        if 0 <= current_position_x + 1 < height_map.shape[0]:
            blocked_positions_array, current_size = evaluate_basin(
                height_map,
                blocked_positions_array,
                current_position_x + 1,
                current_position_y,
                current_size
            )
        # right
        if 0 <= current_position_y - 1 < height_map.shape[1]:
            blocked_positions_array, current_size = evaluate_basin(
                height_map,
                blocked_positions_array,
                current_position_x,
                current_position_y - 1,
                current_size
            )
        # left
        if 0 <= current_position_y + 1 < height_map.shape[1]:
            blocked_positions_array, current_size = evaluate_basin(
                height_map,
                blocked_positions_array,
                current_position_x,
                current_position_y + 1,
                current_size
            )
    return blocked_positions_array, current_size


def find_all_basins(height_map: List) -> List[int]:
    res = []
    array = np.array(height_map)
    blocked_positions_array = np.zeros(array.shape)
    for ix in range(array.shape[0]):
        for iy in range(array.shape[1]):
            if blocked_positions_array[ix][iy] == 0:
                blocked_positions_array, current_size = evaluate_basin(
                    array,
                    blocked_positions_array,
                    ix,
                    iy
                )
                if current_size > 0:
                    res.append(current_size)
    return res


def find_top_size_basins(height_map: List) -> int:
    all_basins = sorted(find_all_basins(height_map), reverse=True)
    res = 1
    for x in range(min(3, len(all_basins))):
        res *= all_basins[x]
    return res


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Low points Test: '
          f'{find_low_points(test_data)}')
    print(f'Low points Submission: '
          f'{find_low_points(submission_data)}')
    print(f'Basins Test: '
          f'{find_top_size_basins(test_data)}')
    print(f'Basins Submission: '
          f'{find_top_size_basins(submission_data)}')