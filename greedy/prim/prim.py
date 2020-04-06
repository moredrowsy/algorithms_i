"""
Prim's Algorithm: Find minimal spanning tree from each node to every other nodes
"""


def prim(weights, source=0):
    """
    Prim's Algorithm: Find the minimal cost of every node connected node.
    Produces the minimal spanning tree.

    Time complexity: O(n^2)
    Complexity breakdown:
        fro loop outer 1: n
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
    {edges: array of edges (tuple), cost: int}

    NOTES
    -----
    - vnear: Node with min distance at each iteration.
        Node is also index at distance[i] to nearest[vnear].
        Tells us the previous node with min distance at distance[i].
    - distance[]: List of min distances at each iteration.
    - nearest[]: List of vnear nodes for distance in distance[i]
        nearest[vnear] to get node corresponding to distance[i].
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
    inf = float('inf')
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
        min_dist = inf

        # find node with min dist
        for i in range(n):
            if distance[i] < min_dist and distance[i] >= 0:
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
