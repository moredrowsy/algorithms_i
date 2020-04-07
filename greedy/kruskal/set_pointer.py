class SetPointer(object):
    """Set Pointer datatype"""

    def __init__(self, size):
        """
        Parameters
        ----------
        size (int): Size of the set
        """
        self.pointers = [i for i in range(size)]

    def __str__(self):
        return f"{self.pointers}"

    def __repr__(self):
        return f"{self.pointers}"

    def find(self, node):
        """Find root node with given node"""
        while self.pointers[node] != node:
            node = self.pointers[node]
        return node

    def merge(self, node_a, node_b):
        """Merges two nodes together. Larger node points to smaller node"""
        if node_a < node_b:
            self.pointers[node_b] = node_a
        else:
            self.pointers[node_a] = node_b

    def equal(self, node_a, node_b):
        return node_a == node_b
