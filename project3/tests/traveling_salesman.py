"""
Unit tests
"""
import unittest

from traveling_salesman import traveling_salesman


class TestTravelingSalesman(unittest.TestCase):
    """
    Tests for Traveling Salesman
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        # problem
        adj = [
            [0, 14, 4, 10, 20],
            [14, 0, 7, 8, 7],
            [4, 5, 0, 7, 16],
            [11, 7, 9, 0, 2],
            [18, 7, 17, 4, 0]
        ]

        # solution
        length = 30
        path = [0, 3, 4, 1, 2, 0]

        # test
        result = traveling_salesman(adj)
        self.assertEqual(result['length'], length)
        self.assertEqual(result['path'], path)

    def test_problem2(self):
        # problem
        adj = [
            [0, 20, 30, 10, 1],
            [15, 0, 16, 4, 2],
            [3, 5, 0, 2, 4],
            [19, 6, 18, 0, 3],
            [16, 4, 7, 16, 0]
        ]

        # solution
        length = 28
        path = [0, 3, 1, 4, 2, 0]

        # test
        result = traveling_salesman(adj)
        self.assertEqual(result['length'], length)
        self.assertEqual(result['path'], path)

    def test_problem3(self):
        # problem
        adj = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]

        # solution
        length = 80
        path = [0, 1, 3, 2, 0]

        # test
        result = traveling_salesman(adj)
        self.assertEqual(result['length'], length)
        self.assertEqual(result['path'], path)


if __name__ == "__main__":
    unittest.main()
