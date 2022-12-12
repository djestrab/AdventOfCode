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


def open_box(day_number: int):
    """

    """







