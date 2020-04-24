import math


class Sudoku(object):
    empty = 0

    def __init__(self, board=None):
        self.board = board
        self.n = 9
        self.box = 3
        self._init_dimensions()

    def setboard(self, board):
        self.board = board
        self._init_dimensions()

    def _init_dimensions(self):
        if self.board:
            self.n = len(self.board)
            self.box = int(math.sqrt(self.n))

    def solve(self):
        # find position of empty cell
        cell = self._find_empty_cell()

        if cell:
            row, col = cell
            for number in range(1, self.n + 1):
                if self._is_promising(cell, number):
                    self.board[row][col] = number

                    if self.solve():
                        return True
                    else:
                        self.board[row][col] = Sudoku.empty
            return False
        else:
            return True

    def _find_empty_cell(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == Sudoku.empty:
                    return i, j
        return None

    def _is_promising(self, cell, number):
        return self._is_valid_row(cell[0], number) and\
            self._is_valid_col(cell[1], number) and\
            self._is_valid_box(cell, number) and\
            self.board[cell[0]][cell[1]] == Sudoku.empty

    def _is_valid_row(self, row, number):
        return False if number in self.board[row] else True

    def _is_valid_col(self, col, number):
        for i in range(self.n):
            if self.board[i][col] == number:
                return False
        return True

    def _is_valid_box(self, cell, number):
        row, col = cell
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
