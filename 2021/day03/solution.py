"""
Advent of Code 2021
Day 3 solution
Author: Benjamin Wheeler
"""
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


def part2(text: str) -> int:
    lines = text.splitlines()


if __name__ == '__main__':
    print(f'Running day 3...')

    with open('day03.input') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

