"""
Day 5 initial solution
Benjamin Wheeler
"""
from dataclasses import dataclass


@dataclass
class Seat:
    bot: int
    top: int


def get_row_col(seat: str) -> (int, int):
    max_row, max_col = 127, 7  # Constants
    r = Seat(0, max_row)
    c = Seat(0, max_col)

    for command in seat:
        r_dist = r.top - r.bot + 1
        c_dist = c.top - c.bot + 1
        if command == 'F':
            # Take lower half.
            r.top -= r_dist // 2

        elif command == 'B':
            # Take upper half.
            r.bot += r_dist // 2

        elif command == 'R':
            # Take upper half.
            c.bot += c_dist // 2

        elif command == 'L':
            # Take lower half.
            c.top -= c_dist // 2

    return r.bot, c.top


def part1() -> int:
    with open('day5.input', 'r') as f:
        seats = f.read().splitlines()

    seat_num = []
    for seat in seats:
        r, c = get_row_col(seat)
        seat_num.append(r * 8 + c)

    return max(seat_num)


def part2() -> int:
    with open('day5.input', 'r') as f:
        seats = f.read().splitlines()

    # Get all pairs of seats.
    occupied_seats = set()
    for seat in seats:
        r, c = get_row_col(seat)
        occupied_seats.add((r, c))

    # Get all seats not in this set of seats.
    all_seats: set = {(r, c) for c in range(8) for r in range(128)}

    # Get IDs of each unoccupied seat.
    unoccupied = [r * 8 + c for r, c in all_seats - occupied_seats]

    # Search for a seat with no empty neighbors.
    temp = set(unoccupied)
    for seat in temp:
        if seat + 1 not in temp and seat - 1 not in temp:
            return seat

    else:
        return -1


if __name__ == '__main__':
    print(f'Running day 5...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

