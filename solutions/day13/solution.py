"""
Day 13 initial solution
Benjamin Wheeler
"""
from functools import reduce
import operator


def part1(lines=None) -> int:
    if not lines:
        with open('day13.input', 'r') as f:
            lines = f.read()
    earliest, routes = lines.splitlines()

    # Format input
    earliest = int(earliest)
    routes = [int(r) for r in routes.split(',') if r != 'x']

    # earliest % route gives the amount of time we missed the route by.
    # Modulo operator is useful because the routes are periodic (reset to 0).
    next_buses = [route - earliest % route for route in routes]

    # Pick the one coming up the soonest.
    next_bus = min(next_buses)

    return next_bus * routes[next_buses.index(next_bus)]


def chinese(*, remainders, modulae):
    """ Performs the chinese remainder theorem. """

    total = 0
    product = reduce(operator.mul, modulae)

    print('N =', product)

    for remainder, mod in zip(remainders, modulae):
        ni = product // mod

        total += remainder * ni * pow(ni, -1, mod)  # modular multiplicative inverse (requires py3.8+)

    return total % product


def part2(routes=None) -> int:
    if not routes:
        with open('day13.input', 'r') as f:
            _, routes = f.read().splitlines()

    # Preserve the don't cares ('x') because index is important.
    routes = [int(r) if r != 'x' else 'x' for r in routes.split(',')]

    # Each remainder comes from the location in the base array.
    b = [idx for idx, r in enumerate(routes) if r != 'x']

    # Each modulae is the bus route time.
    n = [r for r in routes if r != 'x']

    # b[0] = routes[0]

    # Find a number x such that x % answer[n] == n where n is an index 0 <= n < len(answer).
    return chinese(remainders=b, modulae=n)


if __name__ == '__main__':
    print(f'Running day 13...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

