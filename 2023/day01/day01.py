"""
Advent of Code 2023
Day 1 solution
Author: Benjamin Wheeler
"""


def part1(text: str) -> int:
    lines = text.splitlines()
    return 0


def part2(text: str) -> int:
    lines = text.splitlines()
    return 0

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
