"""
Day 9 initial solution
Benjamin Wheeler
"""


def part1() -> int:
    with open('day9.input', 'r') as f:
        nums = [int(line) for line in f.read().splitlines()]

    # preamble is 25 lines
    for i in range(25, len(nums)):
        # Get previous group.
        prev_group = nums[i - 25:i]
        the_sum = nums[i]

        # Find two numbers in the previous group that add up to the current num.
        for f in prev_group:
            to_find = the_sum - f
            if to_find in prev_group:
                break
        else:
            return the_sum


def part2() -> int:
    with open('day9.input', 'r') as f:
        nums = [int(line) for line in f.read().splitlines()]

    num_to_find = 507622668  # Answer from part 1

    for base in range(len(nums)):
        for end in range(base, len(nums)):
            if sum(subset := nums[base:end]) == num_to_find:
                return min(subset) + max(subset)


if __name__ == '__main__':
    print(f'Running day 9...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

