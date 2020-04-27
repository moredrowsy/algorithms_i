import copy
import heapq


class KnapsackItem(object):
    """Represent a knapsack item with weight, profit, ratio"""

    def __init__(self, id, weight, profit):
        """
        Parameters
        ----------
        id (int): Knapsack item number
        weight (int): item's weight
        profit (float): item's profit
        """
        self.id = id
        self.weight = weight
        self.profit = profit

    def __repr__(self):
        return f"(ID {self.id} W {self.weight} P {self.profit})"

    def __eq__(self, o):
        return self.id == o.id\
            and self.weight == o.weight\
            and self.profit == o.profit


class KnapsackNode(object):
    """Knapsack node representation in Breath First Search traversal"""

    def __init__(self, level=0, weight=0, profit=0, bound=0, indices=None):
        """
        Parameters
        ----------
        level (int): kth item level
        weight (int): item's weight
        profit (float): item's profit
        bound (float): profit boundary for this node using greedy apporach
        indices (list): list of item indices
        """
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.indices = indices if indices else []

    def __repr__(self):
        return f"(L {self.level} W {self.weight} P {self.profit} B {self.bound})"

    def __lt__(self, o):
        return self.bound < o.bound


def knapsack(items, cap):
    """
    0-1 Knapsack using branch and bound algorithm using Best First Search,
    a modified version of Breath First Search using priority queue.

    Time complexity: W(b^m), b = branching factor, m = depth of tree if
        state space tree is not pruned.

    Parameters
    ----------
    items (array): List of KnapsackItem
    cap (int): Capacity of the knapsack

    Return
    ------
    {knapsack: array of KnapsackItem, profit: float}
    """
    maxprofit = 0

    # sort items by nonincreasing ratio
    items.sort(key=lambda i: i.profit/i.weight, reverse=True)

    # init priority queue
    # python heapq is ONLY minheap, so negate item in tuple for maxheap!
    pq = []
    heapq.heapify(pq)

    # init root node
    node = KnapsackNode(-1, 0, 0)
    node.bound = bound(items, cap, node)
    best_node = node

    # enqueue node
    heapq.heappush(pq, (-node.bound, node))  # negate bound for maxheap

    while pq:
        # dequeue node
        node = heapq.heappop(pq)[1]

        if node.bound > maxprofit:
            # left child
            left_child = KnapsackNode(node.level+1, node.weight, node.profit)
            left_child.weight += items[left_child.level].weight
            left_child.profit += items[left_child.level].profit
            left_child.indices = copy.copy(node.indices)
            left_child.indices.append(left_child.level)

            if left_child.weight <= cap and left_child.profit > maxprofit:
                maxprofit = left_child.profit
                best_node = left_child

            left_child.bound = bound(items, cap, left_child)
            if left_child.bound > maxprofit:
                heapq.heappush(pq, (-left_child.bound, left_child))

            # right child
            right_child = KnapsackNode(node.level+1, node.weight, node.profit)
            right_child.indices = copy.copy(node.indices)

            if right_child.weight <= cap and right_child.profit > maxprofit:
                maxprofit = right_child.profit
                best_node = right_child

            right_child.bound = bound(items, cap, right_child)
            if right_child.bound > maxprofit:
                heapq.heappush(pq, (-right_child.bound, right_child))

    # create a list of knapsack items
    knapsack = []
    for index in best_node.indices:
        knapsack.append(items[index])

    return {'knapsack': knapsack, 'profit': maxprofit}


def bound(items, cap, node):
    """
    Calculate max profit boundary using greedy approach for current node.

    Parameters
    ----------
    items (array): List of KnapsackItem
    cap (int): Capacity of the knapsack

    Return
    ------
    profit (float): maxprofit boundary
    """
    # invalidate bound if weight is at/over capacity
    if node.weight >= cap:
        return 0

    profit = node.profit
    cap -= node.weight

    for i in range(node.level + 1, len(items)):
        # add profit if future capacity is valid
        if cap - items[i].weight > 0:
            profit += items[i].profit
            cap -= items[i].weight
        # add fractional profit for the last item
        else:
            profit += cap/items[i].weight * items[i].profit
            break

    return profit


