"""
Day 16 tests
Benjamin Wheeler
"""
from day16.solution import part1, part2
from textwrap import dedent

def test_part1():
    test_input = dedent("""\
        class: 1-3 or 5-7
        row: 6-11 or 33-44
        seat: 13-40 or 45-50

        your ticket:
        7,1,14

        nearby tickets:
        7,3,47
        40,4,50
        55,2,20
        38,6,12"""
    )
    output = part1(test_input)
    assert output == 71


def test_part2():
    pass

