"""
Day 2 initial solution
Benjamin Wheeler
"""


def part1(text=None) -> int:
    if not text:
        with open('day02.input') as f:
            text = f.read()
    
    lines = text.splitlines()
    
    x = 0  # horizontal position 
    depth = 0

    for line in lines:
        direction, mag = line.split()
        magnitude = int(mag)
        
        if direction == "up":
            depth -= magnitude
        elif direction == "down":
            depth += magnitude
        elif direction == "forward":
            x += magnitude
    
    return x * depth


def part2(text=None) -> int:
    if not text:
        with open('day02.input') as f:
            text = f.read()
    
    lines = text.splitlines()
    
    x = 0  # horizontal position 
    depth = 0
    aim = 0

    for line in lines:
        direction, mag = line.split()
        magnitude = int(mag)
        
        if direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "forward":
            x += magnitude
            depth += aim * magnitude
    
    return x * depth


if __name__ == '__main__':
    print(f'Running day 2...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

