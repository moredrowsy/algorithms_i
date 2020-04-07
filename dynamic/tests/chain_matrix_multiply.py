"""
Unit tests
"""
import io
import sys
import unittest

from chain_matrix_multiply import chain_matrix_multiply, print_optimal_order


class TestChainMatrixMultiply(unittest.TestCase):
    """
    Tests Chain Matrix Multiplication's Algorithm
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        inf = float('inf')

        # problem
        #  A0     A1     A2     A3     A4     A5
        # 5x2    2x3    3x4    4x6    6x7    7x8
        dimensions = [5, 2, 3, 4, 6, 7, 8]

        # solution
        seperations = [
            [inf, 0, 0, 0, 0, 0],
            [inf, inf, 1, 2, 3, 4],
            [inf, inf, inf, 2, 3, 4],
            [inf, inf, inf, inf, 3, 4],
            [inf, inf, inf, inf, inf, 4]
        ]
        cost = 348
        order = "(A0((((A1A2)A3)A4)A5))"

        # test
        result = chain_matrix_multiply(dimensions)
        self.assertEqual(result['seperations'], seperations)
        self.assertEqual(result['cost'], cost)

        # test print output
        output = io.StringIO()
        sys.stdout = output
        print_optimal_order(result['seperations'], 0, len(dimensions) - 2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), order)

    def test_problem2(self):
        inf = float('inf')

        # problem
        #  A0     A1     A2     A3
        # 20x2   2x30   30x12  12x8
        dimensions = [20, 2, 30, 12, 8]

        # solution
        seperations = [
            [inf, 0, 0, 0],
            [inf, inf, 1, 2],
            [inf, inf, inf, 2],
        ]
        order = "(A0((A1A2)A3))"
        cost = 1232

        # test
        result = chain_matrix_multiply(dimensions)
        self.assertEqual(result['seperations'], seperations)
        self.assertEqual(result['cost'], cost)

        # test print output
        output = io.StringIO()
        sys.stdout = output
        print_optimal_order(result['seperations'], 0, len(dimensions) - 2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), order)

    def test_problem3(self):
        inf = float('inf')

        # problem
        #  A0     A1     A2     A3     A4
        # 10x4   4x5    5x20   20x2   2x50
        dimensions = [10, 4, 5, 20, 2, 50]

        # solution
        seperations = [
            [inf, 0, 0, 0, 3],
            [inf, inf, 1, 1, 3],
            [inf, inf, inf, 2, 3],
            [inf, inf, inf, inf, 3]
        ]
        order = "((A0(A1(A2A3)))A4)"
        cost = 1320

        # test
        result = chain_matrix_multiply(dimensions)
        self.assertEqual(result['seperations'], seperations)
        self.assertEqual(result['cost'], cost)

        # test print output
        output = io.StringIO()
        sys.stdout = output
        print_optimal_order(result['seperations'], 0, len(dimensions) - 2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), order)


if __name__ == "__main__":
    unittest.main()
