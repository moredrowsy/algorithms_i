"""
Backtracking Algorithms

- nQueens
"""
from nqueens import nqueens


class Run(object):
    """
    Run Backtracking Algorithms
    """

    def n_queens(self):
        print("\nN-QUEENS\n--------")

        board_size = 4
        print(f"\nBoard size: {board_size}")
        nqueens(board_size)


if __name__ == "__main__":
    Run().n_queens()
