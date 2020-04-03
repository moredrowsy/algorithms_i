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
        return f"(#{self.index}], {self.weight}, {self.profit})"

    def __repr__(self):
        return f"(#{self.index}, {self.weight}, {self.profit}, {self.ratio})"

    def __eq__(self, o):
        return self.index == o.index\
            and self.weight == o.weight\
            and self.profit == o.profit


def fractional_knapsack(knapsack, capacity):
    """
    Calculate the optimal set of items' profit in Knapsack

    Parameters
    ----------
    knapsack (array): List of KnapsackItems
    capacity (float): Capacity of the knapsack

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
    knapsack.sort(key=lambda i: i.ratio, reverse=True)

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
