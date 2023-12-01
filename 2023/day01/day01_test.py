"""
Advent of Code 2023
Day 1 tests
Author: Benjamin Wheeler
"""
from day01 import part1, part2
from textwrap import dedent

text = dedent("""\
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """)

def test_part1():
    assert part1(text) == 142


def test_part2():
    assert part2(text) == 0

