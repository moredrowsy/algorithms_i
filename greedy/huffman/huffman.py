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
        return f"({self.sym if self.sym else 'None'}, {self.freq})"

    def __repr__(self):
        return f"({self.sym if self.sym else 'None'}, {self.freq})"

    def __lt__(self, o):
        if self.freq != o.freq:
            return self.freq < o.freq
        else:
            if self.sym is None:
                return True
            elif o.sym is None:
                return False
            else:
                return self.sym < o.sym

    def __eq__(self, o):
        return self.freq == o.freq

    def __ne__(self, o):
        return self.freq != o.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def huffman_tree(nodes):
    """
    Produces a Huffman coding tree

    Parameters
    ----------
    nodes (array): Array of HuffmanNodes

    Return
    ------
    root (HuffmanNode): The root node for the Huffman coding tree
    """
    n = len(nodes)
    heapq.heapify(nodes)

    for _ in range(n - 1):
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        root = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(nodes, root)

    return heapq.heappop(nodes)


def huffman_decode(root, string):
    """
    Decode an encoded Huffman string

    Parameters
    ----------
    root (HuffmanNode): Root node of a Huffman coding tree
    string (str): Encoded string of 0 and 1

    Return
    ------
    decoded_string (str): Decoded string
    """
    decoded_string = ''
    node = root

    for i in range(len(string)):
        if string[i] == '0':
            node = node.left
        else:
            node = node.right

        if node.is_leaf():
            decoded_string += node.sym
            node = root

    return decoded_string


def print_huffman_tree(root):
    """Wrapper for recursive print_tree"""
    print_tree(root, 0)


def print_tree(root, level):
    """Print entire tree via root node recursively"""
    if root.right:
        print_tree(root.right, level + 1)
    else:
        print(10 * level * ' ', 7 * ' ', '|||')

    print(10 * level * ' ', root)

    if root.left:
        print_tree(root.left, level + 1)
    else:
        print(10 * level * ' ', 7 * ' ', '|||')
