"""
Day 15 tests
Benjamin Wheeler
"""
from day15.solution import part1, part2


def test_part1():
    # Test the step-by-step example
    assert part1('0,3,6') == 436

    # Test several examples
    data = {
        '1,3,2': 1,
        '2,1,3': 10,
        '1,2,3': 27,
        '2,3,1': 78,
        '3,2,1': 438,
        '3,1,2': 1836
    }

    for nums, ans in data.items():
        assert part1(nums) == ans




def test_part2():
    pass

