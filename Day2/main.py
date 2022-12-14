def outcome_v1(move1, move2):
    move_value = 1 if move2 == "X" else 2 if move2 == "Y" else 3
    if move1 == "A":
        return move_value if move2 == "Z" else move_value + 3 if move2 == "X" else move_value + 6

    if move1 == "B":
        return move_value if move2 == "X" else move_value + 3 if move2 == "Y" else move_value + 6

    if move1 == "C":
        return move_value if move2 == "Y" else move_value + 3 if move2 == "Z" else move_value + 6


def outcome_v2(move, result):
    if move == "A":
        return 3 if result == "X" else 4 if result == "Y" else 8

    if move == "B":
        return 1 if result == "X" else 5 if result == "Y" else 9

    if move == "C":
        return 2 if result == "X" else 6 if result == "Y" else 7


def score(rounds):
    current_score = 0
    for current_round in rounds:
        if len(current_round) != 3:
            break
        current_score += outcome_v2(current_round[0], current_round[2])

    return current_score


def main(input_file):
    with open(input_file) as f:
        file_content = f.read()

    rounds = file_content.split("\n")
    print(score(rounds))


if __name__ == '__main__':
    main('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
