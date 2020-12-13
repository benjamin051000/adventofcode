"""
Day 10 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day10.solution import part1, part2
from timeit import default_timer


def test_part1():
    assert part1() == 2376


def test_example1():
    example = dedent("""\
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """)
    assert part1(example) == 7 * 5
    assert part2(example) == 8


def test_example2():
    example = dedent("""\
    28
    33
    18
    42
    31
    14
    46
    20
    48
    47
    24
    23
    49
    45
    19
    38
    39
    11
    1
    32
    25
    35
    8
    17
    7
    9
    4
    2
    34
    10
    3
    """)
    assert part1(example) == 22 * 10
    assert part2(example) == 19208


def test_part2():
    start = default_timer()
    assert part2() == 129586085429248
    end = default_timer()
    print('Elapsed time:', end - start)
