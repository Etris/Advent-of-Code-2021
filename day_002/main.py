from typing import List, Tuple


def load_data(file: str) -> List:
    with open(file, 'r') as file:
        input_data = []
        for line in file.readlines():
            parsed_line = line.strip().split(' ')
            input_data.append(
                {
                    'direction': str(parsed_line[0]),
                    'scale': int(parsed_line[1])
                }
            )
        return input_data


def move_ship(input_data: List) -> Tuple:
    horizontal = 0
    depth = 0
    for line in input_data:
        if line.get('direction') == 'forward':
            horizontal += line.get('scale')
        elif line.get('direction') == 'up':
            depth -= line.get('scale')
        elif line.get('direction') == 'down':
            depth += line.get('scale')
        else:
            raise ValueError("Unknown movement")
    return horizontal, depth


def process_first_part(input_data: List) -> int:
    horizontal, depth = move_ship(input_data)
    return horizontal * depth


def move_ship_with_aim(input_data: List) -> Tuple:
    horizontal = 0
    depth = 0
    aim = 0
    for line in input_data:
        current_value = line.get('scale')
        if line.get('direction') == 'forward':
            horizontal += current_value
            if aim != 0:
                depth += (aim * line.get('scale'))
        elif line.get('direction') == 'up':
            aim -= current_value
        elif line.get('direction') == 'down':
            aim += current_value
        else:
            raise ValueError("Unknown movement")
    return horizontal, depth


def process_second_part(input_data: List) -> int:
    horizontal, depth = move_ship_with_aim(input_data)
    print(horizontal, depth)
    return horizontal * depth


if __name__ == '__main__':
    print(f'Test_1: {process_first_part(load_data("test.txt"))}')
    print(f'Task_1: {process_first_part(load_data("submission.txt"))}')
    print(f'Test_2: {process_second_part(load_data("test.txt"))}')
    print(f'Task_2: {process_second_part(load_data("submission.txt"))}')
