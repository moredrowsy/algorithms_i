import heapq


class HuffmanNode(object):
    """A node object for Huffman's coding with sym and freq"""

    def __init__(self, sym, freq, left=None, right=None):
        """
        Parameters
        ----------
        sym (char): Character symbol
        freq (int): Frequency integer
        left (HuffmanNode): left child HuffmanNode
        right (HuffmanNode): right child HuffmanNode
        """
        self.sym = sym
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.sym}, {self.freq})" if self.sym\
            else f"(None, {self.freq})"

    def __repr__(self):
        return f"({self.sym}, {self.freq})" if self.sym\
            else f"(None, {self.freq})"

    def __lt__(self, o):
        return self.freq < o.freq

    def __le__(self, o):
        return self.freq <= o.freq

    def __eq__(self, o):
        return self.freq == o.freq

    def __ne__(self, o):
        return self.freq != o.freq

    def __gt__(self, o):
        return self.freq > o.freq

    def __ge__(self, o):
        return self.freq >= o.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def huffman_tree(codes):
    """
    Produces a Huffman coding tree

    Parameters
    ----------
    code (array): Array of HuffmanNodes

    Return
    ------
    root (HuffmanNode): The root node for the Huffman coding tree
    """
    n = len(codes)
    for _ in range(n - 1):
        left = heapq.heappop(codes)
        right = heapq.heappop(codes)
        root = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(codes, root)

    return heapq.heappop(codes)
