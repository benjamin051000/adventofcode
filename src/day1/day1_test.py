"""
Day 1 tests utilizing pytest
Benjamin Wheeler
"""
from day1.solution import part1, part2


def test_part1():
    assert part1() == 989824


def test_part2():
    assert part2() == 66432240
