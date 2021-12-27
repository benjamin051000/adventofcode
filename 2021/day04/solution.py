"""
Advent of Code 2021
Day 4 solution
Author: Benjamin Wheeler
"""


def part1(text: str) -> int:
    lines = text.splitlines()
    return 0


def part2(text: str) -> int:
    lines = text.splitlines()
    return 0

def main():
    print(f'Running day 4...')

    with open('day02.input') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

if __name__ == '__main__':
    main()
