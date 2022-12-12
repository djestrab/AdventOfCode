

def parse_input(filename: str) -> list:
    """
    Take filename as input and return parsed in a list(each round) of chars:
    """

    with open(filename) as file:
        parsed_input = ["".join(line.split()) for line in file]
    return parsed_input


def calculate_score(round_string: str) -> int:
    """
    Take a string representation of a round and return score for player
    Score = (0 if lost, 3 if draw, 6 if won) + (1 for Rock, 2 for Paper, and 3 for Scissors)
    """

    score_dict = {
        "AX": 3+1,
        "AY": 6+2,
        "AZ": 0+3,
        "BX": 0+1,
        "BY": 3+2,
        "BZ": 6+3,
        "CX": 6+1,
        "CY": 0+2,
        "CZ": 3+3
    }

    return score_dict[round_string]


def calculate_total_score(strategy_guide):
    """

    """
    return sum([calculate_score(encrypted_round) for encrypted_round in strategy_guide])


def open_day_two():
    strategy_guide = parse_input("inputs/2.txt")
    return calculate_total_score(strategy_guide)


print(open_day_two())


