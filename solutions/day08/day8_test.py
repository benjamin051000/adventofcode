"""
Day 8 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day08.solution import part1, part2


def test_part1():
    assert part1() == 1179


def test_part2_example():
    example = dedent("""\
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6"""
    )

    assert part2(example) == 8


def test_part2():
    assert part2() == 1089

