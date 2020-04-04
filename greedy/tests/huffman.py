"""
Unit tests
"""
import sys
import unittest

from huffman import HuffmanNode, huffman_encode, huffman_decode, huffman_tree


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

        str1 = "abba"
        str2 = "dafe"
        encoded_answer1 = "001110111000"
        encoded_answer2 = "0100101111"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        self.assertEqual(encoded_str1, encoded_answer1)
        self.assertEqual(encoded_str2, encoded_answer2)
        self.assertEqual(decoded_str1, str1)
        self.assertEqual(decoded_str2, str2)

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

        str1 = "SAAB"
        str2 = "ZIX"
        encoded_answer1 = "1100000011"
        encoded_answer2 = "0100100101"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        self.assertEqual(encoded_str1, encoded_answer1)
        self.assertEqual(encoded_str2, encoded_answer2)
        self.assertEqual(decoded_str1, str1)
        self.assertEqual(decoded_str2, str2)

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

        str1 = "DEED"
        str2 = "MUCK"
        encoded_answer1 = "10100101"
        encoded_answer2 = "111111001110111101"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        self.assertEqual(encoded_str1, encoded_answer1)
        self.assertEqual(encoded_str2, encoded_answer2)
        self.assertEqual(decoded_str1, str1)
        self.assertEqual(decoded_str2, str2)


if __name__ == "__main__":
    unittest.main()
