from typing import List
import numpy as np

AGE_MAPPING = {0: 6, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}


def load_data(file_path: str) -> List:
    with open(file_path, 'r') as file:
        input_state_data = [int(x) for x in file.readline().strip().split(',')]
        return input_state_data


def state_logger(day: int, fish_count: int, is_initial: bool = False) -> None:
    if is_initial:
        print(f'Initial state: {fish_count}')
    elif day < 10:
        print(f'After  {day} days: {fish_count}')
    else:
        print(f'After {day} days: {fish_count}')


def calculate_using_dict(
        number_of_days: int,
        initial_state: List,
        debug: bool = False) -> int:
    if debug:
        state_logger(0, len(initial_state), is_initial=True)
    unique, counts = np.unique(initial_state, return_counts=True)
    current_state = {k: 0 for k in AGE_MAPPING.keys()}
    for key, value in zip(unique, counts):
        current_state[key] = value
    for day in range(number_of_days):
        number_of_fishes_to_rotate = current_state[0]
        current_state = {
            AGE_MAPPING[age]: current_state[age] for age in range(
                min(AGE_MAPPING.keys()), max(AGE_MAPPING.keys()) + 1
            )
        }
        current_state[8] = number_of_fishes_to_rotate
        current_state[6] += number_of_fishes_to_rotate
        if debug:
            state_logger(day + 1, sum(current_state.values()))

    return sum(current_state.values())


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Test_1_1: '
          f'{calculate_using_dict(18, test_data)}')
    print(f'calculate_using_dict: '
          f'{calculate_using_dict(80, test_data)}')
    print(f'Submission_1: '
          f'{calculate_using_dict(80, submission_data)}')
    print(f'Test_2: '
          f'{calculate_using_dict(256, test_data)}')
    print(f'Submission_2: '
          f'{calculate_using_dict(256, submission_data)}')
