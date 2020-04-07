"""
Unit tests
"""
import unittest

from dijkstra import dijkstra, dijkstra_path


class TestDijkstra(unittest.TestCase):
    """
    Tests Dijsktra's Algorithm
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 7, 4, 6, 1],
            [inf, 0, inf, inf, inf],
            [inf, 2, 0, 5, inf],
            [inf, 3, inf, 0, inf],
            [inf, inf, inf, 1, 0]
        ]

        # solution
        edges = [
            (0, 4),
            (4, 3),
            (0, 2),
            (3, 1)
        ]
        predecessor = [0, 3, 0, 4, 0]
        path_answer = [0, 4, 3, 1]

        # test
        source, target = 0, 1
        result = dijkstra(weights, source)
        path = dijkstra_path(result['predecessor'], target)

        self.assertEqual(result['edges'], edges)
        self.assertEqual(result['predecessor'], predecessor)
        self.assertEqual(path, path_answer)

    def test_problem2(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 50, 10, inf, 45, inf],
            [inf, 0, 15, inf, 10, inf],
            [20, inf, 0, 15, inf, inf],
            [inf, 20, inf, 0, 35, inf],
            [inf, inf, inf, 30, 0, 20],
            [inf, inf, inf, 3, inf, 0]
        ]

        # solution
        edges = [
            (0, 2),
            (2, 3),
            (3, 1),
            (0, 4),
            (4, 5)
        ]
        predecessor = [0, 3, 0, 2, 0, 4]
        path_answer = [0, 4, 5]

        # test
        source, target = 0, 5
        result = dijkstra(weights, source)
        path = dijkstra_path(result['predecessor'], target)

        self.assertEqual(result['edges'], edges)
        self.assertEqual(result['predecessor'], predecessor)
        self.assertEqual(path, path_answer)

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
            (4, 3),
            (4, 1),
            (4, 2),
            (4, 5),
            (4, 0)
        ]
        predecessor = [4, 4, 4, 4, 4, 4]
        path_answer = [4, 3]

        # test
        source, target = 4, 3
        result = dijkstra(weights, source)
        path = dijkstra_path(result['predecessor'], target)

        self.assertEqual(result['edges'], edges)
        self.assertEqual(result['predecessor'], predecessor)
        self.assertEqual(path, path_answer)


if __name__ == "__main__":
    unittest.main()
