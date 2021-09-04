"""
Day 15 initial solution
Benjamin Wheeler
"""


def part1(starting_nums=None) -> int:
    if not starting_nums:
        with open('solutions/day15/day15.input', 'r') as f:
            starting_nums = f.read()

    # Format numbers as integers.
    spoken_nums = [int(n) for n in starting_nums.split(',')]
    # If rounds has 5 elements, next round is 6.
    round_num = len(spoken_nums) + 1

    while len(spoken_nums) < 2020:
        #print('Round', round_num)

        # Look at previously spoken number
        prev_num = spoken_nums[-1]
        #print('Previous num:', prev_num)

        # Has it been spoken before?
        # Traverse backwards thru list to find next most recent spoken
        for k in range(round_num-2, 0, -1):
            #print('Checking round', k)
            if spoken_nums[k-1] == prev_num:
                # Take difference between these rounds
                diff = (round_num-1) - (k-1) - 1
                #print(f'Last round {prev_num} spoken: {k}')
                #print(f'{round_num} - {k} = {diff}')
                spoken_nums.append(diff)
                break
        else:
            # Last time was first time. Say 0.
            #print('First time. Speaking 0.')
            spoken_nums.append(0)
        
        round_num += 1
    
    print(f'{len(spoken_nums)=}')
    return spoken_nums[-1]

    


def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Running day 15...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

