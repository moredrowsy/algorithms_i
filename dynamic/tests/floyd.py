"""
Unit tests
"""
import unittest

from floyd import floyd, floyd_path


class TestFloyd(unittest.TestCase):
    """
    Tests Floyd's Algorithm
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 1, inf, 1, 5],
            [9, 0, 3, 2, inf],
            [inf, inf, 0, 4, inf],
            [inf, inf, 2, 0, 3],
            [3, inf, inf, inf, 0]
        ]

        # solution
        distances = [
            [0, 1, 3, 1, 4],
            [8, 0, 3, 2, 5],
            [10, 11, 0, 4, 7],
            [6, 7, 2, 0, 3],
            [3, 4, 6, 4, 0]
        ]
        intermediate = [
            [inf, inf, 3, inf, 3],
            [4, inf, inf, inf, 3],
            [4, 4, inf, inf, 3],
            [4, 4, inf, inf, inf],
            [inf, 0, 3, 0, inf]
        ]
        path_answer = [1, 3, 4]

        # test
        result = floyd(weights)
        self.assertEqual(result['distances'], distances)
        self.assertEqual(result['intermediate'], intermediate)

        source, target = 1, 4
        path = floyd_path(result['intermediate'], source, target)
        self.assertEqual(path, path_answer)

    def test_problem2(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 8, 2],
            [5, 0, inf],
            [inf, 3, 0]
        ]

        # solution
        distances = [
            [0, 5, 2],
            [5, 0, 7],
            [8, 3, 0]
        ]
        intermediate = [
            [inf, 2, inf],
            [inf, inf, 0],
            [1, inf, inf]
        ]
        path_answer = [1, 0, 2]

        # test
        result = floyd(weights)
        self.assertEqual(result['distances'], distances)
        self.assertEqual(result['intermediate'], intermediate)

        source, target = 1, 2
        path = floyd_path(result['intermediate'], source, target)
        self.assertEqual(path, path_answer)

    def test_problem3(self):
        inf = float('inf')

        # problem
        weights = [
            [0, 4, inf, inf, inf, 10, inf],
            [3, 0, inf, 18, inf, inf, inf],
            [inf, 6, 0, inf, inf, inf, inf],
            [inf, 5, 15, 0, 2, 19, 5],
            [inf, inf, 12, 1, 0, inf, inf],
            [inf, inf, inf, inf, inf, 0, 10],
            [inf, inf, inf, 8, inf, inf, 0]
        ]

        # solution
        distances = [
            [0, 4, 36, 22, 24, 10, 20],
            [3, 0, 32, 18, 20, 13, 23],
            [9, 6, 0, 24, 26, 19, 29],
            [8, 5, 14, 0, 2, 18, 5],
            [9, 6, 12, 1, 0, 19, 6],
            [26, 23, 32, 18, 20, 0, 10],
            [16, 13, 22, 8, 10, 26, 0],
        ]
        intermediate = [
            [inf, inf, 4, 1, 3, inf, 5],
            [inf, inf, 4, inf, 3, 0, 3],
            [1, inf, inf, 1, 3, 1, 3],
            [1, inf, 4, inf, inf, 1, inf],
            [3, 3, inf, inf, inf, 3, 3],
            [6, 6, 6, 6, 6, inf, inf],
            [3, 3, 4, inf, 3, 3, inf],
        ]
        path_answer = [1, 3, 4, 2]

        # test
        result = floyd(weights)
        self.assertEqual(result['distances'], distances)
        self.assertEqual(result['intermediate'], intermediate)

        source, target = 1, 2
        path = floyd_path(result['intermediate'], source, target)
        self.assertEqual(path, path_answer)


if __name__ == "__main__":
    unittest.main()
