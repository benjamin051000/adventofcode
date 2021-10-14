"""
Day 16 initial solution
Benjamin Wheeler
"""
import re
import itertools

def part1(text: str = None) -> int:
    if text is None:
        with open('day16.input', 'r') as f:
            text = f.read()
    
    error_rate = 0

    # Parse the text to get the rules.
    RULE_PATTERN = re.compile(r"(\w+): (\d+)-(\d+) or (\d+)-(\d+)")
    rules_text = re.findall(RULE_PATTERN, text)
    
    # Enumerate rules into sets.
    rules = []
    for rule in rules_text:
        first = set(range(int(rule[1]), int(rule[2])+1))
        second = set(range(int(rule[3]), int(rule[4])+1))
        rules.append((rule[0], first | second))

    # Get the lines of tickets.
    nearby_tix = text.partition("nearby tickets:\n")[2].splitlines()
    
    for ticket in nearby_tix:
        nums = map(int, ticket.split(','))
        for num in nums:
            for rule in rules:
                # Check if this num fits here.
                if num in rule[1]:
                    # This ticket could be valid.
                    break
            else:
                # This number doesn't work with any rule. Ticket is certainly invalid.
                error_rate += num

    return error_rate



def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Running day 16...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

