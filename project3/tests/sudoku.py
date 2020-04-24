"""
Unit tests
"""
import unittest

from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    """
    Tests for Sudoku
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        _ = Sudoku.empty

        # problem
        board = [
            [3, _, 4, _],
            [_, 2, _, 3],
            [_, _, _, _],
            [_, 4, _, 1],
        ]

        # solution
        solution = [
            [3, 1, 4, 2],
            [4, 2, 1, 3],
            [1, 3, 2, 4],
            [2, 4, 3, 1],
        ]

        # test
        sudoku = Sudoku()
        sudoku.setboard(board)
        is_solved = sudoku.solve()
        self.assertEqual(is_solved, True)
        self.assertEqual(board, solution)

    def test_problem2(self):
        _ = Sudoku.empty

        # problem
        board = [
            [3, _, 6, 5, _, 8, 4, _, _],
            [5, 2, _, _, _, _, _, _, _],
            [_, 8, 7, _, _, _, _, 3, 1],
            [_, _, 3, _, 1, _, _, 8, _],
            [9, _, _, 8, 6, 3, _, _, 5],
            [_, 5, _, _, 9, _, 6, _, _],
            [1, 3, _, _, _, _, 2, 5, _],
            [_, _, _, _, _, _, _, 7, 4],
            [_, _, 5, 2, _, 6, 3, _, _]
        ]

        # solution
        solution = [
            [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9]
        ]

        # test
        sudoku = Sudoku()
        sudoku.setboard(board)
        is_solved = sudoku.solve()
        self.assertEqual(is_solved, True)
        self.assertEqual(board, solution)

    def test_problem3(self):
        _ = Sudoku.empty

        # problem
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

        # solution
        solution = [
            [9, 5, 7, 6, 1, 3, 2, 8, 4],
            [4, 8, 3, 2, 5, 7, 1, 9, 6],
            [6, 1, 2, 8, 4, 9, 5, 3, 7],
            [1, 7, 8, 3, 6, 4, 9, 5, 2],
            [5, 2, 4, 9, 7, 1, 3, 6, 8],
            [3, 6, 9, 5, 2, 8, 7, 4, 1],
            [8, 4, 5, 7, 9, 2, 6, 1, 3],
            [2, 9, 1, 4, 3, 6, 8, 7, 5],
            [7, 3, 6, 1, 8, 5, 4, 2, 9]
        ]

        # test
        sudoku = Sudoku()
        sudoku.setboard(board)
        is_solved = sudoku.solve()
        self.assertEqual(is_solved, True)
        self.assertEqual(board, solution)


if __name__ == "__main__":
    unittest.main()
