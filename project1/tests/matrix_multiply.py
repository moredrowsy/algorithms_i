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
    # class attributes

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
        C = matrix_add(self.A11, self.A22)
        D = matrix_add(self.B11, self.B22)
        C_answer = [[6, 8], [8, 6]]
        D_answer = [[22, 24], [24, 22]]

        self.assertEqual(C, C_answer)
        self.assertEqual(D, D_answer)

        P = matrix_multiply_2x2(C, D)
        P_answer = [[324, 320], [320, 324]]
        self.assertEqual(P, P_answer)

    def test_matrix_Q(self):
        C = matrix_add(self.A21, self.A22)
        C_answer = [[10, 12], [12, 10]]

        Q = matrix_multiply_2x2(C, self.B11)
        Q_answer = [[212, 210], [206, 208]]

        self.assertEqual(Q, Q_answer)

    def test_matrix_R(self):
        C = matrix_sub(self.B12, self.B22)
        C_answer = [[-4, -4], [-4, -4]]

        self.assertEqual(C, C_answer)

        R = matrix_multiply_2x2(self.A11, C)
        R_answer = [[-4, -4], [-20, -20]]

        self.assertEqual(R, R_answer)

    def test_matrix_S(self):
        C = matrix_sub(self.B21, self.B11)
        C_answer = [[4, 4], [4, 4]]

        self.assertEqual(C, C_answer)

        S = matrix_multiply_2x2(self.A22, C)
        S_answer = [[52, 52], [36, 36]]

        self.assertEqual(S, S_answer)

    def test_matrix_T(self):
        C = matrix_add(self.A11, self.A12)
        C_answer = [[2, 4], [4, 2]]

        self.assertEqual(C, C_answer)

        T = matrix_multiply_2x2(C, self.B22)
        T_answer = [[80, 78], [82, 84]]

        self.assertEqual(T, T_answer)

    def test_matrix_U(self):
        C = matrix_sub(self.A21, self.A11)
        D = matrix_add(self.B11, self.B12)
        C_answer = [[4, 4], [4, 4]]
        D_answer = [[18, 20], [20, 18]]

        self.assertEqual(C, C_answer)
        self.assertEqual(D, D_answer)

        U = matrix_multiply_2x2(C, D)
        U_answer = [[152, 152], [152, 152]]

        self.assertEqual(U, U_answer)

    def test_matrix_V(self):
        C = matrix_sub(self.A12, self.A22)
        D = matrix_add(self.B21, self.B22)
        C_answer = [[-4, -4], [-4, -4]]
        D_answer = [[26, 28], [28, 26]]

        self.assertEqual(C, C_answer)
        self.assertEqual(D, D_answer)

        V = matrix_multiply_2x2(C, D)
        V_answer = [[-216, -216], [-216, -216]]

        self.assertEqual(V, V_answer)

    def test_classic_2x2(self):
        """
        Test classic matrix at 2x2
        """
        A = [[0, 1], [1, 0]]
        B = [[2, 3], [3, 2]]
        answer = [[3, 2], [2, 3]]

        C = matrix_multiply(A, B)
        self.assertEqual(C, answer)

    def test_classic_4x4(self):
        """
        Test classic matrix at 4x4
        """
        A = [[0, 1, 2, 3], [3, 2, 1, 0], [4, 5, 6, 7], [7, 6, 5, 4]]
        B = [[8, 9, 10, 11], [11, 10, 9, 8],
             [12, 13, 14, 15], [15, 14, 13, 12]]
        answer = [[80, 78, 76, 74], [58, 60, 62, 64], [
            264, 262, 260, 258], [242, 244, 246, 248]]

        C = matrix_multiply(A, B)
        self.assertEqual(C, answer)

    def test_strassen_2x2(self):
        """
        Test classic matrix at 2x2
        """
        A = [[0, 1], [1, 0]]
        B = [[2, 3], [3, 2]]
        answer = [[3, 2], [2, 3]]

        C = strassen_multiply(A, B)
        self.assertEqual(C, answer)

    def test_strassen_4x4(self):
        """
        Test classic matrix at 4x4
        """
        A = [[0, 1, 2, 3], [3, 2, 1, 0], [4, 5, 6, 7], [7, 6, 5, 4]]
        B = [[8, 9, 10, 11], [11, 10, 9, 8],
             [12, 13, 14, 15], [15, 14, 13, 12]]
        answer = [[80, 78, 76, 74], [58, 60, 62, 64], [
            264, 262, 260, 258], [242, 244, 246, 248]]

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
        answer = [[274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818],
                  [274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818]]

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
        answer = [[274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818],
                  [274, 274, 274, 274, 274, 274, 274, 274],
                  [338, 338, 338, 338, 338, 338, 338, 338],
                  [882, 882, 882, 882, 882, 882, 882, 882],
                  [818, 818, 818, 818, 818, 818, 818, 818]]

        C = strassen_multiply(A, B)
        self.assertEqual(C, answer)


if __name__ == "__main__":
    unittest.main()
