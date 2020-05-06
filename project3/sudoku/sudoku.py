import math


class Sudoku(object):
    """
    Sudoku puzzle solver.

    Time complexity: O(n^m)
        n = # possibilities in each square, m = # blank spaces in board
        Ex: For 9x9, O(9^m)
    """
    # Value for empty node in board
    empty = 0

    def __init__(self, board=None):
        """
        Parameters
        ----------
        board (array): 2D array with dimensions that are perfect square
        """
        self.size = 9
        self.box = 3
        self.board = board
        self._update_dimensions()

    def setboard(self, board):
        """Set a new board and update dimensions"""
        self.board = board
        self._update_dimensions()

    def _update_dimensions(self):
        """Update dimensions from board"""
        if self.board:
            self.size = len(self.board)
            self.box = int(math.sqrt(self.size))
            assert self.box * self.box == self.size

    def solve(self, node=(0, 0)):
        """Solve Sudoku: backtracking algorithm"""
        # Find an empty node
        node = self._find_empty(node)

        if node:
            row, col = node
            next_node = self._next(node)

            # Try every number
            for number in range(1, self.size + 1):
                # Check if node with number is promising
                if self._is_promising(row, col, number):
                    self.board[row][col] = number

                    # Recur to next node
                    if self.solve(next_node):
                        return True
                    # Unmark node if recursion path fails
                    else:
                        self.board[row][col] = Sudoku.empty

            # Current path fails when all numbers are exhausted
            return False
        else:
            # No more empty nodes means the Sudoku puzzle is solved
            return True

    def _find_empty(self, node):
        """Find an empty node. Return tuple of (row, col) else None"""
        row, col = node

        for i in range(row, self.size):
            for j in range(col, self.size):
                if self.board[i][j] == Sudoku.empty:
                    return i, j
            col = 0
        return None

    def _next(self, node):
        """Return next node indices"""
        row, col = node

        if col == self.size - 1:
            row, col = row + 1, 0
        else:
            col += 1

        return row, col

    def _is_promising(self, row, col, number):
        """Check if node with number is promising"""
        return self._not_in_row(row, number) and\
            self._not_in_col(col, number) and\
            self._not_in_box(row, col, number) and\
            self.board[row][col] == Sudoku.empty

    def _not_in_row(self, row, number):
        """Check number is not in row"""
        return number not in self.board[row]

    def _not_in_col(self, col, number):
        """Check number is not in column"""
        for i in range(self.size):
            if self.board[i][col] == number:
                return False
        return True

    def _not_in_box(self, row, col, number):
        """Check number is not in box"""
        row = row - row % self.box
        col = col - col % self.box

        for i in range(self.box):
            for j in range(self.box):
                if self.board[row+i][col+j] == number:
                    return False
        return True

    def print(self):
        """Print sudoku board"""
        if self.board:
            pad = len(str(self.size))

            for i in range(self.size):
                if i % self.box == 0 and i != 0:
                    for j in range(self.box):
                        if j != self.box - 1:
                            print("-" * (self.box * (pad+1)) + "+-", end="")
                        else:
                            print("-" * (self.box * (pad+1) - 1), end="")
                    print()

                for j in range(self.size):
                    if j % self.box == 0 and j != 0:
                        print("| ", end="")
                    print(f"{self.board[i][j]:^{pad}} ", end="")
                print()
