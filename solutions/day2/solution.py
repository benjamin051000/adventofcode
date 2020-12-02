"""
Day 2 initial solution
Benjamin Wheeler
"""
import re


def part1() -> int:
    with open('day2.input', 'r') as f:
        entries = f.readlines()

    # Use a regular expression to find the valid characters.
    pattern = re.compile(r'(\d+)-(\d+) (\D): (\D+)')
    total = 0

    for e in entries:
        least, most, check, psswd = re.match(pattern, e).groups()
        occurrences = re.findall(f'({check})', psswd)
        total += 1 if int(least) <= len(occurrences) <= int(most) else 0

    return total


def part2():
    pass


if __name__ == '__main__':
    answer = part1()
    print(answer)
