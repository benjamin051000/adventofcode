"""
Day 6 tests
Benjamin Wheeler
"""
import textwrap
from day6.solution import part1, part2


def test_part2_sample_input():
    sample_input = textwrap.dedent(""" \
        abc
        
        a
        b
        c
        
        ab
        ac
        
        a
        a
        a
        a
        
        b
    """)
    assert part2(sample_input) == 6


def test_part1():
    assert part1() == 6443


def test_part2():
    assert part2() == 3232

