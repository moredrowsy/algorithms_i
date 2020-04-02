import sys


def dijkstra(weights, start_vertex):
    """
    Find the shortest path using Dijkstra's Algorithm

    Parameters
    ----------
    weights (array): 2D array of weights between edges
    start_vertex (int): Starting index

    Return
    ------
    {final: array of tuple, touch: array of tuple}
    """
    INF = sys.maxsize
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
            touch.append(0)
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

        edge = (touch[vnear], vnear)
        final_edges.append(edge)

        for i in range(n):
            if length[vnear] + weights[vnear][i] < length[i]:
                length[i] = length[vnear] + weights[vnear][i]
                touch[i] = vnear

        length[vnear] = -1

    return {'final': final_edges, 'touch': touch}
