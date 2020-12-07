"""
Day 6 initial solution
Benjamin Wheeler
"""
from string import ascii_lowercase


def part1() -> int:
    with open('day6.input', 'r') as f:
        questions = f.read().splitlines()

    total_yes = 0

    # Split the groups by the empty lines.
    answered_yes = set()
    for line in questions:
        if line == '':
            total_yes += len(answered_yes)
            answered_yes = set()
            continue

        # Iterate through each character on the line
        # and add it to the total answered yes.
        answered_yes |= {c for c in line}

    # Add the last iteration to the total.
    return total_yes + len(answered_yes)


def part2(questions=None) -> int:
    if questions is None:
        with open('day6.input', 'r') as f:
            questions = f.read().splitlines()
    else:
        questions = questions.splitlines()

    total_yes = 0

    starting_set = {c for c in ascii_lowercase}

    everyone_yes = starting_set.copy()
    for line in questions:
        if line == '':
            total_yes += len(everyone_yes)
            everyone_yes = starting_set.copy()
            continue

        everyone_yes &= {c for c in line}

    return total_yes + len(everyone_yes)


if __name__ == '__main__':
    print(f'Running day 6...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

