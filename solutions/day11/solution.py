"""
Day 11 initial solution
Benjamin Wheeler
"""
import itertools


def get_neighbors(seats, r, c):
    """ Returns number of neighbors around a particular seat. """
    total_rows = len(seats)
    total_cols = len(seats[0])

    neighbors = 0

    for v, h in itertools.product(range(-1, 2), repeat=2):
        # Check for boundary errors
        check_r = r + v
        check_c = c + h
        if not 0 <= check_r < total_rows or not 0 <= check_c < total_cols:
            continue

        # Skip own seat
        elif check_r == r and check_c == c:
            continue

        elif seats[check_r][check_c] == '#':  # Occupied seat
            neighbors += 1

    return neighbors


def simulate_once_part1(seats):
    """ Simulates one iteration of seat changing.
     Returns the new seating arrangement and total occupied seats."""

    # Use itertools.product to iterate through a 2D array a little simpler.
    total_rows = len(seats)
    total_cols = len(seats[0])

    # Record the seats that will change from L to # or vice versa.
    changes = []

    for r, c in itertools.product(range(total_rows), range(total_cols)):
        if seats[r][c] == '.':
            continue

        # Get sum of occupied seats around this one
        neighbors = get_neighbors(seats, r, c)

        # Next, see if this seat needs to change.
        if seats[r][c] == 'L' and neighbors == 0:
            changes.append((r, c, '#'))

        elif seats[r][c] == '#' and neighbors >= 4:
            changes.append((r, c, 'L'))

    # Apply changes
    for r, c, new in changes:
        seats[r][c] = new

    # Count total occupied
    occupied = len([seat for row in seats for seat in row if seat == '#'])

    return seats, occupied


def print_seats(seats, occ):
    """ Prints the seats.
     For debugging purposes."""
    rows = [''.join(row) for row in seats]
    print()
    print('='*20)
    print('\n'.join(rows))
    print('Occupancy:', occ)
    print('='*20)


def part1(lines: [str] = None) -> int:
    if not lines:
        with open('day11.input', 'r') as f:
            lines = f.read()

    # Separate by line
    lines = lines.splitlines()

    # This is necessary because we can't reassign characters in a string.
    seats = [[char for char in row] for row in lines]

    last = 0
    current = -1

    iterations = 0

    # Run the simulation until last == current
    while last != current:
        last = current
        seats, current = simulate_once_part1(seats)
        iterations += 1

    print(f'Solved simulation in {iterations} iterations.')

    return current


def get_first_visible(seats, row, col):
    """ Returns the sum of the first visible seats
    in each direction from a particular seat r, c."""
    total_rows = len(seats)
    total_cols = len(seats[0])

    visible = 0

    directions = [(v, h) for v, h in itertools.product(range(-1, 2), repeat=2)]
    directions.remove((0, 0))

    # For each direction, traverse until we hit a boundary or an occupied seat.
    for direction in directions:
        r = row + direction[0]
        c = col + direction[1]

        # Boundary check
        while 0 <= r < total_rows and 0 <= c < total_cols:
            if seats[r][c] == '#':
                visible += 1
                # All other neighbors in this direction are obstructed, so we're done.
                break

            elif seats[r][c] == 'L':
                # This chair sees an empty seat. Move on
                break

            # Do it again one step further out.
            r += direction[0]
            c += direction[1]

    return visible


def simulate_once_part2(seats):
    total_rows = len(seats)
    total_cols = len(seats[0])
    changes = []

    for r, c in itertools.product(range(total_rows), range(total_cols)):
        if seats[r][c] == '.':
            continue

        # Get sum of first visible neighbors in each direction.
        neighbors = get_first_visible(seats, r, c)

        # Next, see if this seat needs to change.
        if seats[r][c] == 'L' and neighbors == 0:
            changes.append((r, c, '#'))

        elif seats[r][c] == '#' and neighbors >= 5:
            changes.append((r, c, 'L'))

    # Apply changes
    for r, c, new in changes:
        seats[r][c] = new

    # Count total occupied
    occupied = len([seat for row in seats for seat in row if seat == '#'])

    return seats, occupied


def part2(lines: [str] = None) -> int:
    if not lines:
        with open('day11.input', 'r') as f:
            lines = f.read()

    lines = lines.splitlines()
    seats = [[char for char in row] for row in lines]

    last = 0
    current = -1
    iterations = 0

    while last != current:
        last = current
        seats, current = simulate_once_part2(seats)
        iterations += 1

    print(f'Solved simulation in {iterations} iterations.')

    return current


if __name__ == '__main__':
    print(f'Running day 11...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')
