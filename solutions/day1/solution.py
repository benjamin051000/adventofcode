"""
Day 1 initial solution
Benjamin Wheeler
"""


def part1() -> int:
    with open('day1.input', 'r') as f:
        entries = [int(line) for line in f.readlines()]

    # Find two entries that sum to 2020.
    for idx, i in enumerate(entries):
        for j in entries[idx:]:
            if i + j == 2020:
                return i * j


def part2() -> int:
    with open('day1.input', 'r') as f:
        entries = [int(line) for line in f.readlines()]

    # Find three entries that sum to 2020.
    for i, x in enumerate(entries):
        for j, y in enumerate(entries[i:]):
            for z in entries[j:]:
                if x + y + z == 2020:
                    return x * y * z


if __name__ == '__main__':
    answer = part1()
    print(answer)

    answer = part2()
    print(answer)
