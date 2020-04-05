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
    Prints Floyd's path from source to destination.

    Parameters
    ----------
    paths (2D array): Array from Floyd's last visited nodes
    source (int): Starting node
    destination (int): Ending node
    """
    print(f"{source} -> ", end="")
    print_floyd_int_path(paths, source, destination)
    print(f"{destination}")


def print_floyd_int_path(paths, source, destination):
    """
    Prints intermediate nodes from Floyd's paths array.

    Parameters
    ----------
    paths (2D array): Array from Floyd's last visited nodes
    source (int): Starting node
    destination (int): Ending node
    """
    if paths[source][destination] != float('inf'):
        print_floyd_int_path(paths, source, paths[source][destination])
        print(f"{paths[source][destination]} -> ", end="")
        print_floyd_int_path(paths, paths[source][destination], destination)
