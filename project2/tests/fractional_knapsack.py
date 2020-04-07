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

    def test_problem2(self):
        items = [
            KnapsackItem(0, 10, 60),
            KnapsackItem(1, 20, 100),
            KnapsackItem(2, 30, 120)
        ]
        capacity = 50
        solution = [
            (1,  KnapsackItem(0, 10, 60)),
            (1, KnapsackItem(1, 20, 100)),
            (2/3, KnapsackItem(2, 30, 120)),
        ]
        profit = 240

        result = fractional_knapsack(items, capacity)
        self.assertEqual(result['knapsack'], solution)
        self.assertEqual(result['profit'], profit)

    def test_problem3(self):
        items = [
            KnapsackItem(0, 2, 10),
            KnapsackItem(1, 3, 5),
            KnapsackItem(2, 5, 15),
            KnapsackItem(3, 7, 7),
            KnapsackItem(4, 1, 6),
            KnapsackItem(5, 4, 18),
            KnapsackItem(6, 1, 3),
        ]
        capacity = 15
        solution = [
            (1, KnapsackItem(4, 1, 6)),
            (1, KnapsackItem(0, 2, 10)),
            (1, KnapsackItem(5, 4, 18)),
            (1, KnapsackItem(2, 5, 15)),
            (1, KnapsackItem(6, 1, 3)),
            (2/3, KnapsackItem(1, 3, 5)),
        ]
        profit = 166/3

        result = fractional_knapsack(items, capacity)
        self.assertEqual(result['knapsack'], solution)
        self.assertEqual(result['profit'], profit)


if __name__ == "__main__":
    unittest.main()
