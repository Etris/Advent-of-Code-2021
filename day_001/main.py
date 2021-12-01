from typing import List


def load_data(file: str) -> List:
    with open(file, 'r') as file:
        input_data = [
            int(str(line).replace("\n", '')) for line in file.readlines()
        ]
        return input_data


def calculate_growths(input_data: List) -> int:
    result = 0
    for ix in range(1, len(input_data)):
        if input_data[ix] > input_data[ix - 1]:
            result += 1
    return result


def calculate_window_growth(input_data: List, window_size: int) -> int:
    result = 0
    for ix in range(window_size-1, len(input_data)-1, 1):
        if sum(input_data[ix-2:ix+1]) < sum(input_data[ix-1:ix+2]):
            result += 1
    return result


if __name__ == '__main__':
    print(f'Test_1: {calculate_growths(load_data("test.txt"))}')
    print(f'Task_1: {calculate_growths(load_data("submission.txt"))}')
    print(f'Test_2: {calculate_window_growth(load_data("test.txt"),3)}')
    print(f'Task_2: {calculate_window_growth(load_data("submission.txt"),3)}')
