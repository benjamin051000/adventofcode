"""
Advent of Code 2023
Day 1 solution
Author: Benjamin Wheeler
"""
from typing import Tuple
import re

def part1(text: str) -> int:
    lines = text.splitlines()
    total = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        first = digits[0]
        last = digits[-1]
        total += int(first + last)
    return total

def get_first_and_last_numbers(line: str) -> Tuple[str, str]:
    terms = [r"\d", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits = re.findall(f"(?=({'|'.join(terms)}))", line)
    first = digits[0]
    last = digits[-1]
    if first in terms:
        first = str(terms.index(first))
    if last in terms:
        last = str(terms.index(last))
    return first, last

def part2(text: str) -> int:
    lines = text.splitlines()
    total = 0
    for line in lines:
        first, last = get_first_and_last_numbers(line)
        total += int(first + last)
    return total


def main():
    print(f'Running day 1...')

    with open('day01_input.txt') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

if __name__ == '__main__':
    main()
