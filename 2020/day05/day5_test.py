"""
Day 5 tests
Benjamin Wheeler
"""
from day05.solution import *


def test_get_row_col():
    seats = ('FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL')
    r_c = ((44, 5), (70, 7), (14, 7), (102, 4))

    for seat, ans in zip(seats, r_c):
        assert get_row_col(seat) == ans


def test_part1():
    assert part1() == 998


def test_part2():
    assert part2() == 676

