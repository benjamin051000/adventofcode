"""
Day 12 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day12.solution import part1, part2


def test_example1():
    example = dedent("""\
    F10
    N3
    F7
    R90
    F11
    """)
    assert part1(example) == 25
    assert part2(example) == 286


def test_part1():
    assert part1() == 904


def test_part2():
    pass

