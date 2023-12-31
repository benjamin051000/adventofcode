#!/bin/python
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
import pathlib

# Get the days, which are all folders.
try:
    year = argv[1]
    language = argv[2]
except:
    print("Usage: python new_day.py <year> <rust|py> [--dry-run]")
    exit()

days = os.listdir(year)

ignored_dirs = [
    "__pycache__",
    ".pytest_cache",
    ".vscode",
    "template.rs"
]

numbers = [int(d.strip("day")) for d in days if d not in ignored_dirs]

if len(numbers) == 0:
    numbers = [0]

# New day number
day_num = max(numbers) + 1

day_num_str = f"{day_num:02d}"  # Format with one leading zero

print(f"Generating '{year}/day{day_num_str}' directory...")

if "--dry-run" in argv:
    print("Dry run done.")
    exit()

# The name of the new directory from the root directory.
directory = f"{year}/day{day_num_str}"

if language in ["py", "python"]:
    os.mkdir(directory)

    # Write the solution file
    with open(f"{directory}/day{day_num_str}.py", "w") as f:
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

                with open('day{day_num_str}_input.txt') as f:
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
    with open(f"{directory}/day{day_num_str}_input.txt", "w") as f:
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
    with open(f"{directory}/day{day_num_str}_test.py", "w") as f:
        f.write(
            textwrap.dedent(
                f"""\
                \"\"\"
                Advent of Code {year}
                Day {day_num} tests
                Author: Benjamin Wheeler
                \"\"\"
                from day{day_num_str} import part1, part2
                from textwrap import dedent

                text = dedent(\"\"\"\\

                    \"\"\")

                def test_part1_example():
                    assert part1(text) == 0


                def test_part2_example():
                    assert part2(text) == 0


                ##############################
                # WARNING: SPOILERS AHEAD!!!
                ##############################
                def test_part1():
                    with open('day{day_num_str}_input.txt') as f:
                        text = f.read()
                    assert part1(text) == 0  # TODO replace with actual solution

                def test_part2():
                    with open('day{day_num_str}_input.txt') as f:
                        text = f.read()
                    assert part2(text) == 0  # TODO replace with actual solution
            """
            )
        )

    # Add to git
    subprocess.run(["git", "add", f"{directory}/*"])

elif language == "rust":
    print("Making Rust project...")
    subprocess.run(["cargo", "new", directory])
    # Copy template file
    subprocess.run(["cp", f"{year}/template.rs", f"{directory}/src/main.rs"])
    subprocess.run(["git", "add", directory])

# (re)create link to latest dir
pathlib.Path('./latest').symlink_to(directory)


print("Done.")
