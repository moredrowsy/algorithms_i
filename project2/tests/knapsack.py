"""
Unit tests
"""
import unittest

from knapsack import KnapsackItem, knapsack


class TestKnapsack(unittest.TestCase):
    """
    Tests for Fractional Knapsack
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        items = [
            KnapsackItem(0, 2, 3),
            KnapsackItem(1, 1, 4),
            KnapsackItem(2, 4, 8),
            KnapsackItem(3, 3, 5)
        ]
        capacity = 6
        profit = 12

        result = knapsack(items, capacity)
        print(result['profit'], profit)


if __name__ == "__main__":
    unittest.main()
