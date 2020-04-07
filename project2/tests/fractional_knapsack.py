"""
Unit tests
"""
import unittest

from knapsack import KnapsackItem, fractional_knapsack


class TestFractionalKnapsack(unittest.TestCase):
    """
    Tests for Fractional Knapsack
    """

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        items = [
            KnapsackItem(0, 18, 25),
            KnapsackItem(1, 15, 24),
            KnapsackItem(2, 10, 15)
        ]
        capacity = 20
        solution = [
            (1, KnapsackItem(1, 15, 24)),
            (0.5, KnapsackItem(2, 10, 15)),
        ]
        profit = 31.5

        result = fractional_knapsack(items, capacity)

        self.assertEqual(result['knapsack'], solution)
        self.assertEqual(result['profit'], profit)


if __name__ == "__main__":
    unittest.main()
