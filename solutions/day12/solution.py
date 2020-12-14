"""
Day 12 initial solution
Benjamin Wheeler
"""
import turtle
from math import sin, cos, radians, ceil

import numpy as np


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


def rotate_around_waypoint(t, w, deg):
    """ Rotate the waypoint a certain amount
    of degrees around the turtle via
    good ol' linear transformations.
    Negative angles are clockwise,
    positive angles are counterclockwise. """

    # Convert to radians for the sin and cos functions.
    deg = radians(deg)

    trans = np.array([[cos(deg), -sin(deg)],
                      [sin(deg), cos(deg)]])
    # Define a vector between waypoint and ship.
    vec = w.position() - t.position()
    start = np.array(vec)

    # Perform a matrix-vector multiplication.
    out_vec = np.matmul(trans, start)

    # Move waypoint to new location.
    end = t.position() + out_vec
    # end = map(ceil, end)
    w.setposition(end)


def move_toward_waypoint(t: turtle.Turtle, w, n):
    """ Move toward waypoint n times. """
    # Get vector from w -> t
    start = np.array(t.pos()) - np.array(w.pos())  # pos() == position()

    # Scale by negative n (to move toward tip of vector)
    end_vec = start * -n

    newpos = np.array(t.pos()) + end_vec

    t.setposition(newpos)
    # The waypoint moves with the ship.
    w.setposition(np.array(w.pos()) + end_vec)


def part2(directions=None) -> int:
    if not directions:
        with open('day12.input', 'r') as f:
            directions = f.read()

    directions = directions.splitlines()

    s = turtle.Screen()
    s.screensize(1200, 1600)

    t = turtle.Turtle()
    # Initialize waypoint
    w = turtle.Turtle()
    w.setposition(10, 1)  # t starts at (0, 0).
    w.color('green')

    movements = {
        'N': lambda dist: w.sety(w.ycor() + dist),
        'S': lambda dist: w.sety(w.ycor() - dist),
        'E': lambda dist: w.setx(w.xcor() + dist),
        'W': lambda dist: w.setx(w.xcor() - dist),
        'L': lambda deg: rotate_around_waypoint(t, w, deg),
        'R': lambda deg: rotate_around_waypoint(t, w, -deg),
        'F': lambda times: move_toward_waypoint(t, w, times)
    }

    for i, direction in enumerate(directions):
        command, *arg = direction
        arg = int(''.join(arg))

        # Run the command
        movements[command](arg)

        print('Finished command', i)

    # print('Turtle is done, you can now close the window.')
    # turtle.done()

    # Return the Manhattan distance.
    return abs(int(t.xcor())) + abs(int(t.ycor()))


if __name__ == '__main__':
    print(f'Running day 12...')
    # answer = part1()
    # print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

