"""
Unit tests for sort module
"""
import sys
import unittest

from fractional_knapsack import fractional_knapsack, KnapsackItem


class TestFractionalKnapsack(unittest.TestCase):
    """
    Tests Dijsktra's ALgorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        knapsack = [
            KnapsackItem(0, 18, 25),
            KnapsackItem(1, 15, 24),
            KnapsackItem(2, 10, 15)
        ]
        capacity = 20
        solution_set = [
            (1, KnapsackItem(1, 15, 24)),
            (0.5, KnapsackItem(2, 10, 15)),
            (0, KnapsackItem(0, 18, 25))
        ]
        cost_answer = 31.5

        result = fractional_knapsack(knapsack, capacity)

        self.assertEqual(result['set'], solution_set)
        self.assertEqual(result['cost'], cost_answer)


if __name__ == "__main__":
    unittest.main()
