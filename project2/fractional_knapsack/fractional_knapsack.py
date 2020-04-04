import copy


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


def fractional_knapsack(items, capacity):
    """
    Calculate the optimal set of items' profit in Knapsack

    Parameters
    ----------
    items (array): List of KnapsackItems
    capacity (float): Capacity of the knapsack

    Return
    ------
    {set: array of (fraction, KnapsackItem), cost: int}

    NOTES
    -----
    Sort the list of knapsack items by their profit/weight ratio
    Pick each the first item at every iteration
    If there's capacity:
        If capacity - item's weight >= 0, then add entire item to final set
        Else add item at fraction of capacity/item's weight
    Else: Add the rest of the items at 0 fraction.
    """
    cost = 0
    final_set = []

    # sort knapsack by ratio
    knapsack = sorted(items, key=lambda item: item.ratio, reverse=True)

    for item in knapsack:
        if capacity > 0:
            if capacity - item.weight >= 0:
                fractional = 1
                final_set.append((fractional, item))
            else:
                fractional = capacity / item.weight
                final_set.append((fractional, item))

            cost += final_set[-1][1].profit * final_set[-1][0]
            capacity -= item.weight
        else:
            final_set.append((0, item))

    return {'set': final_set, 'cost': cost}
