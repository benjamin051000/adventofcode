"""
Day 11 tests
Benjamin Wheeler
"""
from textwrap import dedent
from day11.solution import part1, part2, get_first_visible


def test_example1():
    example = dedent("""\
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """)
    assert part1(example) == 37

    assert part2(example) == 26


def test_part1():
    assert part1() == 2361


def test_first_visible():
    """ Tests the get_first_visible function in part 2. """
    examples = [
        dedent("""\
        .......#.
        ...#.....
        .#.......
        .........
        ..#L....#
        ....#....
        .........
        #........
        ...#.....
        """),

        dedent("""\
        .............
        .L.L.#.#.#.#.
        .............
        """),

        dedent("""\
        .##.##.
        #.#.#.#
        ##...##
        ...L...
        ##...##
        #.#.#.#
        .##.##.
        """)
    ]

    test_chair = [(4, 3), (1, 1), (3, 3)]

    answers = [8, 0, 0]  # Second entry sees one empty seat, but zero occupied seats.

    for ex, ans, (r, c) in zip(examples, answers, test_chair):
        # Construct 2D list
        seats = [[char for char in row] for row in ex.splitlines()]

        assert get_first_visible(seats, r, c) == ans


def test_part2():
    pass

