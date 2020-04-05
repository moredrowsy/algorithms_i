"""
Unit tests
"""
import unittest

from floyd import floyd


class TestFloyd(unittest.TestCase):
    """
    Tests Binomial Coefficient's Algorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        inf = float('inf')

        weights = [
            [0, 1, inf, 1, 5],
            [9, 0, 3, 2, inf],
            [inf, inf, 0, 4, inf],
            [inf, inf, 2, 0, 3],
            [3, inf, inf, inf, 0]
        ]
        distances = [
            [0, 1, 3, 1, 4],
            [8, 0, 3, 2, 5],
            [10, 11, 0, 4, 7],
            [6, 7, 2, 0, 3],
            [3, 4, 6, 4, 0]
        ]
        paths = [
            [inf, inf, 3, inf, 3],
            [4, inf, inf, inf, 3],
            [4, 4, inf, inf, 3],
            [4, 4, inf, inf, inf],
            [inf, 0, 3, 0, inf]
        ]

        result = floyd(weights)

        self.assertEqual(result['distances'], distances)
        self.assertEqual(result['paths'], paths)

    def test_problem2(self):
        inf = float('inf')

        weights = [
            [0, 8, 2],
            [5, 0, inf],
            [inf, 3, 0]
        ]
        distances = [
            [0, 5, 2],
            [5, 0, 7],
            [8, 3, 0]
        ]
        paths = [
            [inf, 2, inf],
            [inf, inf, 0],
            [1, inf, inf]
        ]

        result = floyd(weights)

        self.assertEqual(result['distances'], distances)
        self.assertEqual(result['paths'], paths)

    def test_problem3(self):
        inf = float('inf')

        weights = [
            [0, 4, inf, inf, inf, 10, inf],
            [3, 0, inf, 18, inf, inf, inf],
            [inf, 6, 0, inf, inf, inf, inf],
            [inf, 5, 15, 0, 2, 19, 5],
            [inf, inf, 12, 1, 0, inf, inf],
            [inf, inf, inf, inf, inf, 0, 10],
            [inf, inf, inf, 8, inf, inf, 0]
        ]
        distances = [
            [0, 4, 36, 22, 24, 10, 20],
            [3, 0, 32, 18, 20, 13, 23],
            [9, 6, 0, 24, 26, 19, 29],
            [8, 5, 14, 0, 2, 18, 5],
            [9, 6, 12, 1, 0, 19, 6],
            [26, 23, 32, 18, 20, 0, 10],
            [16, 13, 22, 8, 10, 26, 0],
        ]
        paths = [
            [inf, inf, 4, 1, 3, inf, 5],
            [inf, inf, 4, inf, 3, 0, 3],
            [1, inf, inf, 1, 3, 1, 3],
            [1, inf, 4, inf, inf, 1, inf],
            [3, 3, inf, inf, inf, 3, 3],
            [6, 6, 6, 6, 6, inf, inf],
            [3, 3, 4, inf, 3, 3, inf],
        ]

        result = floyd(weights)

        self.assertEqual(result['distances'], distances)
        self.assertEqual(result['paths'], paths)


if __name__ == "__main__":
    unittest.main()
