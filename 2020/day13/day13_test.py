"""
Day 13 tests
Benjamin Wheeler
"""
from day13.solution import part1, part2, chinese, inverse


def test_part1():
    assert part1() == 3385


def test_chinese():
    b = [3, 1, 6]
    n = [5, 7, 8]
    assert chinese(remainders=b, modulae=n) == 78

    b = [2, 3, 2]
    n = [3, 5, 7]
    assert chinese(remainders=b, modulae=n) == 23


def test_part2():
    tests = {
        '7,13,x,x,59,x,31,19': 1068781,
        '17,x,13,19': 3417,
        '67,7,59,61': 754018,
        '67,x,7,59,61': 779210,
        '67,7,x,59,61': 1261476,
        '1789,37,47,1889': 1202161486
    }

    for i, o in tests.items():
        assert part2(i) == o

    # Test input file
    assert part2() == 600689120448303
