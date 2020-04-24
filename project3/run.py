"""
Project 3

- FSudoku
"""
import os.path

from sudoku import Sudoku


class Run(object):
    """
    Run project 3's tasks
    """

    def sudoku_game(self):
        print("SUDOKU\n------")

        _ = Sudoku.empty
        sudoku = Sudoku()

        # problem 1
        board = [
            [3, _, 4, _],
            [_, 2, _, 3],
            [_, _, _, _],
            [_, 4, _, 1],
        ]

        sudoku.setboard(board)

        print("\nBoard")
        sudoku.print()

        if sudoku.solve():
            print("\nSolution")
            sudoku.print()
        else:
            print("Invalid board")

        # problem 2
        board = [
            [_, _, _, _, _, _, 2, _, _],
            [_, 8, _, _, _, 7, _, 9, _],
            [6, _, 2, _, _, _, 5, _, _],
            [_, 7, _, _, 6, _, _, _, _],
            [_, _, _, 9, _, 1, _, _, _],
            [_, _, _, _, 2, _, _, 4, _],
            [_, _, 5, _, _, _, 6, _, 3],
            [_, 9, _, 4, _, _, _, 7, _],
            [_, _, 6, _, _, _, _, _, _]
        ]

        sudoku.setboard(board)

        print("\nBoard")
        sudoku.print()

        if sudoku.solve():
            print("\nSolution")
            sudoku.print()
        else:
            print("Invalid board")


if __name__ == "__main__":
    Run().sudoku_game()
