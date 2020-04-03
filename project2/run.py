"""
Project 2

- Fractional Knapsack
- Whole Knapsack
"""

from fractional_knapsack import fractional_knapsack, KnapsackItem


class Run(object):
    """
    Run project 2's methods
    """

    def fract_knapsack(self):
        """Run sorting algorithm for Merge sort and Quick sort
        """
        knapsack = [
            KnapsackItem(0, 18, 25),
            KnapsackItem(1, 15, 24),
            KnapsackItem(2, 10, 15)
        ]
        capacity = 20

        print("Knapsack:", knapsack)
        result = fractional_knapsack(knapsack, capacity)
        print("optiomal set:", result['set'])
        print("cost:", result['cost'])


if __name__ == "__main__":
    Run().fract_knapsack()
