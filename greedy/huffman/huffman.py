"""
Huffman's Coding Algorithm: Encoding/decoding strings with prefix codes
"""
import heapq


class HuffmanNode(object):
    """A node object for Huffman's coding with symbol and frequency"""

    def __init__(self, sym, freq, left=None, right=None):
        """
        Parameters
        ----------
        sym (char): Character symbol. Use None if no symbol.
        freq (int): Frequency integer
        left (HuffmanNode): left child HuffmanNode
        right (HuffmanNode): right child HuffmanNode
        """
        self.sym = sym
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.sym if self.sym else 'None'}, {self.freq})"

    def __lt__(self, o):
        if self.freq != o.freq:
            return self.freq < o.freq
        else:
            if self.sym and o.sym:
                return self.sym < o.sym
            elif self.sym is None and o.sym is None:
                return False
            elif self.sym:
                return False
            else:
                return True

    def __eq__(self, o):
        return self.freq == o.freq

    def __ne__(self, o):
        return self.freq != o.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def huffman_nodes(string):
    """
    Calculate the frequency of characters in string.

    Parameters
    ----------
    string (str): Input string for parsing

    Return
    ------
    list: A list of HuffmanNodes
    """
    map_nodes = {}

    for s in string:
        if s in map_nodes:
            map_nodes[s].freq += 1
        else:
            map_nodes[s] = HuffmanNode(s, 1)

    return list(map_nodes.values())


def huffman_tree(nodes):
    """
    Produces a Huffman coding tree.

    Time complexity: O(nlogn)
    Complexity breakdown:
        heapq.heapify: logn
        heapq.heappop: logn
        for loop: n - 1
        total: (n-1)*logn = O(nlogn)

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
    str: Decoded string
    """
    decoded_string = ''
    node = root

    for s in string:
        node = node.left if s == '0' else node.right

        if node.is_leaf():
            decoded_string += node.sym
            node = root

    return decoded_string


def huffman_encode(root, string):
    """
    Encode a string to binary coded string

    Parameters
    ----------
    root (HuffmanNode): Root node of Huffman coding tree
    string (str): String to encode

    Return
    ------
    str: Encoded binary string
    """
    encoded_string = ''
    huffmap = huffman_map(root)

    for s in string:
        encoded_string += huffmap[s]

    return encoded_string


def huffman_map(root):
    """
    Wrapper for huffman_mapping()

    Return
    ------
    {char: encoded string}: A dictionary of letters to encoded strings
    """
    huffmap = {}
    string = ''
    huffman_mapping(root, huffmap, string)
    return huffmap


def huffman_mapping(root, huffmap, string):
    """
    Produces a Huffman dictionary of letters as keys mapping to encoded strings
    via adding to huffmap by reference.

    Parameters
    ----------
    root (HuffmanNode): Root node of Huffman coding tree
    huffmap (dict): Dictionary object
    string (str): Encoded binary string
    """
    if root:
        huffman_mapping(root.right, huffmap, string + str(1))
        huffman_mapping(root.left, huffmap, string + str(0))

        if root.sym:
            huffmap[root.sym] = string


def print_huffman_tree(root):
    """Wrapper for recursive print_tree()"""
    print_tree(root, 0)


def print_tree(root, level):
    """Print entire tree via root node recursively"""
    if root:
        print_tree(root.right, level + 1)
        print(10 * level * ' ', root)
        print_tree(root.left, level + 1)
    else:
        print(10 * level * ' ', '|||')
