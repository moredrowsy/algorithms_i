"""
Prim's Algorithm: Find the minimal spanning tree to every node
"""


def prim(weights, start_vertex):
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
    weights (array): 2D array of weights between edges
    start_vertex (int): Starting index

    Return
    ------
    {edges: array of edges (tuple), cost: int}

    NOTES
    -----
    - vnear: Nearest vertex from the index at distance[i] to nearest[vnear].
             Tells us the previous vertex that has the smallest distance at
             distance[i].
    - nearest[]: Has the "nearest" vertices for the corresponding distances
                 in distance[i].
    - distance[]: Has the smallest distances at each iteration.
                  nearest[vnear] will tell us which previous vertex correspond
                  to distance[i].
    - final_edges[]: the resultant array of edges that produces the minimal
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
    INF = float('inf')
    n = len(weights)
    vnear, total_cost = -1, 0
    nearest, distance, final_edges = [], [], []

    # init nearest vertex as with start_vertex and
    # distance with weights[start_index]
    for i in range(n):
        if i == start_vertex:
            nearest.append(-1)
            distance.append(-1)
        else:
            nearest.append(start_vertex)
            distance.append(weights[start_vertex][i])

    # repeat for n-1 times
    for _ in range(n - 1):
        min = INF

        # find shorter distance
        for i in range(n):
            if distance[i] < min and distance[i] >= 0:
                min = distance[i]
                vnear = i

        # add to final set
        edge = (nearest[vnear], vnear)
        final_edges.append(edge)
        total_cost += weights[nearest[vnear]][vnear]

        # mark visited node
        distance[vnear] = -1

        # find shorter distances from weights[vnear] and update nearest/distance
        for i in range(n):
            if weights[vnear][i] < distance[i]:
                distance[i] = weights[vnear][i]
                nearest[i] = vnear

    return {'edges': final_edges, 'cost': total_cost}
