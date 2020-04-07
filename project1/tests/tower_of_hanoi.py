"""
Unit tests
"""
import unittest

from tower_of_hanoi import TowerOfHanoi


class TestTowerOfHanoi(unittest.TestCase):
    """
    Tests for Tower of Hanoi
    """

    def setUp(self):
        """
        Test setup
        """

    def test_toh_empty(self):
        """
        Test Tower of Hanoi with no disks
        """
        # problem
        A = []
        B = []
        C = []

        # test
        toh = TowerOfHanoi(A, B, C, "A", "B", "C")
        toh.solve(display=False)

        self.assertEqual(A, [])
        self.assertEqual(B, [])
        self.assertEqual(C, [])

    def test_toh_n1(self):
        """
        Test Tower of Hanoi at n = 1
        """
        # problem
        n = 1
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []

        # test
        toh = TowerOfHanoi(A, B, C, "A", "B", "C")
        toh.solve(display=False)

        self.assertEqual(A, [])
        self.assertEqual(B, [])
        self.assertEqual(C, [i for i in range(n, 0, -1)])

    def test_toh_n2(self):
        """
        Test Tower of Hanoi at n = 2
        """
        # problem
        n = 2
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []

        # test
        toh = TowerOfHanoi(A, B, C, "A", "B", "C")
        toh.solve(display=False)

        self.assertEqual(A, [])
        self.assertEqual(B, [])
        self.assertEqual(C, [i for i in range(n, 0, -1)])

    def test_toh_n3(self):
        """
        Test Tower of Hanoi at n = 3
        """
        # problem
        n = 3
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []

        # test
        toh = TowerOfHanoi(A, B, C, "A", "B", "C")
        toh.solve(display=False)

        self.assertEqual(A, [])
        self.assertEqual(B, [])
        self.assertEqual(C, [i for i in range(n, 0, -1)])

    def test_toh_n4(self):
        """
        Test Tower of Hanoi at n = 4
        """
        # problem
        n = 4
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []

        # test
        toh = TowerOfHanoi(A, B, C, "A", "B", "C")
        toh.solve(display=False)

        self.assertEqual(A, [])
        self.assertEqual(B, [])
        self.assertEqual(C, [i for i in range(n, 0, -1)])


if __name__ == "__main__":
    unittest.main()
