"""
Advent of Code 2023
Day 2 solution
Author: Benjamin Wheeler
"""

def is_possible(vals):
    rules = {"red": 12, "green": 13, "blue": 14}
    result = { rules[c] - vals[c] >= 0 for c in vals.keys() }
    # breakpoint()
    return all(result)


def part1(text: str) -> int:
    lines = text.splitlines()
    total = 0
    for game_num, line in enumerate(lines, start=1):
        line = line[line.index(': ')+2:]
        parts = line.split(';')

        is_part_possible = True
        for part in parts:
            part = part.split(', ')
            vals = {x.split()[1]: int(x.split()[0]) for x in part}
            is_part_possible &= is_possible(vals)

        if is_part_possible:
            total += game_num

    return total


def part2(text: str) -> int:
    lines = text.splitlines()
    return 0

def main():
    print(f'Running day 2...')

    with open('day02_input.txt') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

if __name__ == '__main__':
    main()
