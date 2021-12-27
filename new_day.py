"""
new_day.py
Generates a directory for a new day automatically.
Provides one solution.py file as well as a testfile.

Benjamin Wheeler
"""
import os
import textwrap
from sys import argv
import subprocess

# Get the days, which are all folders.
try:
    year = argv[1]
except:
    print("Supply a valid year as a command-line argument.")
    exit()

days = os.listdir(year)

ignored_dirs = [
    "__pycache__",
    ".pytest_cache",
    ".vscode",
]

numbers = [int(d.strip("day")) for d in days if d not in ignored_dirs]

if len(numbers) == 0:
    numbers = [0]

# New day number
day_num = max(numbers) + 1

day_num_str = f"{day_num:02d}"  # Format with one leading zero

print(f"Generating '{year}/day{day_num_str}' directory...")

# The name of the new directory from the root directory.
directory = f"{year}/day{day_num_str}"
os.mkdir(directory)

# Write the solution file
with open(f"{directory}/solution.py", "w") as f:
    f.write(
        textwrap.dedent(
            f"""\
        \"\"\"
        Advent of Code {year}
        Day {day_num} solution
        Author: Benjamin Wheeler
        \"\"\"
    
    
        def part1(text: str) -> int:
            lines = text.splitlines()
            return 0
        
        
        def part2(text: str) -> int:
            lines = text.splitlines()
            return 0

        def main():
            print(f'Running day {day_num}...')

            with open('day{day_num_str}.input') as f:
                text = f.read()

            answer = part1(text)
            print('Part 1:', answer)
            
            answer = part2(text)
            print('Part 2:', answer)
            
            print('Done.')
        
        if __name__ == '__main__':
            main()
    """
        )
    )


# Add input file
with open(f"{directory}/day{day_num_str}.input", "w") as f:
    pass

# Add README file
with open(f"{directory}/README.md", "w") as f:
    f.write(
        textwrap.dedent(
            f"""\
        # Day {day_num}
        
        ## Part 1
        
        
        
        ## Part 2

        
    """
        )
    )


# Write the test file
with open(f"{directory}/day{day_num}_test.py", "w") as f:
    f.write(
        textwrap.dedent(
            f"""\
            \"\"\"
            Advent of Code {year}
            Day {day_num} tests
            Author: Benjamin Wheeler
            \"\"\"
            from solution import part1, part2
            from textwrap import dedent

            text = dedent(\"\"\"\\

                \"\"\")

            def test_part1():
                assert part1(text) == 0


            def test_part2():
                assert part2(text) == 0

        """
        )
    )

# Add to git
subprocess.run(["git", "add", f"{directory}/*"])

print("Done.")
