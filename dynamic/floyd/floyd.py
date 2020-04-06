"""
Floyd's Algorithm: Find shortest paths from every node to every other nodes
"""
import copy


def floyd(weights):
    """
    Floyd's Algorithm: Find the shortest paths from every node to every other
    nodes. Produces intermediate nodes array from path source to target.

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
    {distances: array, intermediate: array}
    """
    n = len(weights)
    dist = copy.deepcopy(weights)
    intermediate = [[float('inf') for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    intermediate[i][j] = k

    return {'distances': dist, 'intermediate': intermediate}


def print_floyd_path(intermediate, source, target):
    """
    Prints Floyd's path from source to target.

    Parameters
    ----------
    intermediate (2D array): Array of intermediate nodes in paths
    source (int): Origin node
    target (int): Destination node
    """
    print(f"{source} -> ", end="")
    print_intermediate(intermediate, source, target)
    print(f"{target}")


def print_intermediate(intermediate, source, target):
    """
    Prints intermediate nodes from Floyd's intermediate array.

    Parameters
    ----------
    intermediate (2D array): Array of intermediate nodes in paths
    source (int): Origin node
    target (int): Destination node
    """
    if intermediate[source][target] != float('inf'):
        print_intermediate(intermediate, source, intermediate[source][target])
        print(f"{intermediate[source][target]} -> ", end="")
        print_intermediate(intermediate, intermediate[source][target], target)
