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
    text_input = dedent("""\
        class: 0-1 or 4-19
        row: 0-5 or 8-19
        seat: 0-13 or 16-19

        your ticket:
        11,12,13

        nearby tickets:
        3,9,18
        15,1,5
        5,14,9
    """)
    output = part2(text_input)
    

