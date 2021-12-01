"""
Day 16 initial solution
Benjamin Wheeler
"""
import re
import itertools
import numpy as np

def parse_rules(text: str):
    # Parse the text to get the rules.
    RULE_PATTERN = re.compile(r"(\w+): (\d+)-(\d+) or (\d+)-(\d+)")
    rules_text = re.findall(RULE_PATTERN, text)
    
    # Enumerate rules into sets.
    rules = []
    for rule in rules_text:
        first = set(range(int(rule[1]), int(rule[2])+1))
        second = set(range(int(rule[3]), int(rule[4])+1))
        rules.append((rule[0], first | second))
    
    return rules


def is_invalid(ticket, rules) -> int:
    """
    Determines if a ticket is invalid. 
    Returns the value 0 if valid, or the number 
    on the ticket which makes it invalid.
    """
    nums = map(int, ticket.split(','))
    for num in nums:
        for rule in rules:
            # Check if this num fits here.
            if num in rule[1]:
                # This ticket could be valid.
                break
        else:
            # This number doesn't work with any rule. Ticket is certainly invalid.
            return num
    
    # All the numbers match up to at least one. Return 0 for valid.
    return 0


def part1(text: str) -> int:    
    error_rate = 0
    rules = parse_rules(text)

    # Get the lines of tickets.
    nearby_tix = text.partition("nearby tickets:\n")[2].splitlines()
    
    for ticket in nearby_tix:
        error_rate += is_invalid(ticket, rules)

    return error_rate


def part2(text: str) -> int:
    rules = parse_rules(text)

    # Get the lines of tickets.
    nearby_tix_text = text.partition("nearby tickets:\n")[2].splitlines()
    # Remove all invalid tickets.
    valid_tickets = [t for t in nearby_tix_text if not is_invalid(t, rules)]
    
    # Get all permutations of the rules.
    rule_perms = itertools.permutations(rules)
    
    # Record of failed attempts for branch pruning.
    # failed_attempts = {}

    # Bipartite Graphs have ONE unique perfect match (one rule that only works with one column). Let's find it.
    ticket_matrix = np.array([list(map(int, t.split(','))) for t in valid_tickets])
    for rule in rules:
        # One of these should fit exactly 1 column in the graph.
        # Try each column of the array.
        for c in range(len(ticket_matrix[0])):
            col: np.ndarray = ticket_matrix[:,c]

            test = [val in rule[1] for val in col]
            if all(test):
                # This is the one!
                print('found it!')
        else:
            print('didnt find it anywhere')
    
    # # At least one permutation of the rules should work for all tickets.
    # for i, perm in enumerate(rule_perms):
    #     print(f'attempt {i}')
    #     # Should we skip this permutation?
    #     skip = False
    #     for rule_idx, rule in enumerate(perm):
    #         if rule[0] in failed_attempts:
    #             if rule_idx in failed_attempts[rule[0]]:
    #                 skip = True
    #     if skip:
    #         continue
        
    #     # Try for all tickets.
    #     for ticket in valid_tickets:
    #         nums = map(int, ticket.split(','))
    #         # Does this one work with the same permutation?
    #         b = [num in rule[1] for num, rule in zip(nums, perm)]
    #         if not all(b):
    #             # It didn't work. 
    #             # Which caused it to fail? Record this mapping so we can skip later
    #             idx = b.index(False)
    #             corr_rule = perm[idx]  # Corresponding rule
    #             try:
    #                 failed_attempts[corr_rule[0]].append(idx)
    #             except KeyError:
    #                 failed_attempts[corr_rule[0]] = [idx]
                
    #             print(f'{failed_attempts=}')
    #             # Start over with a new permutation.
    #             break
    #     else:
    #         # We made it to the end. This must be the proper permutation.
    #         print(perm)




if __name__ == '__main__':
    # Read input file
    with open('day16.input', 'r') as f:
        text = f.read()

    print(f'Running day 16...')
    answer = part1(text)
    print('Part 1:', answer)

    from textwrap import dedent
    text = dedent("""\
        class: 0-1 or 4-19
        row: 0-5 or 8-19
        seat: 0-13 or 16-19

        your ticket:
        11,12,13

        nearby tickets:
        3,9,18
        15,1,5
        5,14,9
    """)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')
