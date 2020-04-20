"""
Prim's Algorithm: Find minimal spanning tree from each node to every other nodes
"""


def prim(weights, source=0):
    """
    Prim's Algorithm: Find the minimal cost of every node connected node.
    Produces the minimal spanning tree.

    Time complexity: O(n^2)
    Complexity breakdown:
        for loop outer 1: n
        for loop outer 2: n - 1
        for loop inner 1: n
        for loop inner 2: n
        total: n + (n-1)*2n = O(n^2)

    Parameters
    ----------
    weights (2D array): Adjacency matrix. Connected, weighted, and undirected
        graph of n >= 2.
    source (int): Starting index. No effect on MST total cost but the
        MST tree might be differennt for edges with same weight.

    Return
    ------
    {edges: array of edges (tuple), cost: float}

    NOTES
    -----
    - vnear: Node with min distance at each iteration.
    - distance[]: List of min distances at each node.
        When updating distance[i] for new min distance with vnear,
        nearest[i] stores vnear.
    - nearest[]: List of previous nearest (closest) node to vnear.
        nearest[vnear] to get previous node closest to vnear.
    - final_edges[]: Resultant array of edges that produces the minimal
                     spanning tree (MST).

    Algorithm finishes when distance[] is populated with all -1

    DIFFERENCE FROM DJIKSTRA
    ------------------------
    Consider 3 nodes: X, Y, Z.
    Total cost is 3 to connect all nodes together. Cost 3 from X -> Z.
        2
    X ----- Y
            |
            | 1
            Z
    """
    n = len(weights)
    vnear, total_cost = -1, 0
    nearest, distance, final_edges = [], [], []

    # init nearest with source and distance from weights[source]
    for i in range(n):
        if i == source:
            distance.append(-1)
            nearest.append(-1)
        else:
            distance.append(weights[source][i])
            nearest.append(source)

    # repeat for n-1 times
    for _ in range(n - 1):
        min_dist = float('inf')

        # find node with min dist
        for i in range(n):
            if 0 <= distance[i] < min_dist:
                min_dist = distance[i]
                vnear = i

        # add to final set
        edge = (nearest[vnear], vnear)
        final_edges.append(edge)
        total_cost += weights[nearest[vnear]][vnear]

        # mark visited node
        distance[vnear] = -1

        # update arrays with vnear to find new min distance
        for i in range(n):
            if weights[vnear][i] < distance[i]:
                distance[i] = weights[vnear][i]
                nearest[i] = vnear

    return {'edges': final_edges, 'cost': total_cost}
