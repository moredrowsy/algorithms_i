"""
Unit tests
"""
import unittest

from dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    """
    Tests Dijsktra's Algorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        inf = float('inf')
        weights = [
            [0, 7, 4, 6, 1],
            [inf, 0, inf, inf, inf],
            [inf, 2, 0, 5, inf],
            [inf, 3, inf, 0, inf],
            [inf, inf, inf, 1, 0]
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

        source_node = 0
        result = dijkstra(weights, source_node)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['touch'], touch)

    def test_problem2(self):
        inf = float('inf')
        weights = [
            [0, 50, 10, inf, 45, inf],
            [inf, 0, 15, inf, 10, inf],
            [20, inf, 0, 15, inf, inf],
            [inf, 20, inf, 0, 35, inf],
            [inf, inf, inf, 30, 0, 20],
            [inf, inf, inf, 3, inf, 0]
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

        source_node = 0
        result = dijkstra(weights, source_node)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['touch'], touch)

    def test_problem3(self):
        inf = float('inf')
        weights = [
            [0, inf, 72, 50, 90, 35],
            [inf, 0, 71, 70, 73, 75],
            [72, 71, 0, inf, 77, 90],
            [50, 70, inf, 0, 60, 40],
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

        source_node = 4
        result = dijkstra(weights, source_node)

        self.assertEqual(result['edges'], solution_set)
        self.assertEqual(result['touch'], touch)


if __name__ == "__main__":
    unittest.main()
