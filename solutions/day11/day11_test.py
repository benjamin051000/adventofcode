"""
Day 11 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day11.solution import part1, part2, simulate_once


def test_example1():
    example = dedent("""\
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """)
    assert part1(example) == 37


def test_part1():
    assert part1() == 2361


def test_part2():
    pass

