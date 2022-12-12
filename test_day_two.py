from day_two import *


def test_open_day_two():
    strategy_guide = parse_input("inputs/test_2.txt")
    assert calculate_total_score(strategy_guide) == 15
