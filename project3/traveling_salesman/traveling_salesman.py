import copy
import heapq


class TravelNode(object):
    """Representation for the Traveling Salesman node"""

    def __init__(self, level=0, bound=0, path=None):
        """
        Parameters
        ----------
        level (int): kth node level
        bound (float): total boundary length for this node
        path (list): list of path indices
        """
        self.level = level
        self.bound = bound
        self.path = path if path else []

    def __repr__(self):
        return f"(L {self.level} B {self.bound})"

    def __lt__(self, o):
        return self.bound < o.bound


def traveling_salesman(adj):
    """
    Find the shortest path through every node once using track and bound
    algorithm with best first search.

    Time complexity: W(b^m), b = branching factor, m = depth of tree if
        state space tree is not pruned.

    Parameters
    ----------
    adj (array): 2D array adjacency matrix

    Return
    ------
    {length: float, path: list of node indices}
    """
    n = len(adj)
    minlength = float('inf')

    # init priority queue
    pq = []
    heapq.heapify(pq)

    # init root node
    node = TravelNode(0, 0, [0])
    node.bound = bound(adj, node)
    best_node = node

    # enqueue node
    heapq.heappush(pq, node)

    while pq:
        # dequeue node
        node = heapq.heappop(pq)

        if node.bound < minlength:
            for i in range(1, n):
                if i not in node.path:
                    # init child node
                    child = TravelNode(node.level + 1)
                    child.path = copy.copy(node.path)
                    child.path.append(i)

                    # when the child node is near the end
                    if child.level == n - 2:
                        add_remaining_nodes(child, n)

                        total_length = length(adj, child)
                        if total_length < minlength:
                            minlength = total_length
                            best_node = child
                    else:
                        child.bound = bound(adj, child)

                        if child.bound < minlength:
                            heapq.heappush(pq, child)

    return {'length': minlength, 'path': best_node.path}


def bound(adj, node):
    """Find the lenght boundary for the current node"""
    n = len(adj)
    minlength = 0
    path = node.path

    # get all edges in path
    if len(path) > 1:
        for i in range(len(path) - 1):
            minlength += adj[path[i]][path[i+1]]
    else:
        minlength += min(i for i in adj[0] if i > 0)

    # find minimun edges not in path except for last index
    for i in range(1, n):
        # when last path index is same as ith row
        if i == path[-1]:
            # exlucde columns that are in path
            row = (adj[i][j] for j in range(n) if j not in path and i != j)
            minlength += min(row)
        # exclude ith row in path
        elif i not in path:
            # exclude columns that are in path except the first node
            row = (adj[i][j] for j in range(n) if j not in path[1:] and i != j)
            minlength += min(row)

    return minlength


def length(adj, node):
    """Find total length of node's path"""
    total_length = 0
    path = node.path

    for i in range(len(path) - 1):
        total_length += adj[path[i]][path[i+1]]

    return total_length


def add_remaining_nodes(node, n):
    """Add the remaining indices to node, including the start index @ end"""
    for i in range(1, n):
        if i not in node.path:
            node.path.append(i)
    node.path.append(0)
