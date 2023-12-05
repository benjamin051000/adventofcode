"""
Advent of Code 2023
Day 3 tests
Author: Benjamin Wheeler
"""
from day03 import part1, part2
from textwrap import dedent

text = dedent("""\

    """)

def test_part1_example():
    assert part1(text) == 0


def test_part2_example():
    assert part2(text) == 0


##############################
# WARNING: SPOILERS AHEAD!!!
##############################
def test_part1():
    with open('day03_input.txt') as f:
        text = f.read()
    assert part1(text) == 0  # TODO replace with actual solution

def test_part2():
    with open('day03_input.txt') as f:
        text = f.read()
    assert part2(text) == 0  # TODO replace with actual solution
