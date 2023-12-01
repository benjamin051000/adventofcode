"""
Advent of Code 2023
Day 1 tests
Author: Benjamin Wheeler
"""
from day01 import part1, part2
from textwrap import dedent


def test_part1_example():
    text = dedent("""\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """)
    assert part1(text) == 142


def test_part2_example():
    text = dedent("""\
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """)
    assert part2(text) == 281

##############################
# WARNING: SPOILERS AHEAD!!!
##############################
def test_part1():
    with open('day01_input.txt') as f:
        text = f.read()
    assert part1(text) == 53080

def test_part2():
    with open('day01_input.txt') as f:
        text = f.read()
    assert part2(text) == 53268
