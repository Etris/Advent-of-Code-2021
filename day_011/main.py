from typing import List, Tuple
import numpy as np

FLASH_MAPPING = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 0}


def load_data(file_path: str) -> np.array:
    with open(file_path, 'r') as file:
        input_state_data = []
        for line in file.readlines():
            input_state_data.append(
                [int(x) for x in line.replace('\n', '')]
            )
        return np.array(input_state_data)


def try_to_flash(
        current_array: np.array,
        can_flash: np.array,
        x: int,
        y: int
) -> Tuple[np.array, np.array, int]:
    number_of_flashes = 0
    if current_array[x][y] > 9 and can_flash[x][y] == 0:
        can_flash[x][y] = 1
        number_of_flashes += 1
        current_array[x][y] = 0
        for sub_x in range(max(0, x - 1),
                           min(x + 2, len(current_array))):
            for sub_y in range(max(0, y - 1),
                               min(y + 2, len(current_array))):
                if sub_x == x and sub_y == y:
                    continue
                if can_flash[sub_x][sub_y] == 0:
                    current_array[sub_x][sub_y] += 1
                current_array, can_flash, flashes = try_to_flash(
                    current_array,
                    can_flash,
                    sub_x,
                    sub_y
                )
                number_of_flashes += flashes
    return current_array, can_flash, number_of_flashes


def make_iteration(current_array: np.array) -> Tuple[np.array, np.array, int]:
    flash_counter = 0
    empty_flashes = np.zeros(current_array.shape)
    for x in range(len(current_array)):
        for y in range(len(current_array[x])):
            if empty_flashes[x][y] == 0:
                current_array[x][y] += 1
                current_array, empty_flashes, flashes = try_to_flash(
                    current_array,
                    empty_flashes,
                    x,
                    y
                )
                flash_counter += flashes
    return current_array, empty_flashes, flash_counter


def make_all_process_part_1(
        loaded_data: np.array,
        iterations: int = 100
) -> int:
    current_frame = loaded_data.copy()
    total_flashes = 0
    for i in range(iterations):
        current_frame, _, flashes = make_iteration(current_frame)
        total_flashes += flashes
    return total_flashes


def find_synchro_moment_part_2(
    loaded_data: np.array
) -> int:
    current_frame = loaded_data.copy()
    for i in range(9999999999):
        current_frame, current_flashes, _ = make_iteration(current_frame)
        unique, counts = np.unique(current_frame, return_counts=True)
        res = dict(zip(unique, counts))
        if 0 in res.keys():
            if res[0] == 100:
                return i + 1


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Test Part I: '
          f'{make_all_process_part_1(test_data)}')
    print(f'Submission Part I: '
          f'{make_all_process_part_1(submission_data)}')
    print(f'Test Part I: '
          f'{find_synchro_moment_part_2(test_data)}')
    print(f'Submission Part I: '
          f'{find_synchro_moment_part_2(submission_data)}')
