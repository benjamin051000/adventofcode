"""
Day 14 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day14.solution import part1, part2


def test_part1():
    example = dedent("""\
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0
    """)

    assert part1(example) == 165

    assert part1() == 6559449933360


def test_part2():
    pass

