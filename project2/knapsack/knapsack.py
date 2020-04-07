"""
Knapsack Problem: Find the optimal collection of items within capacity for
maximum profit
- 0-1 Knapsack: Dynamic approach
- Fractional Knapsack: Greedy approach
"""


class KnapsackItem(object):
    """Represent a knapsack item with weight, profit, ratio"""

    def __init__(self, index, weight, profit):
        """
        Parameters
        ----------
        index (int): Knapsack item number
        weight (float): the weight of this item
        profit (float): the profit for this item
        ratio (float): the profit per weight ratio
        """
        self.index = index
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

    def __str__(self):
        return f"(id:{self.index} weight:{self.weight} profit:{self.profit})"

    def __repr__(self):
        return f"(id:{self.index} w:{self.weight} p:{self.profit} r:{self.ratio})"

    def __eq__(self, o):
        return self.index == o.index\
            and self.weight == o.weight\
            and self.profit == o.profit


def knapsack(items, cap):
    """
    Find optimum set of items with maximum profit within knapsack's capacity.
    Items must be whole (can not be fractional).

    Time Complexity: O(min(2^n, n*c)), c = capacity

    Parameters
    ----------
    items (array): List of KnapsackItems
    cap (int): Capacity of the knapsack

    Return
    ------
    {profit: maximum profit}
    """
    n = len(items)
    profits = [[0 for j in range(cap + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if items[i-1].weight > j:
                profits[i][j] = profits[i-1][j]
            else:
                profits[i][j] = max(profits[i-1][j],
                                    profits[i-1][j-int(items[i-1].weight)] +
                                    items[i-1].profit)

    return {'profit': profits[n][cap]}


def fractional_knapsack(items, cap):
    """
    Find optimum set of items with maximum profit within knapsack's capacity.
    Items can be fractional.

    Time complexity: O(nlogn)
    Complexity breakdown:
        sort: nlogn
        for loop: n
        total: nlogn + n = O(nlogn)

    Parameters
    ----------
    items (array): List of KnapsackItems
    cap (float): Capacity of the knapsack

    Return
    ------
    {knapsack: array of (fraction, KnapsackItem), profit: float}
    """
    profit = 0
    knapsack = []

    # sort items by nonincreasing ratio
    sorted_items = sorted(items, key=lambda item: item.ratio, reverse=True)

    for item in sorted_items:
        if cap > 0:
            # if future capacity is negative, set to capacity/weight; else 1
            fraction = cap / item.weight if cap - item.weight < 0 else 1

            knapsack.append((fraction, item))
            profit += fraction * item.profit
            cap -= item.weight
        else:
            break

    return {'knapsack': knapsack, 'profit': profit}
