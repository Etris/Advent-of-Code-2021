from typing import List


def load_data(file_path: str) -> List:
    with open(file_path, 'r') as file:
        input_state_data = [int(x) for x in file.readline().strip().split(',')]
        return input_state_data


def find_optimal_position(input_data: List) -> int:
    current_best_position = 0
    current_best_score = None
    min_pos = min(input_data)
    max_pos = max(input_data)
    for ix in range(min_pos, max_pos + 1):
        current_sum = sum([abs(ix - x) for x in input_data])
        if current_best_score:
            if current_best_score > current_sum:
                current_best_score = current_sum
                current_best_position = ix
        else:
            current_best_score = current_sum
            current_best_position = ix
    print(current_best_position)
    return current_best_score


def calculate_scaled_rate(input_value: int) -> int:
    return sum([
        x for x in range(0, input_value +1)
    ])


def find_optimal_position_scaled(input_data: List) -> int:
    current_best_position = 0
    current_best_score = None
    min_pos = min(input_data)
    max_pos = max(input_data)
    for ix in range(min_pos, max_pos + 1):
        current_sum = sum(
            [
                calculate_scaled_rate(abs(ix - x)) for x in input_data
            ]
        )
        if current_best_score:
            if current_best_score > current_sum:
                current_best_score = current_sum
                current_best_position = ix
        else:
            current_best_score = current_sum
            current_best_position = ix
    print(f'Best position: {current_best_position}')
    return current_best_score


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Test 1: '
          f'{find_optimal_position(test_data)}')
    print(f'Submission 1: '
          f'{find_optimal_position(submission_data)}')
    print(f'Test 2: '
          f'{find_optimal_position_scaled(test_data)}')
    print(f'Submission 2: '
          f'{find_optimal_position_scaled(submission_data)}')
