from typing import List, Tuple


def load_data(file: str) -> Tuple:
    with open(file, 'r') as file:
        chosen_numbers = []
        bingo_list = []
        current_bingo = None
        for line in file.readlines():
            if len(chosen_numbers) == 0:
                chosen_numbers = [int(x) for x in str(line).strip().split(',')]
            else:
                if len(line.strip()) == 0:
                    if current_bingo:
                        bingo_list.append(current_bingo.copy())
                    current_bingo = []
                    current_bingo_iterator_line = 0
                else:
                    current_bingo.append(
                        [
                            int(x) for x in str(line).strip().split()
                        ]
                    )
                    current_bingo_iterator_line += 1
        bingo_list.append(current_bingo.copy())
        return chosen_numbers, bingo_list


def check_single_pattern(
        list_of_previously_chosen_numbers: List,
        current_line: List
) -> bool:
    chosen_numbers = set(list_of_previously_chosen_numbers)
    current_line_set = set(current_line)
    if len(chosen_numbers.intersection(current_line_set)) == 5:
        return True
    return False


def check_all_horizontals(
        list_of_previously_chosen_numbers: List,
        current_bingo: List
) -> bool:
    for ix in range(5):
        if check_single_pattern(
                list_of_previously_chosen_numbers,
                current_bingo[ix]
        ):
            return True
    return False


def check_all_verticals(
        list_of_previously_chosen_numbers: List,
        current_bingo: List
) -> bool:
    for ix in range(5):
        current_line = [
            x[ix] for x in current_bingo
        ]
        if check_single_pattern(
                list_of_previously_chosen_numbers,
                current_line
        ):
            return True
    return False


def check_all_patterns(
        list_of_previously_chosen_numbers: List,
        current_bingo: List
) -> bool:
    return any([
        check_all_verticals(list_of_previously_chosen_numbers, current_bingo),
        check_all_horizontals(list_of_previously_chosen_numbers, current_bingo)
    ])


def get_sum_of_all_unmarked(
        list_of_previously_chosen_numbers: List,
        current_bingo: List
) -> int:
    result_sum = 0
    for ix in range(5):
        for bx in range(5):
            if current_bingo[ix][bx] not in list_of_previously_chosen_numbers:
                result_sum += current_bingo[ix][bx]
    return result_sum


def make_all_bingo_movements(
        list_of_all_moves: List,
        list_of_cards: List
) -> int:
    list_of_current_movements = []
    for move in list_of_all_moves:
        list_of_current_movements.append(move)
        for single_card in list_of_cards:
            if check_all_patterns(list_of_current_movements, single_card):
                return move * get_sum_of_all_unmarked(
                    list_of_current_movements,
                    single_card
                )


def let_squid_win_so_choose_last_bingo_table(
        list_of_all_moves: List,
        list_of_cards: List
) -> int:
    all_winners = []
    all_winners_movements = []
    list_of_current_movements = []
    list_of_current_cards = list_of_cards.copy()
    for move in list_of_all_moves:
        list_of_current_movements.append(move)
        for current_card in list_of_current_cards:
            if check_all_patterns(list_of_current_movements, current_card):
                all_winners.append(current_card)
                all_winners_movements = list_of_current_movements.copy()
        list_of_current_cards = [
            card for card in list_of_current_cards if card not in all_winners
        ]
    return all_winners_movements[-1] * get_sum_of_all_unmarked(
        all_winners_movements,
        all_winners[-1]
    )


if __name__ == '__main__':
    test_movements, test_cards = load_data("test.txt")
    submission_movements, submission_cards = load_data("submission.txt")
    print(f'Test_1: '
          f'{make_all_bingo_movements(test_movements, test_cards)}')
    print(f'Task_1: '
          f'{make_all_bingo_movements(submission_movements, submission_cards)}')
    print(f'Test_2: '
          f'{let_squid_win_so_choose_last_bingo_table(test_movements, test_cards)}')
    print(f'Task_2: '
          f'{let_squid_win_so_choose_last_bingo_table(submission_movements, submission_cards)}')
