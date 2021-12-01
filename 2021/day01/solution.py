"""
Day 1 solution
Benjamin Wheeler
"""


def part1(lines=None) -> int:
    if not lines:
        with open('day01.input') as f:
            lines = f.read()
    
    numbers = [int(line) for line in lines.splitlines()]
    
    prev_number = numbers[0]
    count = 0

    for curr_number in numbers[1:]:
        if curr_number > prev_number:
            count += 1
        
        prev_number = curr_number
    
    return count


def part2(lines=None) -> int:
    if not lines:
        with open('day01.input') as f:
            lines = f.read()
    
    numbers = [int(line) for line in lines.splitlines()]

    prev_window = numbers[0:3]
    count = 0

    for idx, num in enumerate(numbers[1:]):
        curr_window = numbers[idx:idx+3]
        
        if sum(curr_window) > sum(prev_window):
            count += 1

        prev_window = curr_window
    
    return count


if __name__ == '__main__':
    print(f'Running day 1...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

