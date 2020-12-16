"""
Day 12 initial solution
Benjamin Wheeler
"""
from math import sin, cos, radians

import numpy as np


class Turtle:
    """ Basically a vector class, same functionality
     as the STL turtle but with no GUI. """

    def __init__(self):
        self.x = 0
        self.y = 0

    def pos(self):
        return self.x, self.y

    def position(self):
        return self.pos()

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def setposition(self, *coords):
        try:
            self.x, self.y = coords
        except ValueError:
            self.x, self.y = coords[0]

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y

    def __repr__(self):
        return f'({self.x}, {self.y})'


def rotate_waypoint(t, w, deg):
    """ Rotate the waypoint a certain amount
    of degrees around the ship via
    good ol' linear transformations.
    Negative angles are clockwise,
    positive angles are counterclockwise. """

    # Convert to radians for the sin and cos functions.
    deg = radians(deg)

    trans = np.array([[round(cos(deg)), round(-sin(deg))],
                      [round(sin(deg)), round(cos(deg))]])
    # Define a vector between waypoint and ship.
    start = np.array(w.position()) - np.array(t.position())

    # Perform a matrix-vector multiplication.
    out_vec = np.matmul(trans, start)

    # Move waypoint to new location.
    end = t.position() + out_vec
    w.setposition(end)


def move_toward_waypoint(t: Turtle, w, n):
    """ Move toward waypoint n times. """
    # Get vector from w -> t
    start = np.array(w.pos()) - np.array(t.pos())  # pos() == position()

    # Scale by n (to move toward tip of vector)
    end_vec = start * n

    # Move both the ship and the waypoint along the final vector.
    t.setposition(np.array(t.pos()) + end_vec)
    w.setposition(np.array(w.pos()) + end_vec)


def part2(directions=None) -> int:
    if not directions:
        with open('day12.input', 'r') as f:
            directions = f.read()

    directions = directions.splitlines()

    t = Turtle()
    # Initialize waypoint
    w = Turtle()
    w.setposition(10, 1)  # t starts at (0, 0).

    movements = {
        'N': lambda dist: w.sety(w.ycor() + dist),
        'S': lambda dist: w.sety(w.ycor() - dist),
        'E': lambda dist: w.setx(w.xcor() + dist),
        'W': lambda dist: w.setx(w.xcor() - dist),
        'L': lambda deg: rotate_waypoint(t, w, deg),
        'R': lambda deg: rotate_waypoint(t, w, -deg),
        'F': lambda times: move_toward_waypoint(t, w, times)
    }

    for i, direction in enumerate(directions):
        command, *arg = direction
        arg = int(''.join(arg))

        # Run the command
        movements[command](arg)

        print('Finished command', i)

    # Return the Manhattan distance.
    return abs(int(t.xcor())) + abs(int(t.ycor()))


if __name__ == '__main__':
    print(f'Running day 12...')

    answer = part2()
    print('Part 2:', answer)

    print('Done.')

