"""
Unit tests
"""
import unittest

from prim import prim


class TestPrim(unittest.TestCase):
    """
    Tests Prim's Algorithm
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 1, 3, inf, inf],
            [1, 0, 3, 6, inf],
            [3, 3, 0, 4, 2],
            [inf, 6, 4, 0, 5],
            [inf, inf, 2, 5, 0],
        ]

        # solution
        edges = [
            (0, 1),
            (0, 2),
            (2, 4),
            (2, 3)
        ]
        cost = 10

        # test
        source = 0
        result = prim(weights, source)
        self.assertEqual(result['edges'], edges)
        self.assertEqual(result['cost'], cost)

    def test_problem2(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 13, 3, 22, 8, inf, inf, inf],
            [13, 0, inf, 9, inf, inf, inf, inf],
            [3, inf, 0, inf, 9, inf, inf, inf],
            [22, 9, inf, 0, inf, 10, inf, inf],
            [8, inf, 9, inf, 0, 15, 10, inf],
            [inf, inf, inf, 10, 15, 0, inf, 12],
            [inf, inf, inf, inf, 10, inf, 0, inf],
            [inf, inf, inf, inf, 12, inf, inf, 0]
        ]

        # solution
        edges = [
            (0, 2),
            (0, 4),
            (4, 6),
            (0, 1),
            (1, 3),
            (3, 5),
            (5, 7)
        ]
        cost = 65

        # test
        source = 0
        result = prim(weights, source)
        self.assertEqual(result['edges'], edges)
        self.assertEqual(result['cost'], cost)

    def test_problem3(self):
        inf = float('inf')

        # problem
        weights = [
            [0, inf, 72, 50, 90, 35],
            [inf, 0, 71, 70, 73, 75],
            [72, 71, 0, inf, 77, 90],
            [50, 70, inf, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        # solution
        edges = [
            (3, 5),
            (5, 0),
            (3, 4),
            (3, 1),
            (1, 2)
        ]
        cost = 276

        # test
        source = 3
        result = prim(weights, source)
        self.assertEqual(result['edges'], edges)
        self.assertEqual(result['cost'], cost)


if __name__ == "__main__":
    unittest.main()
