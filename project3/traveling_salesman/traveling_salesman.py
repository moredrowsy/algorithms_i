import copy
import heapq


class TravelNode(object):
    def __init__(self, level=0, bound=0, path=[]):
        self.level = level
        self.bound = bound
        self.path = path

    def __lt__(self, o):
        return self.bound < o.bound


def traveling_salesman(adj):
    n = len(adj)
    minlength = float('inf')

    # init priority queue
    pq = []
    heapq.heapify(pq)

    # init root node
    node = TravelNode(0)
    node.path.append(0)
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

                    # update length if reach near the end
                    if child.level == n - 2:
                        add_leftover_nodes(child, n)

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
    n = len(adj)
    length = 0
    level = node.level
    path = node.path

    # get all edges in path
    if len(path) > 1:
        for i in range(len(path) - 1):
            length += adj[path[i]][path[i+1]]
    else:
        length += min(i for i in adj[0] if i > 0)

    for i in range(1, n):
        # row for last index in path
        if i == path[-1]:
            row = [adj[path[-1]][i] for i in range(n) if i not in path]
            length += min(row)
        elif i not in path:
            row = [adj[i][j] for j in range(n) if j not in path[1:] and i != j]
            length += min(row)

    return length


def length(adj, node):
    total_length = 0
    path = node.path

    for i in range(len(path) - 1):
        total_length += adj[path[i]][path[i+1]]

    return total_length


def add_leftover_nodes(node, n):
    for i in range(1, n):
        if i not in node.path:
            node.path.append(i)
    node.path.append(0)
