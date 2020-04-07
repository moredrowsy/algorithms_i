"""
Unit tests
"""
import unittest

from matrix_multiply import matrix_multiply, strassen_multiply
from matrix_multiply.matrix_multiply import *


class TestMatrixMultiply(unittest.TestCase):
    """
    Tests for Matrix Multiplication
    """

    def setUp(self):
        """
        Test setup
        """
        self.A = [[0, 1, 2, 3], [3, 2, 1, 0], [4, 5, 6, 7], [7, 6, 5, 4]]
        self.B = [[8, 9, 10, 11], [11, 10, 9, 8],
                  [12, 13, 14, 15], [15, 14, 13, 12]]
        self.A11 = [[0, 1], [3, 2]]
        self.A12 = [[2, 3], [1, 0]]
        self.A21 = [[4, 5], [7, 6]]
        self.A22 = [[6, 7], [5, 4]]
        self.B11 = [[8, 9], [11, 10]]
        self.B12 = [[10, 11], [9, 8]]
        self.B21 = [[12, 13], [15, 14]]
        self.B22 = [[14, 15], [13, 12]]

    def test_matrix_P(self):
        C_answer = [[6, 8], [8, 6]]
        D_answer = [[22, 24], [24, 22]]
        P_answer = [[324, 320], [320, 324]]

        C = matrix_add(self.A11, self.A22)
        D = matrix_add(self.B11, self.B22)
        self.assertEqual(C, C_answer)
        self.assertEqual(D, D_answer)

        P = matrix_multiply_2x2(C, D)
        self.assertEqual(P, P_answer)

    def test_matrix_Q(self):
        C_answer = [[10, 12], [12, 10]]
        Q_answer = [[212, 210], [206, 208]]

        C = matrix_add(self.A21, self.A22)
        self.assertEqual(C, C_answer)

        Q = matrix_multiply_2x2(C, self.B11)
        self.assertEqual(Q, Q_answer)

    def test_matrix_R(self):
        C_answer = [[-4, -4], [-4, -4]]
        R_answer = [[-4, -4], [-20, -20]]

        C = matrix_sub(self.B12, self.B22)
        self.assertEqual(C, C_answer)

        R = matrix_multiply_2x2(self.A11, C)
        self.assertEqual(R, R_answer)

    def test_matrix_S(self):
        C_answer = [[4, 4], [4, 4]]
        S_answer = [[52, 52], [36, 36]]

        C = matrix_sub(self.B21, self.B11)
        self.assertEqual(C, C_answer)

        S = matrix_multiply_2x2(self.A22, C)
        self.assertEqual(S, S_answer)

    def test_matrix_T(self):
        C_answer = [[2, 4], [4, 2]]
        T_answer = [[80, 78], [82, 84]]

        C = matrix_add(self.A11, self.A12)
        self.assertEqual(C, C_answer)

        T = matrix_multiply_2x2(C, self.B22)
        self.assertEqual(T, T_answer)

    def test_matrix_U(self):
        C_answer = [[4, 4], [4, 4]]
        D_answer = [[18, 20], [20, 18]]
        U_answer = [[152, 152], [152, 152]]

        C = matrix_sub(self.A21, self.A11)
        D = matrix_add(self.B11, self.B12)
        self.assertEqual(C, C_answer)
        self.assertEqual(D, D_answer)

        U = matrix_multiply_2x2(C, D)
        self.assertEqual(U, U_answer)

    def test_matrix_V(self):
        C_answer = [[-4, -4], [-4, -4]]
        D_answer = [[26, 28], [28, 26]]
        V_answer = [[-216, -216], [-216, -216]]

        C = matrix_sub(self.A12, self.A22)
        D = matrix_add(self.B21, self.B22)
        self.assertEqual(C, C_answer)
        self.assertEqual(D, D_answer)

        V = matrix_multiply_2x2(C, D)
        self.assertEqual(V, V_answer)

    def test_classic_2x2(self):
        """
        Test classic matrix at 2x2
        """
        # problem
        A = [[0, 1], [1, 0]]
        B = [[2, 3], [3, 2]]

        # solution
        answer = [[3, 2], [2, 3]]

        # test
        C = matrix_multiply(A, B)
        self.assertEqual(C, answer)

    def test_classic_4x4(self):
        """
        Test classic matrix at 4x4
        """
        # problem
        A = [[0, 1, 2, 3], [3, 2, 1, 0], [4, 5, 6, 7], [7, 6, 5, 4]]
        B = [[8, 9, 10, 11], [11, 10, 9, 8],
             [12, 13, 14, 15], [15, 14, 13, 12]]

        # solution
        answer = [[80, 78, 76, 74], [58, 60, 62, 64], [
            264, 262, 260, 258], [242, 244, 246, 248]]

        # test
        C = matrix_multiply(A, B)
        self.assertEqual(C, answer)

    def test_strassen_2x2(self):
        """
        Test classic matrix at 2x2
        """
        # problem
        A = [[0, 1], [1, 0]]
        B = [[2, 3], [3, 2]]
        answer = [[3, 2], [2, 3]]

        C = strassen_multiply(A, B)
        self.assertEqual(C, answer)

    def test_strassen_4x4(self):
        """
        Test classic matrix at 4x4
        """
        # problem
        A = [[0, 1, 2, 3], [3, 2, 1, 0], [4, 5, 6, 7], [7, 6, 5, 4]]
        B = [[8, 9, 10, 11], [11, 10, 9, 8],
             [12, 13, 14, 15], [15, 14, 13, 12]]

        # solution
        answer = [[80, 78, 76, 74], [58, 60, 62, 64], [
            264, 262, 260, 258], [242, 244, 246, 248]]

        # test
        C = strassen_multiply(A, B)
        self.assertEqual(C, answer)

    def test_classic_8x8(self):
        A = [[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9],
             [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]
        B = [[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9],
             [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]

        # solution
        answer = [[274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818],
                  [274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818]]

        # test
        C = matrix_multiply(A, B)
        self.assertEqual(C, answer)

    def test_strassen_8x8(self):
        A = [[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9],
             [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]
        B = [[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9],
             [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]

        # solution
        answer = [[274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818],
                  [274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818]]

        # test
        C = strassen_multiply(A, B)
        self.assertEqual(C, answer)


if __name__ == "__main__":
    unittest.main()
