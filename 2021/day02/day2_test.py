"""
Day 2 tests
Benjamin Wheeler
"""
from solution import part1, part2
from textwrap import dedent

text = dedent("""\
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    """)

def test_part1():
    assert part1(text) == 150


def test_part2():
    assert part2(text) == 900

if __name__ == '__main__':
    test_part2()