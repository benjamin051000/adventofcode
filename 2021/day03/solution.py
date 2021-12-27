"""
Advent of Code 2021
Day 3 solution
Author: Benjamin Wheeler
"""
from collections import Counter
import numpy as np


def part1(text: str) -> int:
    lines = text.splitlines()

    threshold =  len(lines) // 2

    # Create a matrix of the elements, and sum them on the column axis.
    arr: np.ndarray = np.array([list(line) for line in lines]).astype(int).sum(axis=0)
    
    gamma = "".join("1" if num > threshold else "0" for num in arr)
    epsilon = "".join("0" if num == "1" else "1" for num in gamma)  # Opposite

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)    

    return gamma * epsilon


def get_rating(arr: np.ndarray, o2_or_co2: int) -> int:
    """Part 2: Get either the oxygen or CO2 rating."""

    num_cols = arr.shape[1]

    for i in range(num_cols):
        column = arr[:, i]

        # Get most common.
        count = Counter(column)
        if count[0] == count[1]:
            bit_to_keep = o2_or_co2  # 1 for O2, 0 for CO2
        else:
            if o2_or_co2 == 1:  # Oxygen case
                bit_to_keep = count.most_common(1)[0][0]  # Whichever (0 or 1) was most common in the column.
            else:  # Case for CO2
                bit_to_keep = count.most_common()[-1][0]  # Get last in most common list, which is the least common.

        # Filter out unwanted ones.
        arr = np.array([row for row in arr if row[i] == bit_to_keep])

    # There should only be one element left. Return it.
    assert arr.shape == (1, num_cols)  # 1 row, n columns

    rating = int(''.join(map(str,arr[0])), base=2)

    return rating


def part2(text: str) -> int:
    lines = text.splitlines()

    arr: np.ndarray = np.array([list(l) for l in lines]).astype(int)

    OX_RATING_DEFAULT = 1
    CO2_RATING_DEFAULT = 0

    oxygen_rating = get_rating(arr, OX_RATING_DEFAULT)

    co2_rating = get_rating(arr, CO2_RATING_DEFAULT)

    return oxygen_rating * co2_rating


if __name__ == '__main__':
    print(f'Running day 3...')

    with open('day03.input') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

