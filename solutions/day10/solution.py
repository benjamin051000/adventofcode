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


def get_paths_cached(adps) -> int:
    cache = {}

    def get_paths(adapters, idx) -> int:
        """ Recursive function to retrieve all possible adapter paths. """
        # Check if it's in the cache.
        if idx in cache:
            return cache[idx]

        # Base case: If we've reached the end of the list
        if idx >= len(adapters) - 1:
            # Add one to the total
            return 1

        this_adapter = adapters[idx]

        # Get next 3 choices and see which ones are viable.
        next_adapters = adapters[idx+1: idx+1+3]

        # Try each one and sum up the results.
        total = 0

        for i, n in enumerate(next_adapters, start=1):
            if n - this_adapter <= 3:
                total += get_paths(adapters, i+idx)

        # Otherwise, none of them were viable.
        cache[idx] = total
        return total

    return get_paths(adps, 0)


def part2(adapters: str = None) -> int:
    if not adapters:
        with open('day10.input', 'r') as f:
            adapters = f.read()

    # Get in int form
    adapters = [int(e) for e in adapters.splitlines()]

    adapters.sort()

    # Add a zero to the beginning of the list
    adapters = [0] + adapters

    # Use recursion to check every combination
    return get_paths_cached(adapters)


if __name__ == '__main__':
    print(f'Running day 10...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

