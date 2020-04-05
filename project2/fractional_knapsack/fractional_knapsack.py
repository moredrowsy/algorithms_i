"""
Fractional Knapsack: Find the optimal collection of items within knapsack
capacity with maximal profit
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


def fractional_knapsack(items, cap):
    """
    Calculate the optimal set of items' profit in Knapsack.

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
            # set to capacity/weight if future capacity is negative
            # otherwise 1
            fraction = cap / item.weight if cap - item.weight < 0 else 1

            knapsack.append((fraction, item))
            profit += fraction * item.profit
            cap -= item.weight
        else:
            break

    return {'knapsack': knapsack, 'profit': profit}
