import sys


def prim(weights, start_vertex):
    """
    Find the minimal spanning tree (MST) using Prim's Algorithm

    Parameters
    ----------
    weights (array): 2D array of weights between edges
    start_vertex (int): Starting index

    Return
    ------
    array of edges (tuple)
    """
    INF = sys.maxsize
    n = len(weights)
    vnear = -1
    nearest = []
    distance = []
    final_edges = []

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

        # mark visited node
        distance[vnear] = -1

        # find shorter distances from weights[vnear] and update nearest/distance
        for i in range(n):
            if weights[vnear][i] < distance[i]:
                distance[i] = weights[vnear][i]
                nearest[i] = vnear

    return final_edges
