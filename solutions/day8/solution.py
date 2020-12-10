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


def program_did_terminate(instructions: [str], switched: int) -> (bool, int):
    """ Returns a bool if the program terminated or not, as well as either
     a line number (in the case the program encountered an infinite loop,
     or an accumulator value (in the case the program terminated successfully)."""
    accum = 0
    line = 0
    visited = set()

    while True:
        if line in visited:
            # Return line number that broke it.
            return False, line

        # Mark line as visited.
        visited.add(line)

        # Run instruction
        try:
            ins, arg = instructions[line].split(' ')
        except IndexError:
            break

        if ins == 'nop':
            line += 1

        elif ins == 'acc':
            accum += int(arg)
            line += 1

        elif ins == 'jmp':
            # if this jump results in an infinite loop, switch it.

            line += int(arg)

    # The loop is over. Return the accumulator value.
    return True, accum


def part2() -> int:
    with open('day8.input', 'r') as f:
        instructions = f.read().splitlines()

    # Keep track of which lines have already been switched.
    switched = 0

    # Run the instructions. If the program terminates, return the value.
    # If not, add the infinite loop line and try again, switching the next
    # nop/jmp line.
    terminated, val = program_did_terminate(instructions, switched)



if __name__ == '__main__':
    print(f'Running day 8...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

