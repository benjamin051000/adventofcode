"""
new_day.py
Generates a directory for a new day automatically.
Provides one solution.py file as well as a testfile.

Benjamin Wheeler
"""
import os
import textwrap

if __name__ != '__main__':
    raise ImportError('This is not an importable module!')

# Get the days, which are all folders.
days = os.listdir('solutions')
numbers = [int(i.strip('day')) for i in days]

# New day number
day_num = max(numbers) + 1

print(f'Generating \'day{day_num}\'...')

# The name of the new directory from the root directory.
directory = f'solutions/day{day_num}'
os.mkdir(directory)

# Write the solution file
with open(f'{directory}/solution.py', 'w') as f:
    f.write(textwrap.dedent(f"""\
        \"\"\"
        Day {day_num} solution
        Benjamin Wheeler
        \"\"\"
    
    
        def part1():
            pass
        
        
        def part2():
            pass
        
    """))


# Write the input file and README file
with open(f'{directory}/day{day_num}.input', 'w') as f:
    pass


with open(f'{directory}/README.md', 'w') as f:
    f.write(textwrap.dedent(f"""\
        # Day {day_num}
        
        ## Part 1
        
        
        
        ## Part 2

        
    """))


# Write the test file
with open(f'{directory}/day{day_num}_test.py', 'w') as f:
    f.write(textwrap.dedent(f"""\
            \"\"\"
            Day {day_num} tests
            Benjamin Wheeler
            \"\"\"
            from day{day_num}.solution import part1, part2

            def test_part1():
                pass


            def test_part2():
                pass

        """))
