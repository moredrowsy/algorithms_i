"""
Dijkstra's Algorithm: Find shortest path tree from single source
"""


def dijkstra(weights, source):
    """
    Dijkstra's Algorithm: Find the shortest path from one source node to
    every other nodes. Produces the shortest path spanning tree.

    Time complexity: O(n^2)
    Complexity breakdown:
        fro loop outer 1: n
        for loop outer 2: n - 1
        for loop inner 1: n
        for loop inner 2: n
        total: n + (n-1)*2n = O(n^2)

    Parameters
    ----------
    weights (2D array): Adjacency matrix. Connected, weighted, and directed
        graph of n >= 2.
    source (int): Starting index

    Return
    ------
    {edges: array of tuple, predecessor: array of parent nodes}

    NOTES
    -----
    - vnear: Node with min distance at each iteration.
    - length[]: List of min total length at each node.
        When updating length[i] with new min total length with vnear,
        touch[i] stores vnear.
    - touch[]: List of previous touched (visited) node to vnear.
        touch[vnear] to get previous node touched by vnear.
    - final_edges[]: Resultant array of edges that produces the shortest
        path tree.

    Algorithm finishes when length[] is populated with all -1

    DIFFERENCE FROM PRIM
    --------------------
    Consider 3 nodes: X, Y, Z.
    Total cost is 4 to connect all nodes together. Cost 2 from X -> Z.
        2
    X ----- Y
    |
    | 2
    Z
    """
    n = len(weights)
    vnear = -1
    length, touch, final_edges = [], [], []

    # init nearest with source and distance from weights[source]
    for i in range(n):
        if i == source:
            length.append(-1)
            touch.append(source)
        else:
            length.append(weights[source][i])
            touch.append(source)

    for _ in range(n - 1):
        min_dist = float('inf')

        # find node with min dist
        for i in range(n):
            if 0 <= length[i] < min_dist:
                min_dist = length[i]
                vnear = i

        # add to final set
        edge = (touch[vnear], vnear)
        final_edges.append(edge)

        # update arrays with vnear to find new min total length
        for i in range(n):
            if length[vnear] + weights[vnear][i] < length[i]:
                length[i] = length[vnear] + weights[vnear][i]
                touch[i] = vnear

        # mark visited node
        length[vnear] = -1

    return {'edges': final_edges, 'predecessor': touch}


def dijkstra_path(predecessor, target):
    """
    Return a list of nodes in a path to target

    Parameters
    ----------
    predecessor (array): List of parent nodes
    target (int): Destination node

    Return
    ------
    list of nodes in a path
    """
    path = []
    path_from_predecessor(predecessor, target, path)
    return path


def path_from_predecessor(predecessor, target, path):
    """
    Add nodes to path list from predecessor array

    Parameters
    ----------
    predecessor (array): List of parent nodes
    target (int): Destination node
    path (array): List of nodes added by reference
    """
    if predecessor[target] != target:
        path_from_predecessor(predecessor, predecessor[target], path)

    path.append(target)


def print_dijkstra_path(predecessor, target):
    """
    Wrapper for print_predecessor

    Parameters
    ----------
    predecessor (array): List of parent nodes
    target (int): Destination node

    NOTES
    -----
    source node is assumed from dijkstra's algorithm
    """
    print_predecessor(predecessor, target)
    print()


def print_predecessor(predecessor, target):
    """
    Prints dijkstra's shortest path by recursively following parent nodes.

    Parameters
    ----------
    predecessor (array): List of parent nodes
    target (int): Destination node
    """
    if predecessor[target] != target:
        print_predecessor(predecessor, predecessor[target])
        print(" -> ", end="")

    print(target, end="")
