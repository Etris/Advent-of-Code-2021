from typing import List, Tuple


def load_data(file: str) -> List:
    with open(file, 'r') as file:
        input_data = []
        for line in file.readlines():
            input_data.append(str(line).replace("\n",''))
        return input_data


def binary_to_decimal(input_binary_string: str) -> int:
    return int(input_binary_string, 2)


def calculate_most_common_on_position(
        input_data: List,
        position: int,
        reverse: bool = False,
        equal_return_smaller: bool = False
) -> int:
    scoring = {}
    for ix in range(len(input_data)):
        current_value = input_data[ix][position]
        scoring[current_value] = scoring.get(current_value, 0) + 1
    if (int(min(scoring, key=scoring.get))
            == int(max(scoring, key=scoring.get))):
        if equal_return_smaller:
            return 0
        else:
            return 1
    if reverse:
        return int(min(scoring, key=scoring.get))
    else:
        return int(max(scoring, key=scoring.get))


def calculate_gamma(input_data: List, calculate_epsilon: bool = False) -> int:
    if len(input_data) > 0:
        final_binary_string = ""
        for ix in range(len(input_data[0])):
            final_binary_string += str(calculate_most_common_on_position(
                input_data,
                ix,
                calculate_epsilon
            ))
        return binary_to_decimal(final_binary_string)
    else:
        raise ValueError("Empty input data")


def calulate_oxygen_and_co_ratings(
        input_data,
        calculate_co: bool = False
) -> int:
    if len(input_data) > 0:
        total_length_of_str = len(input_data[0])
        current_input_data = input_data.copy()
        for ix in range(total_length_of_str):
            if calculate_co:
                current_bit_allowed = calculate_most_common_on_position(
                    current_input_data,
                    ix,
                    reverse=True,
                    equal_return_smaller=True
                )
            else:
                current_bit_allowed = calculate_most_common_on_position(
                    current_input_data,
                    ix
                )
            current_input_data = [
                element for element in current_input_data
                if element[ix] == str(current_bit_allowed)
            ]
            if len(current_input_data) == 1:
                return binary_to_decimal(current_input_data[0])
    else:
        raise ValueError("Empty input data")


def calculate_power_consumption_base(input_data: List) -> int:
    return (calculate_gamma(input_data) *
            calculate_gamma(input_data, calculate_epsilon=True))


def calculate_life_support_rating(input_data: List) -> int:
    return (
        calulate_oxygen_and_co_ratings(input_data) *
        calulate_oxygen_and_co_ratings(input_data, calculate_co=True)
    )


if __name__ == '__main__':
    print(f'Test_1: '
          f'{calculate_power_consumption_base(load_data("test.txt"))}')
    print(f'Task_1: '
          f'{calculate_power_consumption_base(load_data("submission.txt"))}')
    print(f'Test_2: '
          f'{calculate_life_support_rating(load_data("test.txt"))}')
    print(f'Task_2: '
          f'{calculate_life_support_rating(load_data("submission.txt"))}')
