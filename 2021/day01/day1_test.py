"""
Day 1 tests
Benjamin Wheeler
"""
from solution import part1, part2
from textwrap import dedent

text = dedent("""\
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
    """)

def test_part1():
    ans = part1(text)
    print("Part 1 answer:", ans)
    assert ans == 7

    # Real test
    assert part1() == 1451

def test_part2():
    ans = part2(text)
    print("Part 2 answer:", ans)
    assert ans == 5

    # Real test
    assert part2() == 1395