def knapsack_debug(items, cap):
    """0-1 Knapsack branch and bound with debug output at every step"""
    maxprofit = 0

    # sort items by nonincreasing ratio
    items.sort(key=lambda i: i.profit/i.weight, reverse=True)

    # init priority queue
    # python heapq is ONLY minheap, so negate item in tuple for maxheap!
    pq = []
    heapq.heapify(pq)

    # init root node
    node = KnapsackNode(-1, 0, 0)
    node.bound = bound(items, cap, node)
    best_node = node

    # enqueue node
    heapq.heappush(pq, (-node.bound, node))  # negate bound for maxheap

    # debug
    print("\nALL ITEMS\n")
    print_knapsack_items(items)
    step = 0
    print_debug(step, node, pq, maxprofit)

    while pq:
        # dequeue node
        node = heapq.heappop(pq)[1]

        if node.bound > maxprofit:
            # left child
            left_child = KnapsackNode(node.level+1, node.weight, node.profit)
            left_child.weight += items[left_child.level].weight
            left_child.profit += items[left_child.level].profit
            left_child.indices = copy.copy(node.indices)
            left_child.indices.append(left_child.level)

            if left_child.weight <= cap and left_child.profit > maxprofit:
                maxprofit = left_child.profit
                best_node = left_child

            left_child.bound = bound(items, cap, left_child)
            if left_child.bound > maxprofit:
                heapq.heappush(pq, (-left_child.bound, left_child))

            # right child
            right_child = KnapsackNode(node.level+1, node.weight, node.profit)
            right_child.indices = copy.copy(node.indices)

            if right_child.weight <= cap and right_child.profit > maxprofit:
                maxprofit = right_child.profit
                best_node = right_child

            right_child.bound = bound(items, cap, right_child)
            if right_child.bound > maxprofit:
                heapq.heappush(pq, (-right_child.bound, right_child))

        # debug
        step += 1
        print_debug(step, node, pq, maxprofit)

    # create a list of knapsack items
    knapsack = []
    for index in best_node.indices:
        knapsack.append(items[index])

    # debug
    print("\nKNAPSACK\n")
    print_knapsack_items(knapsack)
    print(f"\nPROFIT: {maxprofit}")

    return {'knapsack': knapsack, 'profit': maxprofit}


def print_debug(step, node, pq, maxprofit):
    """Print debug info for knapsack algorithm"""
    print(f"\n\nSTEP {step}")
    print(f"NODE: Level {node.level+1}  Profit {node.profit}  "
          f"Weight {node.weight}  Bound {node.bound}")
    print(f"MAXPROFIT: {maxprofit}")
    print("\nPRIORITY QUEUE\n")
    print_pq(pq)
    print("\n")


def print_pq(pq):
    """Print priority queue in tabular format"""
    pqeueue = copy.deepcopy(pq)
    print_nodes([heapq.heappop(pqeueue)[1] for _ in range(len(pq))])


def print_nodes(items):
    """Print noddes in tabular format"""
    labels = ["LEVEL", "PROFIT", "WEIGHT", "BOUND"]
    width = 10
    fmt_label = "{:<5} {:<{w}} {:<{w}} {:<{w}}"
    fmt_data = "{:<5} {:<{w}.2f} {:<{w}} {:<{w}.2f}"

    bar = [5*'-'] + [width*'-' for _ in range(1, len(labels))]
    print(fmt_label.format(*labels, w=width))
    print(fmt_label.format(*bar, w=width))

    if items:
        for item in items:
            print(fmt_data.format(item.level+1, item.profit, item.weight,
                                  item.bound, w=width))
    else:
        print("EMPTY")


def print_knapsack_items(items):
    """Print knapsack items in tabular format"""
    labels = ["ID", "PROFIT", "WEIGHT"]
    width = 10
    fmt_label = "{:<5} {:<{w}} {:<{w}}"
    fmt_data = "{:<5} {:<{w}.2f} {:<{w}}"

    bar = [5*'-'] + [width*'-' for _ in range(1, len(labels))]
    print(fmt_label.format(*labels, w=width))
    print(fmt_label.format(*bar, w=width))

    if items:
        for item in items:
            print(fmt_data.format(item.id, item.profit, item.weight, w=width))
    else:
        print("EMPTY")
