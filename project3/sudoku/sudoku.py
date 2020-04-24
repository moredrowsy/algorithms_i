class Sudoku(object):
    """
    Sudoku puzzle solver
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

    def solve(self):
        """Solve Sudoku: backtracking algorithm"""
        # Find an empty node
        node = self._find_empty_node()

        if node:
            row, col = node

            # Try every number
            for number in range(1, self.size + 1):
                # Check if node with number is promising
                if self._is_promising(node, number):
                    self.board[row][col] = number

                    # Recurse to next node
                    if self.solve():
                        return True
                    # Unmark node if recursion path fails
                    else:
                        self.board[row][col] = Sudoku.empty

            # Current path fails when all numbers are exhausted
            return False
        else:
            # No more empty nodes means the Sudoku puzzle is solved
            return True

    def _find_empty_node(self):
        """Find an empty node in board. Return tuple of (row, col) else None"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == Sudoku.empty:
                    return i, j
        return None

    def _is_promising(self, node, number):
        """Check if node with number is valid/promising"""
        return self._is_valid_row(node[0], number) and\
            self._is_valid_col(node[1], number) and\
            self._is_valid_box(node, number) and\
            self.board[node[0]][node[1]] == Sudoku.empty

    def _is_valid_row(self, row, number):
        """Check row has no number"""
        return False if number in self.board[row] else True

    def _is_valid_col(self, col, number):
        """Check column has no number"""
        for i in range(self.size):
            if self.board[i][col] == number:
                return False
        return True

    def _is_valid_box(self, node, number):
        """Check box has no number"""
        row, col = node
        row = row - row % self.box
        col = col - col % self.box

        for i in range(self.box):
            for j in range(self.box):
                if self.board[i + row][j + col] == number:
                    return False
        return True

    @staticmethod
    def print_board(board):
        n = len(board)

        for i in range(n):
            for j in range(n):
                print(f"{board[i][j]} ", end="")
            print()
