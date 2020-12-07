"""
Day 7 initial solution
Benjamin Wheeler
"""
import re


def parse_bags(rules: list = None) -> dict:
    """ Parse the rules and return a dictionary
    to lookup what each bag contains. """
    output = {}

    for rule in rules:
        key, val = rule.split(' bags contain ')
        val = {k: int(v) for v, k in re.findall(r'(\d+) (\D+) bag', val)}
        output[key] = val

    return output


def find_bag(rules: dict, bag: str, key: str) -> bool:
    """ Recursive function to find a given
    bag key from the startinng bag."""
    # Base: key is in this bag.
    if key in rules[bag].keys():
        return True
    # Base: bag is empty
    elif not rules[bag]:
        return False
    # Recursive: Search through each subsequent bag (DFS) for the key.
    # (Iterates through each key in rules[bag])
    found = False
    for next_bag in rules[bag]:
        found |= find_bag(rules, next_bag, key)

    return found


def tally_bags(rules: dict, bag: str) -> int:
    """ Recursively returns the total number of bags a bag
    contains, including the bag itself. """
    # Base: bag is empty.
    if not rules[bag]:
        # Return the bag itself.
        return 1

    # Recursive: DFS through the rest of the bags.
    total = 0
    for b, num in rules[bag].items():
        temp = tally_bags(rules, b)
        total += temp * num

    # Return the bag itself plus every bag inside it.
    return total + 1


def part1(rules: str = None) -> int:
    if rules is None:
        with open('day7.input', 'r') as f:
            rules = f.read()

    rules = rules.splitlines()
    rules = parse_bags(rules)

    total_bags = 0

    for bag in rules:
        if find_bag(rules, bag, 'shiny gold'):
            total_bags += 1

    return total_bags


def part2(rules: str = None) -> int:
    if rules is None:
        with open('day7.input', 'r') as f:
            rules = f.read()

    rules = rules.splitlines()
    rules = parse_bags(rules)

    # Tally up every bag inside the shiny gold bag (but not including the shiny gold bag).
    return tally_bags(rules, 'shiny gold') - 1


if __name__ == '__main__':
    print(f'Running day 7...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')
