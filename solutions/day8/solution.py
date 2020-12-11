"""
Day 8 initial solution
Benjamin Wheeler
"""


def part1() -> int:
    with open('day8.input', 'r') as f:
        instructions = f.read().splitlines()

    accum = 0
    line = 0

    visited = set()

    # Stop before the first instruction that has already been visited once.
    while True:
        if line in visited:
            break

        # Set this line as read.
        visited.add(line)

        # Run the instruction
        ins, arg = instructions[line].split(' ')

        if ins == 'nop':
            line += 1

        elif ins == 'acc':
            accum += int(arg)
            line += 1

        elif ins == 'jmp':
            line += int(arg)

    # Loop is over
    return accum


class InfiniteLoopException(Exception):
    """ Exception used in program_did_terminate
    to signify an infinite loop error. """
    pass


def program_did_terminate(instructions: [str]) -> int:
    """ Returns a bool if the program terminated or not, as well as either
     a line number (in the case the program encountered an infinite loop,
     or an accumulator value (in the case the program terminated successfully)."""
    accum = 0
    line = 0
    visited = set()

    while True:
        if line in visited:
            # Return line number that broke it.
            raise InfiniteLoopException

        # Mark line as visited.
        visited.add(line)

        # Run instruction
        try:
            ins, arg = instructions[line].split(' ')
        except IndexError:
            # We've terminated properly.
            break

        if ins == 'nop':
            line += 1

        elif ins == 'acc':
            accum += int(arg)
            line += 1

        elif ins == 'jmp':
            line += int(arg)

    # The loop is over. Return the accumulator value.
    return accum


def part2(instructions: str = None) -> int:
    if not instructions:
        with open('day8.input', 'r') as f:
            instructions = f.read()

    instructions = instructions.splitlines()

    # Run the instructions. If the program terminates, return the value.
    # If not, add the infinite loop line and try again, switching the next
    # nop/jmp line.

    # Find the next element in the list to swap.
    next_swap = -1

    attempts = 0

    while True:
        # Start with a fresh copy of the instructions (removes previous modifications).
        ins = instructions.copy()

        attempts += 1

        # Swap the next nop/jmp instruction.
        prefixes = [e.split(' ')[0] for e in ins]

        try:
            next_nop = prefixes.index('nop', next_swap + 1)
        except ValueError:
            next_nop = len(prefixes)  # Out of bounds

        try:
            next_jmp = prefixes.index('jmp', next_swap + 1)
        except ValueError:
            next_jmp = len(prefixes)  # Out of bounds

        next_swap = min(next_nop, next_jmp)

        if ins[next_swap].startswith('nop'):
            ins[next_swap] = ins[next_swap].replace('nop', 'jmp')

        elif ins[next_swap].startswith('jmp'):
            ins[next_swap] = ins[next_swap].replace('jmp', 'nop')

        try:
            return program_did_terminate(ins)

        except InfiniteLoopException:
            if attempts > len(instructions):
                raise StopIteration(f'DNF solution after {attempts} attempts.')


if __name__ == '__main__':
    print(f'Running day 8...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

