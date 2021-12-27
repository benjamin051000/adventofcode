"""
Advent of Code 2021
Day 3 tests
Author: Benjamin Wheeler
"""
from solution import part1, part2
from textwrap import dedent

text = dedent("""\
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    """)

def test_part1():
    assert part1(text) == 198


def test_part2():
    assert part2(text) == 230

if __name__ == '__main__':
    test_part1()

    test_part2()