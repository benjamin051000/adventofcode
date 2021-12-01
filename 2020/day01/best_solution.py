"""
Day 1
This is a refactored solution for performance.
Benjamin Wheeler
"""


def part1() -> int:
    """
    This function utilizes a set, which has O(1) access time rather
    than a for loop (O(n)) to search for values. This improves time
    complexity from O(n^2) in solution.py to O(n) (with an ammortized
    time complexity of O(n^2)).

    :return: Product of a and b.
    """
    with open('day1.input', 'r') as f:
        # Generate a set of numbers.
        entries: set = {int(line) for line in f.readlines()}

        for a in entries:
            # If a + b = 2020, then 2020 - a = b.
            if (b := 2020 - a) in entries:
                return a * b


def part2() -> int:
    """
    This refactored function improves time complexity
    from O(n^3) in solution.py to O(n^2) (with an ammortized
    time complexity of O(n^3)).

    :return: Product of a, b, and c.
    """
    with open('day1.input', 'r') as f:
        entries: set = {int(line) for line in f.readlines()}

    # Find three entries that sum to 2020.
    for a in entries:
        # Find b and c values that satisfy: 2020 - a = b + c.
        for b in entries:
            if (c := 2020 - a - b) in entries:
                return a * b * c


if __name__ == '__main__':
    answer = part1()
    print(answer)

    answer = part2()
    print(answer)
