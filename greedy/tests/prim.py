"""
Unit tests for sort module
"""
import sys
import unittest

from prim import prim


class TestPrim(unittest.TestCase):
    """
    Tests Prim's ALgorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        INF = sys.maxsize
        weights = [
            [0, 1, 3, INF, INF],
            [1, 0, 3, 6, INF],
            [3, 3, 0, 4, 2],
            [INF, 6, 4, 0, 5],
            [INF, INF, 2, 5, 0],
        ]
        solution_set = [
            (0, 1),
            (0, 2),
            (2, 4),
            (2, 3)
        ]
        total_cost = 10

        start_vertex = 0
        result = prim(weights, start_vertex)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['total_cost'], total_cost)

    def test_problem2(self):
        INF = sys.maxsize
        weights = [
            [0, 13, 3, 22, 8, INF, INF, INF],
            [13, 0, INF, 9, INF, INF, INF, INF],
            [3, INF, 0, INF, 9, INF, INF, INF],
            [22, 9, INF, 0, INF, 10, INF, INF],
            [8, INF, 9, INF, 0, 15, 10, INF],
            [INF, INF, INF, 10, 15, 0, INF, 12],
            [INF, INF, INF, INF, 10, INF, 0, INF],
            [INF, INF, INF, INF, 12, INF, INF, 0]
        ]
        solution_set = [
            (0, 2),
            (0, 4),
            (4, 6),
            (0, 1),
            (1, 3),
            (3, 5),
            (5, 7)
        ]
        total_cost = 65

        start_vertex = 0
        result = prim(weights, start_vertex)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['total_cost'], total_cost)

    def test_problem2(self):
        INF = sys.maxsize
        weights = [
            [0, INF, 72, 50, 90, 35],
            [INF, 0, 71, 70, 73, 75],
            [72, 71, 0, INF, 77, 90],
            [50, 70, INF, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]
        solution_set = [
            (3, 5),
            (5, 0),
            (3, 4),
            (3, 1),
            (1, 2)
        ]
        total_cost = 276

        start_vertex = 3
        result = prim(weights, start_vertex)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['total_cost'], total_cost)


if __name__ == "__main__":
    unittest.main()
