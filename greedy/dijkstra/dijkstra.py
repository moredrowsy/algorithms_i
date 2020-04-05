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
    {edges: array of tuple, touch: array of tuple}

    NOTES
    -----
    - vnear: the nearest node from index at length[i] to touch[vnear].
           Tells us which previous node has the smallest length at length[i].
    - length[]: Has the total legnth of the current iteration
    - touch[]: Has the previous node at corresponding to the total length in
             length[i]. Use touch[vnear] to get previous node.
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
    INF = float('inf')
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
        min_dist = INF

        # find shorter path
        for i in range(n):
            if length[i] < min_dist and length[i] >= 0:
                min_dist = length[i]
                vnear = i

        # add to final set
        edge = (touch[vnear], vnear)
        final_edges.append(edge)

        # find shorter total length from length[vnear] with weights[vnear]
        for i in range(n):
            if length[vnear] + weights[vnear][i] < length[i]:
                length[i] = length[vnear] + weights[vnear][i]
                touch[i] = vnear

        # mark visited node
        length[vnear] = -1

    return {'edges': final_edges, 'touch': touch}


def print_dijkstra_path(paths, destination):
    """
    Wrapper for print_dijkstra

    Parameters
    ----------
    paths (array): Array from Dijkstra's last visited nodes
    destination (int): Destination node

    NOTES
    -----
    source node is assumed from dijkstra's algorithm
    """
    print_dijkstra(paths, destination)
    print()


def print_dijkstra(paths, destination):
    """
    Recursively follow the paths array to produce the dijkstra path

    Parameters
    ----------
    paths (array): Array from Dijkstra's last visited nodes
    destination (int): Destination node
    """
    if paths[destination] != destination:
        print_dijkstra(paths, paths[destination])
        print(" -> ", end="")

    print(destination, end="")
