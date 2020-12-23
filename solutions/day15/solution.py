"""
Day 15 initial solution
Benjamin Wheeler
"""


def part1(starting_nums=None) -> int:
    if not starting_nums:
        with open('day15.input', 'r') as f:
            starting_nums = f.read()

    # Format numbers as integers.
    starting_nums = [int(n) for n in starting_nums.split(',')]

    # A dictionary that keeps track of the round on which each word was spoken.
    record = {k: v for v, k in enumerate(starting_nums, start=1)}
    # record = {}

    # Keeps track of the last spoken word (to check the record dict).
    last_spoken = starting_nums[-1]

    del record[last_spoken]

    # Use a round number to keep track of age (yes, rounds start at one!)
    starting_round = len(starting_nums) + 1  # Excludes last num which was deleted from the record.
    for turn in range(starting_round, 2020+1):
        try:
            # Calculate when the last time this word was spoken was.
            age = turn - 1 - record[last_spoken]

            last_spoken = age

            # Record this word's new turn number.
            record[last_spoken] = turn

        except KeyError:
            # The word has not yet been spoken.
            # Record new word.
            record[last_spoken] = turn
            last_spoken = 0

        print(last_spoken)

    return last_spoken


def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Running day 15...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

