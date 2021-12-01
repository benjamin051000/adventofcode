"""
Day 12 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day12.solution import part1
from day12.solution_part2 import part2


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
    assert part2() == 18747


def test_part2_rotations():
    example = dedent("""\
    F10
    R180
    F20
    L180
    F20
    R90
    R90
    F20
    L90
    L90
    F10
    """)
    # Ship should return to 0,0
    assert part2(example) == 0
