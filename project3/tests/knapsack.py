"""
Unit tests
"""
import unittest

from knapsack import KnapsackItem, knapsack


class TestKnapsack(unittest.TestCase):
    """
    Tests for 0-1 Knapsack
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        # problem
        items = [
            KnapsackItem(0, 2, 3),
            KnapsackItem(1, 1, 4),
            KnapsackItem(2, 4, 8),
            KnapsackItem(3, 3, 5)
        ]
        capacity = 6

        # solution
        sack = [
            KnapsackItem(2, 4, 8),
            KnapsackItem(1, 1, 4)
        ]
        sack.sort(key=lambda i: i.id)
        profit = 12

        # test
        result = knapsack(items, capacity)
        result['knapsack'].sort(key=lambda i: i.id)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)

    def test_problem2(self):
        # problem
        items = [
            KnapsackItem(0, 1, 1),
            KnapsackItem(1, 3, 4),
            KnapsackItem(2, 4, 5),
            KnapsackItem(3, 5, 7)
        ]
        capacity = 7

        # solution
        sack = [
            KnapsackItem(2, 4, 5),
            KnapsackItem(1, 3, 4)
        ]
        sack.sort(key=lambda i: i.id)
        profit = 9

        # test
        result = knapsack(items, capacity)
        result['knapsack'].sort(key=lambda i: i.id)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)

    def test_problem3(self):
        # problem
        items = [
            KnapsackItem(0, 2, 1),
            KnapsackItem(1, 3, 2),
            KnapsackItem(2, 4, 5),
            KnapsackItem(3, 5, 6)
        ]
        capacity = 8

        # solution
        sack = [
            KnapsackItem(3, 5, 6),
            KnapsackItem(1, 3, 2)
        ]
        sack.sort(key=lambda i: i.id)
        profit = 8

        # test
        result = knapsack(items, capacity)
        result['knapsack'].sort(key=lambda i: i.id)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)

    def test_problem4(self):
        # problem
        items = [
            KnapsackItem(0, 10, 60),
            KnapsackItem(1, 20, 100),
            KnapsackItem(2, 30, 120)
        ]
        capacity = 50

        # solution
        sack = [
            KnapsackItem(2, 30, 120),
            KnapsackItem(1, 20, 100)
        ]
        sack.sort(key=lambda i: i.id)
        profit = 220

        # test
        result = knapsack(items, capacity)
        result['knapsack'].sort(key=lambda i: i.id)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)

    def test_problem5(self):
        # problem
        items = [
            KnapsackItem(1, 2, 40),
            KnapsackItem(2, 5, 30),
            KnapsackItem(3, 10, 50),
            KnapsackItem(4, 5, 10)
        ]
        capacity = 16

        # solution
        sack = [
            KnapsackItem(1, 2, 40),
            KnapsackItem(3, 10, 50)
        ]
        sack.sort(key=lambda i: i.id)
        profit = 90

        # test
        result = knapsack(items, capacity)
        result['knapsack'].sort(key=lambda i: i.id)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)

    def test_problem6(self):
        # problem
        items = [
            KnapsackItem(1, 5, 35),
            KnapsackItem(2, 4, 16),
            KnapsackItem(3, 7, 42),
            KnapsackItem(4, 3, 9)
        ]
        capacity = 14

        # solution
        sack = [
            KnapsackItem(1, 5, 35),
            KnapsackItem(3, 7, 42)
        ]
        sack.sort(key=lambda i: i.id)
        profit = 77

        # test
        result = knapsack(items, capacity)
        result['knapsack'].sort(key=lambda i: i.id)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)


if __name__ == "__main__":
    unittest.main()
