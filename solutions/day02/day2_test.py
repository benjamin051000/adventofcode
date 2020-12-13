"""
Day 2 tests
Benjamin Wheeler
"""
from timeit import Timer
from day02.solution import part1, part2


def test_part1():
    assert part1() == 564
    t = Timer(part1)
    runtime = t.timeit(number=1000)
    print('\nAverage runtime', runtime)


def test_part2():
    assert part2() == 325
    t = Timer(part2)
    runtime = t.timeit(number=1000)
    print('\nAverage runtime', runtime)

