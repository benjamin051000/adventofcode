"""
Advent of Code 2023
Day 2 tests
Author: Benjamin Wheeler
"""
from day02 import part1, part2
from textwrap import dedent

text = dedent("""\
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """)

def test_part1_example():
    assert part1(text) == 8


def test_part2_example():
    assert part2(text) == 0


##############################
# WARNING: SPOILERS AHEAD!!!
##############################
def test_part1():
    with open('day02_input.txt') as f:
        text = f.read()
    assert part1(text) == 0  # TODO replace with actual solution

def test_part2():
    with open('day02_input.txt') as f:
        text = f.read()
    assert part2(text) == 0  # TODO replace with actual solution
