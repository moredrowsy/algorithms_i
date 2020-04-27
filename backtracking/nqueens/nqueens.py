def nqueens(n):
    """
    Backtracking algorithm to print all valid Queen positions permutation.

    Time complexity: O(n^n)

    Parameters
    ----------
    n (int): Size of board
    """
    column = [-1] * n
    _nqueens(column, -1)


def _nqueens(column, row):
    """
    Generate all possible queens positions in a board of n x n size.
    Top level call with row = -1: _nqueens(column, -1)

    Parameters
    ----------
    column (array): 1D array that holds the column indices. The index of
        column[i] is the row index. Ex: column[1] = 2 -> node (1, 2)
    row (int): row index
    """
    if promising(column, row):
        if row == len(column) - 1:
            print("\nSolution")
            print_board(column)
        else:
            for col in range(len(column)):
                column[row + 1] = col
                _nqueens(column, row + 1)


def promising(col, k):
    """
    Check if column array is still valid by:
        1. If two queens are in the same column
        2. If two queens are in the same diagonal

    Parameters
    ----------
    col (array): 1D array that holds column indices
    k (int): k'th row index
    """
    for i in range(k):
        if col[i] != -1:
            if col[i] == col[k] or abs(col[i] - col[k]) == abs(i - k):
                return False
    return True


def print_board(column):
    """Print queens board"""
    n = len(column)
    board = [['_']*n for i in range(n)]

    for i in range(n):
        board[i][column[i]] = 'Q'

    for i in range(n):
        for j in range(n):
            print(f"{board[i][j]} ", end="")
        print()
