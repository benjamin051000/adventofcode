"""
Advent of Code 2023
Day 5 solution
Author: Benjamin Wheeler
"""

# TODO return type hint
def create_map(text: str):
    lines = text.splitlines()

    # First, obtain the mapping.
    range_from_to_text = lines.pop(0).split(' ')[0].split('-')
    range_from, range_to = range_from_to_text[0], range_from_to_text[-1]


def part1(text: str) -> int:
    paragraphs = text.split("\n\n")

    seeds = paragraphs.pop(0)
    maps = []
    for paragraph in paragraphs:
        maps.append(create_map(paragraph))


    return 0


def part2(text: str) -> int:
    lines = text.splitlines()
    return 0

def main():
    print(f'Running day 5...')

    with open('day05_input.txt') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

if __name__ == '__main__':
    main()
