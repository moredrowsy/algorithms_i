from .set_pointer import SetPointer


class Edge(object):
    """Represents an Edge of node a to node b with a cost of weight"""

    def __init__(self, a, b, weight):
        """
        Parameters
        ----------
        a (int): First node
        a (int): Second node
        weight (float): Weight of an edge
        """
        self.a = a
        self.b = b
        self.weight = weight

    def __str__(self):
        return f"({self.a}, {self.b}, {self.weight})"

    def __repr__(self):
        return f"({self.a}, {self.b}, {self.weight})"

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b and self.weight == o.weight

    def indices(self):
        return self.a, self.b


def kruskal(weights):
    """
    Kruskal's Algorithm: Find the minimal cost of every node connected node.
    Produces the minimal spanning tree.

    Time Complexity: O(eloge), W(n^2 * logn), e = edges
    Complexity breakdown:
        matrix to edges: e
        sort: eloge
        disjoint_sets init: eloge
        disjoint_sets ops: eloge
        edges: e >= n - 1
        total: e + 3*(eloge) = O(eloge)
        worst with dense graph: e = n(n-1)/2 = n^2
    Conclusion:
        if Graph is sparse: O(eloge)
        if Graph is dense: O(n^2 * logn)

    Parameters
    ----------
    weights (2D array): Adjacency matrix. Connected, weighted, and undirected
        graph of n >= 2.

    Return
    ------
    {edges: array of edges (tuple), cost: float}
    """
    n = len(weights)
    disjoint_sets = SetPointer(n)
    total_cost = 0
    edges, final_edges = [], []

    # create list of edges from undirected weights matrix
    for i in range(n):
        for j in range(i + 1, n):
            if weights[i][j] != float('inf'):
                edges.append(Edge(i, j, weights[i][j]))

    # sort edges by nondecreasing order
    edges.sort(key=lambda edge: edge.weight)

    for edge in edges:
        if len(final_edges) >= n - 1:
            break

        a, b = edge.indices()

        # if a and b are not in same disjoint set, merge a, b to same set
        root_a, root_b = disjoint_sets.find(a), disjoint_sets.find(b)
        if root_a != root_b:
            disjoint_sets.merge_root(root_a, root_b)
            final_edges.append(edge)
            total_cost += edge.weight

    return {'edges': final_edges, 'cost': total_cost}
