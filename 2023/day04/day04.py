"""
Advent of Code 2023
Day 4 solution
Author: Benjamin Wheeler
"""


def part1(text: str) -> int:
    lines = text.splitlines()
    total = 0
    for line in lines:
        winning_nums_str, your_nums_str = line[line.index(':')+1:].split('|')
        winning_nums = set(winning_nums_str.split())
        your_nums = set(your_nums_str.split())
        winners = your_nums.intersection(winning_nums)
        total += int(2 ** (len(winners) - 1))
    return total


def part2(text: str) -> int:
    lines = text.splitlines()
    return 0

def main():
    print(f'Running day 4...')

    with open('day04_input.txt') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

if __name__ == '__main__':
    main()
