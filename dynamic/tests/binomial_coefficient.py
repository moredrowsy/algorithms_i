"""
Unit tests
"""
import unittest

from binomial_coefficient import binomial_coefficient


class TestBinomialCoefficient(unittest.TestCase):
    """
    Tests Binomial Coefficient's Algorithm
    """

    def setUp(self):
        """
        Test setup
        """

    def test_against_hardcoded_table(self):
        # solution
        table = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 4, 6, 4, 1, 0, 0, 0, 0, 0, 0],
            [1, 5, 10, 10, 5, 1, 0, 0, 0, 0, 0],
            [1, 6, 15, 20, 15, 6, 1, 0, 0, 0, 0],
            [1, 7, 21, 35, 35, 21, 7, 1, 0, 0, 0],
            [1, 8, 28, 56, 70, 56, 28, 8, 1, 0, 0],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1, 0],
            [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
        ]

        # test permutations of n and k
        n = k = len(table)
        for i in range(n):
            for j in range(k):
                coefficient = binomial_coefficient(i, j)
                self.assertEqual(coefficient, table[i][j])


if __name__ == "__main__":
    unittest.main()
