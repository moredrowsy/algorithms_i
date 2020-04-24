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
        _ = Sudoku.empty
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

        sudoku = Sudoku()
        sudoku.setboard(board)
        if sudoku.solve():
            Sudoku.print_board(board)
        else:
            print("Invalid board")


if __name__ == "__main__":
    Run().sudoku_game()
