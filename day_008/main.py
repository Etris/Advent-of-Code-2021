from typing import List, Dict


def load_data(file_path: str) -> List[Dict]:
    with open(file_path, 'r') as file:
        loaded_data = []
        for line in file.readlines():
            current_line_split = line.split('|')
            loaded_data.append(
                {
                    'input_strings': [
                        str(x).strip() for x in current_line_split[0].split()
                    ],
                    'output_digits': [
                        str(x).strip() for x in current_line_split[1].split()
                    ]
                }
            )
        return loaded_data


def check_if_one(current_string: str) -> bool:
    if (len(set([x for x in current_string.strip()])) == 2
            and len(current_string) == 2):
        return True
    return False


def check_if_four(current_string: str) -> bool:
    if (len(set([x for x in current_string.strip()])) == 4
            and len(current_string) == 4):
        return True
    return False


def check_if_seven(current_string: str) -> bool:
    if (len(set([x for x in current_string.strip()])) == 3
            and len(current_string) == 3):
        return True
    return False


def check_if_eight(current_string: str) -> bool:
    if (len(set([x for x in current_string.strip()])) == 7
            and len(current_string) == 7):
        return True
    return False


def identify_digits(current_string: str) -> int:
    # print(current_string, len(current_string))
    if check_if_one(current_string):
        return 1
    elif check_if_four(current_string):
        return 4
    elif check_if_seven(current_string):
        return 7
    elif check_if_eight(current_string):
        return 8
    else:
        return -1


def split_string(current_string: str) -> List:
    return [x for x in current_string.strip()]


def prepare_mapping_patterns(input_list: List) -> Dict:
    mappings = {}
    current_list = input_list.copy()
    # start with finding 1
    for element in input_list:
        if check_if_one(element):
            mappings[1] = element
            break
    current_list.remove(mappings[1])
    # find 8 - pattern
    for element in input_list:
        if check_if_eight(element):
            mappings[8] = element
            break
    current_list.remove(mappings[8])
    # find 4 - pattern
    for element in input_list:
        if check_if_four(element):
            mappings[4] = element
            break
    current_list.remove(mappings[4])
    # find 7 - pattern
    for element in input_list:
        if check_if_seven(element):
            mappings[7] = element
            break
    current_list.remove(mappings[7])
    # find 3 - len(5) - that one that contain 1 in pattern
    for element in current_list:
        if len(element) == 5:
            if len(set(split_string(element)).intersection(
                    split_string(mappings[1]))) == 2:
                mappings[3] = element
                break
    current_list.remove(mappings[3])
    # find 6 - 8 - 1 element of 1, len(6)
    letters_1 = split_string(mappings[1])
    for element in current_list:
        if len(element) == 6:
            for letter in letters_1:
                current_str_list = split_string(mappings[8])
                current_str_list.remove(letter)
                if sorted(split_string(element)) == \
                        sorted(current_str_list):
                    mappings[6] = element
                    break
    current_list.remove(mappings[6])
    # find 9 - len(6), 3 i 4  union = 9
    sequence_9 = set(split_string(mappings[3])).union(
        set(split_string(mappings[4])))
    sequence_9 = list(sequence_9)
    for element in current_list:
        if len(element) == 6:
            if sorted(sequence_9) == sorted(split_string(element)):
                mappings[9] = element
                break
    current_list.remove(mappings[9])
    # find 0 - len(6)
    for element in current_list:
        if len(element) == 6:
            mappings[0] = element
            break
    current_list.remove(mappings[0])
    # find 5 - len(5), 8 - 6 i 8 - 9
    diff_8_6 = set(split_string(mappings[8])).difference(
        split_string(mappings[6]))
    diff_8_9 = set(split_string(mappings[8])).difference(
        split_string(mappings[9]))
    sequence_5 = set(split_string(mappings[8])).difference(
        diff_8_6.union(diff_8_9))
    for element in current_list:
        if len(element) == 5:
            if sorted(sequence_5) == sorted(split_string(element)):
                mappings[5] = element
                break
    current_list.remove(mappings[5])
    # find 2 - len(5), last one
    for element in current_list:
        if len(element) == 5:
            mappings[2] = element
            break
    current_list.remove(mappings[2])
    return mappings


def identify_all_digits(current_string: str, current_pattern: Dict) -> int:
    for key, value in current_pattern.items():
        if sorted(split_string(current_string)) == \
                sorted(split_string(value)):
            return key
    return -1


def count_digits_in_output_values(current_set_of_digits: List) -> int:
    counter = 0
    for element in current_set_of_digits:
        if identify_digits(element) != -1:
            counter += 1
    # print(current_set_of_digits, counter)
    return counter


def process_all_output_values(current_data: List) -> int:
    total_counter = 0
    for single_row in current_data:
        total_counter += count_digits_in_output_values(
            single_row.get('output_digits', [])
        )
    return total_counter


def get_sum_of_digits_from_output_values(
        current_input_values: List,
        current_set_of_digits: List
) -> int:
    current_resolution = ''
    current_mapping = prepare_mapping_patterns(current_input_values)
    for element in current_set_of_digits:
        digit = identify_all_digits(element, current_mapping)
        if digit != -1:
            current_resolution += str(digit)
    return int(current_resolution)


def get_sum_of_all_values(current_data: List) -> int:
    total_counter = 0
    for single_row in current_data:
        current_sum = get_sum_of_digits_from_output_values(
            single_row.get('input_strings', []),
            single_row.get('output_digits', [])
        )
        total_counter += current_sum
        #print(single_row['output_digits'], current_sum)
    return total_counter


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Test 1: '
          f'{process_all_output_values(test_data)}')
    print(f'Submission 1: '
          f'{process_all_output_values(submission_data)}')
    print(f'Test 2: '
          f'{get_sum_of_all_values(test_data)}')
    print(f'Submission 2: '
          f'{get_sum_of_all_values(submission_data)}')
