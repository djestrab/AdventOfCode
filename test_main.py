from main import *


def test_read_input():
    test_input = read_input(1)
    assert test_input == ""


def test_open_box():
    assert False


def test_parse_input():
    assert parse_input("inputs/1.txt") == ""
