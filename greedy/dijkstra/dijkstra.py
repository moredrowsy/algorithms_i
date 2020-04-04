"""
Dijkstra's Algorithm: Find shortest path tree from single source
"""


def dijkstra(weights, start_vertex):
    """
    Dijkstra's Algorithm: Find the shortest path from one starting vertex to
    every other vertices. Produces the shortest path spanning tree.

    Parameters
    ----------
    weights (array): 2D array of weights between edges
    start_vertex (int): Starting index

    Return
    ------
    {edges: array of tuple, touch: array of tuple}

    NOTES
    -----
    - vnear: the nearest vertex from index at length[i] to touch[vnear].
           Tells us which previous vertex has the smallest length at length[i].
    - length[]: Has the total legnth of the current iteration
    - touch[]: Has the previous node at corresponding to the total length in
             length[i]. Use touch[vnear] to get previous node.
    - final_edges[]: the resultant array of edges that produces the shortest
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
    length = []
    touch = []
    final_edges = []

    # init nearest vertex as with start_vertex and
    # distance with weights[start_index]
    for i in range(n):
        if i == start_vertex:
            length.append(-1)
            touch.append(start_vertex)
        else:
            length.append(weights[start_vertex][i])
            touch.append(start_vertex)

    for _ in range(n - 1):
        min = INF

        # find shorter path
        for i in range(n):
            if length[i] < min and length[i] >= 0:
                min = length[i]
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
    """Wrapper for print_dijkstra"""
    print_dijkstra(paths, destination)
    print()


def print_dijkstra(paths, destination):
    """
    """
    if paths[destination] != destination:
        print_dijkstra(paths, paths[destination])
        print("->", end=" ")

    print(destination, end=" ")
