"""
Day 14 initial solution
Benjamin Wheeler
"""
import re


def part1(instructions=None) -> int:
    if not instructions:
        with open('day14.input', 'r') as f:
            instructions = f.read()
    instructions = instructions.splitlines()

    and_mask = 0
    or_mask = 0

    # A dict of that holds memory values in the same format as the input file.
    memory = {}

    for instruction in instructions:
        if instruction.startswith('mask ='):
            mask = instruction.split('=')[1].strip()

            # Make two versions of the mask for and (clear bits) and or (set bits)
            and_mask = int(mask.replace('X', '1'), 2)
            or_mask = int(mask.replace('X', '0'), 2)

        elif instruction.startswith('mem'):
            addr, data = map(int, re.match(r'mem\[(\d+)\] = (\d+)', instruction).groups())
            data &= and_mask
            data |= or_mask

            memory[addr] = data

    return sum(memory.values())


def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Running day 14...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

