"""
Unit tests for sort module
"""
import sys
import unittest

from huffman import HuffmanNode, huffman_tree, huffman_decode,\
    print_huffman_tree


class TestHuffman(unittest.TestCase):
    """
    Tests Huffman's ALgorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        nodes = [
            HuffmanNode('b', 5),
            HuffmanNode('e', 10),
            HuffmanNode('c', 12),
            HuffmanNode('a', 16),
            HuffmanNode('d', 17),
            HuffmanNode('f', 25)
        ]
        root_answer = HuffmanNode(None, 85)

        root = huffman_tree(nodes)
        self.assertEqual(root, root_answer)

        coded_str1 = '001110111000'
        coded_str2 = '0100101111'
        decoded_answer1 = 'abba'
        decoded_answer2 = 'dafe'

        decoded1 = huffman_decode(root, coded_str1)
        decoded2 = huffman_decode(root, coded_str2)

        self.assertEqual(decoded1, decoded_answer1)
        self.assertEqual(decoded2, decoded_answer2)

    def test_problem2(self):
        nodes = [
            HuffmanNode('A', 12),
            HuffmanNode('B', 7),
            HuffmanNode('I', 18),
            HuffmanNode('M', 10),
            HuffmanNode('S', 9),
            HuffmanNode('X', 5),
            HuffmanNode('Z', 2)
        ]
        root_answer = HuffmanNode(None, 63)

        root = huffman_tree(nodes)
        self.assertEqual(root, root_answer)

        coded_str1 = '1100000011'
        coded_str2 = '0100100101'
        decoded_answer1 = 'SAAB'
        decoded_answer2 = 'ZIX'

        decoded1 = huffman_decode(root, coded_str1)
        decoded2 = huffman_decode(root, coded_str2)

        self.assertEqual(decoded1, decoded_answer1)
        self.assertEqual(decoded2, decoded_answer2)

    def test_problem3(self):
        nodes = [
            HuffmanNode('Z', 2),
            HuffmanNode('K', 7),
            HuffmanNode('M', 24),
            HuffmanNode('C', 32),
            HuffmanNode('U', 37),
            HuffmanNode('D', 42),
            HuffmanNode('L', 42),
            HuffmanNode('E', 120)
        ]
        root_answer = HuffmanNode(None, 306)

        root = huffman_tree(nodes)
        self.assertEqual(root, root_answer)

        coded_str1 = '10100101'
        coded_str2 = '111111001110111101'
        decoded_answer1 = 'DEED'
        decoded_answer2 = 'MUCK'

        decoded1 = huffman_decode(root, coded_str1)
        decoded2 = huffman_decode(root, coded_str2)

        self.assertEqual(decoded1, decoded_answer1)
        self.assertEqual(decoded2, decoded_answer2)


if __name__ == "__main__":
    unittest.main()
