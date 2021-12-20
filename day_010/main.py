from typing import List, Tuple

opening_sequence = '{([<'
closing_sequence = '})]>'

opening_brackets = {k: v for k, v in zip(opening_sequence,
                                         closing_sequence)}
closing_brackets = {k: v for k, v in zip(opening_sequence,
                                         closing_sequence)}

scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
scoring_autocomplete = {')': 1, ']': 2, '}': 3, '>': 4}


def load_data(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        main_frame = []
        for line in file.readlines():
            main_frame.append(
                line.strip().replace("\n", '')
            )
        return main_frame


def find_miss_matched(text: str):
    current_stack = []
    for char in text:
        if char in opening_brackets:
            current_stack.append(char)
        elif char in closing_brackets:
            removed_char = current_stack.pop()
            if closing_brackets[char] != removed_char:
                return char


def find_all_corrupted(loaded_data: List[str]) -> int:
    current_scores = []
    for line in loaded_data:
        char_returned = find_miss_matched(line)
        if char_returned is not None:
            current_scores.append(
                scoring[char_returned]
            )
    return sum(current_scores)


def remove_all_corrupted(loaded_data: List[str]) -> List[str]:
    allowed_lines = []
    for line in loaded_data:
        if not find_miss_matched(line):
            allowed_lines.append(line)
    return allowed_lines


def fill_stack_for_current_line(line: str) -> List[str]:
    current_stack = []
    for char in line:
        if char in opening_sequence:
            current_stack.append(char)
        elif char in closing_sequence:
            current_stack.pop()
    return current_stack


def autocomplete_not_corrupted(loaded_data: List[str]) -> int:
    current_scores = []
    for line in remove_all_corrupted(loaded_data):
        remaining_chars = fill_stack_for_current_line(line)
        filled_chars = [opening_brackets[op] for op in remaining_chars[::-1]]
        score = 0
        for char in filled_chars:
            score *= 5
            score += scoring_autocomplete[char]
        current_scores.append(score)
    sorted_scores = sorted(current_scores)
    return sorted_scores[int(len(sorted_scores) // 2)]


if __name__ == '__main__':
    test_data = load_data('test.txt')
    submission_data = load_data('submission.txt')
    print(f'Test Part I: '
          f'{find_all_corrupted(test_data)}')
    print(f'Submission Part I: '
          f'{find_all_corrupted(submission_data)}')
    print(f'Test Part II: '
          f'{autocomplete_not_corrupted(test_data)}')
    print(f'Submission Part II: '
          f'{autocomplete_not_corrupted(submission_data)}')
