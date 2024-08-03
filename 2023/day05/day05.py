"""
Advent of Code 2023
Day 5 solution
Author: Benjamin Wheeler
"""
from dataclasses import dataclass
from typing import List, Tuple
    
@dataclass
class Map:
    from_: str
    to: str
    mappings: List[Tuple[int, int, int]]


def create_map(text: str) -> Map:
    lines = text.splitlines()

    # First, obtain the mapping.
    from_to_text = lines.pop(0).split(' ')[0].split('-')

    # Remove "to"
    assert from_to_text.pop(1) == "to"

    # range_from, range_to = from_to_text

    # Set up the mappings
    mappings: List[Tuple[int, int, int]] = []
    for line in lines:
        dest_range_start, source_range_start, range_len = [int(x) for x in line.split()]
        mappings.append((dest_range_start, source_range_start, range_len))


    # Put it all into one data structure (how?) and return
    return Map(*from_to_text, mappings)  # type: ignore

# def convert_between_ranges(source_range_start, dest_range_start, range_len, input: int) -> int:
    # return input - source_range_start

def traverse_maps(maps: List[Map], seed: int) -> int:
    breakpoint()
    # old = seed
    # new = -1 # Sentinel value, haven't started yet
    val = seed
    for map in maps:
        # Look at the mappings to get the next one.
        for dest_range_start, source_range_start, range_len in map.mappings:
            # Check each mappings' ranges to see if it fits.
            if val in range(source_range_start, range_len):
                # Perform the transformation
                val = val - source_range_start + dest_range_start

        else:
            # new = old
            pass

    # return new
    return val


def part1(text: str) -> int:
    paragraphs = text.split("\n\n")

    seeds = [int(x) for x in paragraphs.pop(0).split()[1:]]
    maps: List[Map] = []
    for paragraph in paragraphs:
        maps.append(create_map(paragraph))

    # For part 1, we want the least location number.
    return min(traverse_maps(maps, seed) for seed in seeds)


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
