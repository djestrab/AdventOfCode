"""
Advent of Code
"""
import urllib3


ADVENT_URL = "https://adventofcode.com"
YEAR = "2022"


def read_input(day_number: int):
    """
    Read input from given URL
    """
    # TODO add auth
    day_number = str(day_number)
    http = urllib3.PoolManager()
    url = f"{ADVENT_URL}/{YEAR}/day/{day_number}/input"
    response = http.request("GET", url)
    if response.status == 200:
        return response.data
    else:
        raise Exception(response.data)


def parse_input(filename: str) -> list:
    """
    Take filename as input and return parsed in a list
    """
    # TODO specific for day 1

    parsed_input = []
    with open(filename) as file:
        temp_list = []
        for line in file:
            if line != "\n":
                temp_list.append(int(line.strip()))
            else:
                parsed_input.append(temp_list)
                temp_list = []
        parsed_input.append(temp_list)
    return parsed_input


def open_box(day_number: int):
    """

    """


# Day 1
def open_day_one():
    input_list = parse_input("inputs/1.txt")
    sums = [sum(elf) for elf in input_list]
    return max(sums)


def open_day_one_part_two():
    input_list = parse_input("inputs/1.txt")
    sums = [sum(elf) for elf in input_list]
    sums.sort(reverse=True)
    return sum(sums[:3])


# print(open_day_one())
# print(open_day_one_part_two())


