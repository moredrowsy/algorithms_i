import sys


def prim(weights):
    INF = sys.maxsize
    n = len(weights)
    vnear = -1
    nearest = []
    distance = []
    final_edges = []

    # init first col
    nearest.append(-1)
    distance.append(-1)

    # init nearest vertex as index 0 and distance from weights[0]
    for i in range(1, n):
        nearest.append(0)
        distance.append(weights[0][i])

    # repeat for n-1 times
    for i in range(n - 1):
        min = INF

        # find small distance
        for j in range(1, n):
            if distance[j] < min and distance[j] >= 0:
                min = distance[j]
                vnear = j

        # add to final set
        edge = (nearest[vnear], vnear)
        final_edges.append(edge)

        # mark visited node
        distance[vnear] = -1

        # find smaller distances from weights[vnear] and update nearest/distance
        for j in range(1, n):
            if weights[vnear][j] < distance[j]:
                distance[j] = weights[vnear][j]
                nearest[j] = vnear

    return final_edges
