"""
Unit tests
"""
import unittest

from dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    """
    Tests Dijsktra's ALgorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        INF = float('inf')
        weights = [
            [0, 7, 4, 6, 1],
            [INF, 0, INF, INF, INF],
            [INF, 2, 0, 5, INF],
            [INF, 3, INF, 0, INF],
            [INF, INF, INF, 1, 0]
        ]
        solution_set = [
            (0, 4),
            (4, 3),
            (0, 2),
            (3, 1)
        ]
        touch = [
            0, 3, 0, 4, 0
        ]

        start_vertex = 0
        result = dijkstra(weights, start_vertex)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['touch'], touch)

    def test_problem2(self):
        INF = float('inf')
        weights = [
            [0, 50, 10, INF, 45, INF],
            [INF, 0, 15, INF, 10, INF],
            [20, INF, 0, 15, INF, INF],
            [INF, 20, INF, 0, 35, INF],
            [INF, INF, INF, 30, 0, 20],
            [INF, INF, INF, 3, INF, 0]
        ]
        solution_set = [
            (0, 2),
            (2, 3),
            (3, 1),
            (0, 4),
            (4, 5)
        ]
        touch = [
            0, 3, 0, 2, 0, 4
        ]

        start_vertex = 0
        result = dijkstra(weights, start_vertex)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['touch'], touch)

    def test_problem3(self):
        INF = float('inf')
        weights = [
            [0, INF, 72, 50, 90, 35],
            [INF, 0, 71, 70, 73, 75],
            [72, 71, 0, INF, 77, 90],
            [50, 70, INF, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]
        solution_set = [
            (4, 3),
            (4, 1),
            (4, 2),
            (4, 5),
            (4, 0)
        ]
        touch = [
            4, 4, 4, 4, 4, 4
        ]

        start_vertex = 4
        result = dijkstra(weights, start_vertex)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['touch'], touch)


if __name__ == "__main__":
    unittest.main()
