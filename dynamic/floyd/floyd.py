"""
Floyd's Algorithm: Find shortest paths from every node to every other nodes
"""
import copy


def floyd(weights):
    """
    Floyd's Algorithm: Find the shortest paths from every node to every other
    nodes. Produces the shortest paths 2D array.

    Time complexity: O(n^3)
    Complexity breakdown:
        for loop 1: n
        for loop 2: n
        for loop 3: n
        total: n*n*n = O(n^3)


    Parameters
    ----------
    weights (2D array): Adjacency matrix. Weighted and directed graph.

    Return
    ------
    {distances: array, paths: array}
    """
    n = len(weights)
    dist = copy.deepcopy(weights)
    paths = [[float('inf') for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    paths[i][j] = k

    return {"distances": dist, "paths": paths}


def print_floyd_path(paths, source, destination):
    """
    Wrapper for floyd_path

    Parameters
    ----------
    paths (2D array): Array from Floyd's last visited nodes
    source (int): Starting node
    destination (int): Ending node
    """
    edges = []
    floyd_path(paths, source, destination, edges)

    for edge in edges:
        print(f"{edge[0]} -> ", end="")
    print(edges[-1][1])


def floyd_path(paths, source, destination, edges):
    """
    Produces a list of edges for Floyd's paths recursively

    Parameters
    ----------
    paths (2D array): Array from Floyd's last visited nodes
    source (int): Starting node
    destination (int): Ending node
    edges (array): 1D array for adding edges by reference

    Return
    ------
    edges (array): A list of edges are returned by reference
    """
    if paths[source][destination] != float('inf'):
        edges.append((source, paths[source][destination]))
        floyd_path(paths, source, paths[source][destination], edges)
        floyd_path(paths, paths[source][destination], destination, edges)
        edges.append((paths[source][destination], destination))
