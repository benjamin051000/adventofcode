"""
Day 3 initial solution
Benjamin Wheeler
"""


def part1():
    with open('day3.input', 'r') as f:
        slopes = f.read().splitlines()  # Removes '\n' at EOL

    trees = 0
    col = 3
    for row in slopes[1:]:
        if row[col % len(row)] == '#':
            trees += 1
        col += 3

    return trees


def part2():
    with open('day3.input', 'r') as f:
        slopes = f.read().splitlines()

    # Each pair of movements (rightward, downward)
    directions = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )

    # This is a product, so start at 1.
    total_trees = 1

    # Iterate through each path.
    for right, down in directions:
        # x and y keep track of current position
        x, y = right, down
        trees = 0
        while y < len(slopes):
            row = slopes[y]
            if row[x % len(row)] == '#':
                trees += 1
            # Move to the next position
            x += right
            y += down

        total_trees *= trees

    return total_trees


if __name__ == '__main__':
    answer = part1()
    print(answer)

    answer = part2()
    print(answer)
