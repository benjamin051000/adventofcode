"""
Day 15 initial solution
Benjamin Wheeler
"""


def part1(starting_nums=None, max_round=2020) -> int:
    if not starting_nums:
        with open('solutions/day15/day15.input', 'r') as f:
            starting_nums = f.read()

    # Format numbers as integers.
    spoken_nums = [int(n) for n in starting_nums.split(',')]
    # If rounds has 5 elements, next round is 6.
    round_num = len(spoken_nums) + 1

    while len(spoken_nums) < max_round:
        # Look at previously spoken number
        prev_num = spoken_nums[-1]

        # Has it been spoken before?
        # Traverse backwards thru list to find next most recent spoken
        for k in range(round_num-2, 0, -1):
            if spoken_nums[k-1] == prev_num:
                # Take difference between these rounds
                diff = (round_num-1) - (k-1) - 1
                spoken_nums.append(diff)
                break
        else:
            # Last time was first time. Say 0.
            spoken_nums.append(0)
        
        round_num += 1
    
    return spoken_nums[-1]

    


def part2(starting_nums=None) -> int:
    # return part1(max_round=30_000_000)
    if not starting_nums:
        with open('solutions/day15/day15.input', 'r') as f:
            starting_nums = f.read()

    # Format numbers as integers.
    starting_rounds = [int(n) for n in starting_nums.split(',')]

    # Hold a record of numbers that have been spoken, and a list of rounds they were spoken in.
    word_rec = {word:[rd] for rd,word in enumerate(starting_rounds, start=1)}
    
    # Initial round number
    round_num = len(word_rec)+1

    # Initial last word
    last_word = starting_rounds[-1]
    
    # Run for 30M rounds.
    while round_num <= 30_000_000:
        # Look at previous word.
        # Has this word been spoken previously?
        prev_times = word_rec.get(last_word) or [-1]  # [-1] dummy value for if num has never been spoken

        if len(prev_times) == 1:
            # This word has only been spoken once.
            #print(f'Last round was first time {last_word} was spoken. Speaking 0.')
            word_rec[0].append(round_num)
            last_word = 0
        else:
            # Has been spoken multiple times.
            # Take difference of previous 2 times
            diff = prev_times[-1] - prev_times[-2]
            
            # Add new word to record
            try:
                word_rec[diff].append(round_num)
            except KeyError:
                word_rec[diff] = [round_num]
            
            last_word = diff
        
        round_num += 1
    
    return last_word
        





if __name__ == '__main__':
    print(f'Running day 15...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

