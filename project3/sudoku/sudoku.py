import math


class Implication(object):
    """A sudoku cell with possibilities set"""

    def __init__(self, x, y, *args):
        self.cell = (x, y)
        self.possibilities = set()

    def __repr__(self):
        return f"({self.cell[0]}, {self.cell[1]})"


class Sudoku(object):
    """
    Sudoku puzzle solver.

    Time complexity: O(n^m)
        n = num of possibilities in each cell, m = num of blank spaces in grid
        Ex: For 9x9, O(9^m)
    """

    def __init__(self, grid=None):
        """
        Parameters
        ----------
        grid (array): 2D array with dimensions that are perfect square
        """
        self.empty = 0  # value for empty cell
        self.size = 9
        self.subgrid = 3
        self.grid = grid
        self._update_dimensions()

    def _update_dimensions(self):
        """Update dimensions from grid"""
        if self.grid:
            self.size = len(self.grid)
            self.subgrid = int(math.sqrt(self.size))
            assert self.subgrid * self.subgrid == self.size

    def set_grid(self, grid):
        """Set a new grid and update dimensions"""
        self.grid = grid
        self._update_dimensions()

    def solve(self, cell=(0, 0)):
        """Solve Sudoku: backtracking algorithm"""
        # Find an empty cell
        cell = self._find_empty(cell)

        if cell:
            row, col = cell
            next_cell = self._next(cell)

            # Try every number
            for number in range(1, self.size + 1):
                # Check if cell with number is promising
                if self._is_promising(row, col, number):
                    # try to do implication placements
                    placements = self._imply(cell, number)

                    # Recur to next cell
                    if self.solve(next_cell):
                        return True
                    # Backtrack/undo implication placements when fail
                    else:
                        self._undo_imply(placements)

            # Current path fails when all numbers are exhausted
            return False
        else:
            # No more empty cells means the Sudoku puzzle is solved
            return True

    def _imply(self, cell, number):
        """
        Reduce backtracking with implications.
        Try to imply single possibilities for each empty cell with given number.
        Will mark empty cell with single possibilty implication.
        """
        implications = []  # list of implications for all empty cells
        placements = []  # list of implication placements

        # do first placement with number
        row, col = cell
        self.grid[row][col] = number
        placements.append(Implication(*cell))
        do_implications = True

        # init implications list for empty cells
        for i in range(row, self.size):
            for j in range(col, self.size):
                if self.grid[i][j] == self.empty:
                    imp = Implication(i, j, self.grid[row][col])
                    imp.possibilities = set(p for p in range(1, self.size+1))
                    implications.append(imp)
            col = 0

        # do a round of implication placements
        while do_implications:
            # turn off do_implications
            do_implications = False

            # check every implication and try to reduce possibilities
            for imp in implications:
                if imp.possibilities:
                    row, col = imp.cell

                    # reduce possibilities in subgrid
                    y, x = row - row % self.subgrid, col - col % self.subgrid
                    for i in range(y, y + self.subgrid):
                        for j in range(x, x + self.subgrid):
                            imp.possibilities.discard(self.grid[i][j])

                    # reduce possibilities in row and col
                    for i in range(self.size):
                        imp.possibilities.discard(self.grid[row][i])
                        imp.possibilities.discard(self.grid[i][col])

                    # set placement when there's only one possibilty
                    if len(imp.possibilities) == 1:
                        self.grid[row][col] = imp.possibilities.pop()
                        placements.append(imp)

                        # do implications when there's a placement
                        do_implications = True

        return placements

    def _undo_imply(self, implications):
        """Undo implications by marking each implication cell as empty"""
        for imp in implications:
            row, col = imp.cell
            self.grid[row][col] = self.empty

    def _find_empty(self, cell):
        """Find an empty cell. Return tuple of (row, col) else None"""
        row, col = cell

        for i in range(row, self.size):
            for j in range(col, self.size):
                if self.grid[i][j] == self.empty:
                    return i, j
            col = 0
        return None

    def _next(self, cell):
        """Return next cell indices"""
        row, col = cell

        if col == self.size - 1:
            row, col = row + 1, 0
        else:
            col += 1

        return row, col

    def _is_promising(self, row, col, number):
        """Check if cell with number is promising"""
        return self._not_in_row(row, number) and\
            self._not_in_col(col, number) and\
            self._not_in_box(row, col, number) and\
            self.grid[row][col] == self.empty

    def _not_in_row(self, row, number):
        """Check number is not in row"""
        return number not in self.grid[row]

    def _not_in_col(self, col, number):
        """Check number is not in column"""
        for i in range(self.size):
            if self.grid[i][col] == number:
                return False
        return True

    def _not_in_box(self, row, col, number):
        """Check number is not in box"""
        row = row - row % self.subgrid
        col = col - col % self.subgrid

        for i in range(row, row + self.subgrid):
            for j in range(col, col + self.subgrid):
                if self.grid[i][j] == number:
                    return False
        return True

    def verify(self):
        """Verify board is solved"""
        pset = set(number for number in range(1, self.size+1))

        try:
            for i in range(self.size):
                # test row
                row_set = pset.copy()
                for col in range(self.size):
                    row_set.remove(self.grid[i][col])

                # test col
                col_set = pset.copy()
                for row in range(self.size):
                    col_set.remove(self.grid[row][i])

                # test subgrid
                subgrid_set = pset.copy()
                y = self.subgrid * (i // self.subgrid)
                x = self.subgrid * (i % self.subgrid)
                for row in range(y, y + self.subgrid):
                    for col in range(x, x + self.subgrid):
                        subgrid_set.remove(self.grid[row][col])
        except KeyError:
            return False

        return True

    def print(self):
        """Print sudoku grid"""
        if self.grid:
            pad = len(str(self.size))

            for i in range(self.size):
                if i % self.subgrid == 0 and i != 0:
                    for j in range(self.subgrid):
                        if j != self.subgrid - 1:
                            print("-" * (self.subgrid*(pad+1)) + "+-", end="")
                        else:
                            print("-" * (self.subgrid*(pad+1) - 1), end="")
                    print()

                for j in range(self.size):
                    if j % self.subgrid == 0 and j != 0:
                        print("| ", end="")
                    print(f"{self.grid[i][j]:^{pad}} ", end="")
                print()
