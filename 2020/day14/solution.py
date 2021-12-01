"""
Day 14 initial solution
Benjamin Wheeler
"""
import re
import numpy as np


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
            mask = instruction.split('=')[1]

            # Make two versions of the mask for and (clear bits) and or (set bits)
            and_mask = int(mask.replace('X', '1'), 2)
            or_mask = int(mask.replace('X', '0'), 2)

        elif instruction.startswith('mem'):
            addr, data = map(int, re.match(r'mem\[(\d+)\] = (\d+)', instruction).groups())
            data &= and_mask
            data |= or_mask

            memory[addr] = data

    return sum(memory.values())


def get_addrs(mask, idx=0):
    # Base case: Exhausted string
    if idx >= len(mask):
        return mask

    try:
        new_idx = mask.index('X', idx+1)
    except ValueError:
        # We've exhausted the string.
        new_idx = len(mask)

    # Recursive case
    sub_masks = []

    # Replace this X with 0 and 1.
    on = mask[:idx] + '1' + mask[idx+1:]
    off = mask[:idx] + '0' + mask[idx + 1:]

    sub_masks.append(get_addrs(on, new_idx))
    sub_masks.append(get_addrs(off, new_idx))

    return sub_masks


def part2(instructions=None) -> int:
    if not instructions:
        with open('day14.input', 'r') as f:
            instructions = f.read()
    instructions = instructions.splitlines()

    mask = 0

    # A dict of that holds memory values in the same format as the input file.
    memory = {}

    for instruction in instructions:
        if instruction.startswith('mask ='):
            mask = instruction.split('=')[1].strip()

        elif instruction.startswith('mem'):
            raw_addr, data = re.match(r'mem\[(\d+)\] = (\d+)', instruction).groups()

            # Apply the bitmask.
            result = []
            raw_addr = format(int(raw_addr), 'b').zfill(36)

            for a, m in zip(raw_addr, mask):
                if m == 'X':
                    result.append('X')
                else:
                    result.append(int(a) | int(m))

            result = ''.join(map(str, result))

            # Place the data in ALL addresses from the mask.
            all_masks = get_addrs(result, result.index('X'))
            # Make iteration easier by flattening the array to one dimension.
            all_masks = np.array(all_masks).flatten()

            for addr in all_masks:
                memory[addr] = int(data)

    return sum(memory.values())


if __name__ == '__main__':
    print(f'Running day 14...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

