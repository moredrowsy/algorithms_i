"""
Unit tests
"""
import unittest

from knapsack import KnapsackItem, knapsack, bruteforce_knapsack


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
        # profit = 12
        profit = bruteforce_knapsack(items, capacity)

        # test
        result = knapsack(items, capacity)
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
        # profit = 9
        profit = bruteforce_knapsack(items, capacity)

        # test
        result = knapsack(items, capacity)
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
        # profit = 8
        profit = bruteforce_knapsack(items, capacity)

        # test
        result = knapsack(items, capacity)
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
        # profit = 220
        profit = bruteforce_knapsack(items, capacity)

        # test
        result = knapsack(items, capacity)
        self.assertEqual(result['knapsack'], sack)
        self.assertEqual(result['profit'], profit)


if __name__ == "__main__":
    unittest.main()
