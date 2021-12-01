"""
Day 12 initial solution
Benjamin Wheeler
"""
import turtle


def part1(directions=None) -> int:
    if not directions:
        with open('day12.input', 'r') as f:
            directions = f.read()

    directions = directions.splitlines()

    # Utilize a Turtle to follow the instructions!
    s = turtle.Screen()
    s.screensize(1200, 1600)

    t = turtle.Turtle()

    movements = {
        'N': lambda dist: t.sety(t.ycor() + dist),
        'S': lambda dist: t.sety(t.ycor() - dist),
        'E': lambda dist: t.setx(t.xcor() + dist),
        'W': lambda dist: t.setx(t.xcor() - dist),
        'L': lambda deg: t.left(deg),
        'R': lambda deg: t.right(deg),
        'F': lambda dist: t.forward(dist)
    }

    for direction in directions:
        command, *arg = direction
        arg = int(''.join(arg))

        # Run the command
        movements[command](arg)

    # print('Turtle is done, you can now close the window.')
    # turtle.done()

    # Return the Manhattan distance.
    return abs(int(t.xcor())) + abs(int(t.ycor()))


if __name__ == '__main__':
    print(f'Running day 12...')
    answer = part1()
    print('Part 1:', answer)

    print('Done.')

