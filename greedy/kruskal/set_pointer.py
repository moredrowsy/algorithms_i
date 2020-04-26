class SetPointer(object):
    """
    Set Pointer datatype for representing disjoint sets of size n.
    Two nodes are in the same set if their root nodes are the same.
    """

    def __init__(self, size):
        """
        Initially, each node is in their own set.

        Parameters
        ----------
        size (int): Size of the set
        """
        self.pointers = [i for i in range(size)]

    def __repr__(self):
        return f"{self.pointers}"

    def find(self, node):
        """Find root node with given node"""
        while self.pointers[node] != node:
            node = self.pointers[node]
        return node

    def merge(self, node_a, node_b):
        """Merges two nodes together. Larger root node points to smaller node"""
        root_a, root_b = self.find(node_a), self.find(node_b)
        self.merge_root(root_a, root_b)

    def merge_root(self, root_a, root_b):
        """Merge two root nodes"""
        if root_a < root_b:
            self.pointers[root_b] = root_a
        else:
            self.pointers[root_a] = root_b

    def equal(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)
