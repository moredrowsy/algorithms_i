"""
Knapsack Problem: Find the optimal collection of items within capacity for
maximum profit
- 0-1 Knapsack: Dynamic approach
- Fractional Knapsack: Greedy approach
"""


class KnapsackItem(object):
    """Represent a knapsack item with weight, profit, ratio"""

    def __init__(self, id, weight, profit):
        """
        Parameters
        ----------
        id (int): Knapsack item number
        weight (int): the weight of this item
        profit (float): the profit for this item
        """
        self.id = id
        self.weight = weight
        self.profit = profit

    def __str__(self):
        return f"(id:{self.id} weight:{self.weight} profit:{self.profit})"

    def __repr__(self):
        return f"(id:{self.id} weight:{self.weight} profit:{self.profit})"

    def __eq__(self, o):
        return self.id == o.id\
            and self.weight == o.weight\
            and self.profit == o.profit


def knapsack(items, cap):
    """
    Find optimum set of items with maximum profit within knapsack's capacity.
    Items must be whole (can not be fractional).

    Time Complexity: O(min(2^n, n*c)), c = capacity

    Parameters
    ----------
    items (array): List of KnapsackItem
    cap (int): Capacity of the knapsack

    Return
    ------
    {knapsack: array of KnapsackItem, profit: float}

    NOTES
    -----
    i: Index i represent item number.
        i starts at 0 for items[i]
        i starts at 1 for profits[i][j]
    j: Index j represent weight, up to capacity
    items[]: List of items start at index 0, not 1!
    profits[][]: List of total profits for each item.
        Start at index 1. Index 0 is placeholder for no profit or weight
        Hence, profits[i][j] for item i -> items[i-1]
        Ex: profits[1][j] for item 1 refers to first item at item[0]
    """
    n = len(items)
    profits = [[0 for j in range(cap + 1)] for i in range(n + 1)]

    # i = item index, j = weight index
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            # if current item weight is over capacity, use previous item profit
            if items[i-1].weight > j:
                profits[i][j] = profits[i-1][j]
            # get max of prev item profit vs current item profit
            # plus total profits from items within capacity limit
            else:
                profits[i][j] = max(profits[i-1][j],
                                    profits[i-1][j-items[i-1].weight] +
                                    items[i-1].profit)

    # get list of knapack items from profits array
    knapsack = knapsack_items(items, profits)

    return {'knapsack': knapsack, 'profit': profits[n][cap]}


def knapsack_items(items, profits):
    """Get a list of items in knapsack from profits array"""
    knapsack = []
    cap = len(profits[0]) - 1

    # loop item index backwards
    for item in range(len(profits) - 1, -1, -1):
        if cap <= 0 or profits[item][cap] == 0:
            break
        elif profits[item][cap] == profits[item-1][cap]:
            continue
        else:
            knapsack.append(items[item-1])

        cap -= items[item-1].weight

    return knapsack


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
    items (array): List of KnapsackItem
    cap (int): Capacity of the knapsack

    Return
    ------
    {knapsack: array of (fraction, KnapsackItem), profit: float}
    """
    profit = 0
    knapsack = []

    # sort items by nonincreasing ratio
    sorted_items = sorted(items, key=lambda i: i.profit/i.weight, reverse=True)

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


def bruteforce_knapsack(items, cap):
    """Bruteforce knapsack for testing purposes"""
    return bf_knapsack(items, cap, len(items))


def bf_knapsack(items, cap, n):
    """Recursively permutate all items within capacity for maximum profit"""
    if cap == 0 or n == 0:
        return 0
    elif items[n-1].weight > cap:
        return bf_knapsack(items, cap, n - 1)
    else:
        return max(
            items[n-1].profit +
            bf_knapsack(items, cap - items[n-1].weight, n - 1),
            bf_knapsack(items, cap, n - 1)
        )
