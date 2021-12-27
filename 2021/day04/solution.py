"""
Advent of Code 2021
Day 4 solution
Author: Benjamin Wheeler
"""
import itertools
import numpy as np


def part1(text: str) -> int:
    # Split text by empty lines
    lines = text.split('\n\n')

    # First line is the numbers
    draws = map(int, lines.pop(0).split(','))

    # The rest are the boards
    boards = []
    for board_text in lines:
        boards.append(
            [
                [int(d) for d in l.split(' ') if d] 
                for l in board_text.splitlines()
            ]
        )

    boards = np.array(boards)
    
    # Create a 
    scores = np.full(boards.shape, False)

    # Find the board that wins first.
    for draw in draws:
        for board, score in zip(boards, scores):

            # Check each board, scratch it off.
            row, col = np.where(board == draw)
        
            if len(row) and len(col):
                # Update score
                row = row[0]  # Unpack row to get value
                col = col[0]
                score[row, col] = True

            # Check for winners (rows and columns)
            row_winners = list(map(all, score))
            col_winners = list(map(all, score.transpose()))
            if any(row_winners) or any(col_winners):
                # This is a winner!
                # Sum up unmarked ones.
                final_arr = np.where(score == True, 0, board)  # 0 for marked
                total = np.sum(final_arr)
                return total * draw  # Winning draw

    return 0


def part2(text: str) -> int:
    lines = text.splitlines()
    return 0

def main():
    print(f'Running day 4...')

    with open('day04.input') as f:
        text = f.read()

    answer = part1(text)
    print('Part 1:', answer)

    answer = part2(text)
    print('Part 2:', answer)

    print('Done.')

if __name__ == '__main__':
    main()
