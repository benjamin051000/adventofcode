"""
Day 10 initial solution
Benjamin Wheeler
"""


def part1(adapters: str = None) -> int:
    if not adapters:
        with open('day10.input', 'r') as f:
            adapters = f.read()

    # Get in int form
    adapters = [int(e) for e in adapters.splitlines()]

    adapters.sort()

    # Access by index to increment diffs of 1, 2, and 3.
    diffs = [0, 0, 0]
    last_adapter = 0
    for adapter in adapters:
        diffs[adapter - last_adapter - 1] += 1
        last_adapter = adapter

    # Add device's rating (3 higher than highest adapter)
    diffs[2] += 1

    return diffs[0] * diffs[2]



def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Running day 10...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

