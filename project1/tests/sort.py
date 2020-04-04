"""
Unit tests
"""
import copy
import random
import unittest

from sort import mergesort, quicksort


class TestSort(unittest.TestCase):
    """
    Tests for sorting algorithms
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_list_empty(self):
        """
        Test empty list
        """
        list_empty = []

        mergesort(list_empty)
        self.assertEqual([], list_empty)

        quicksort(list_empty)
        self.assertEqual([], list_empty)

    def test_list_size_one(self):
        """
        Test list of size one
        """
        list_one = [1]

        mergesort(list_one)
        self.assertEqual(list_one, [1])

        quicksort(list_one)
        self.assertEqual(list_one, [1])

    def test_list_size_two(self):
        """
        Test list of size two
        """
        list_two = [2, 1]

        mergesort(list_two)
        self.assertEqual(list_two, [1, 2])

        quicksort(list_two)
        self.assertEqual(list_two, [1, 2])

    def test_list_size_three(self):
        """
        Test list of size three
        """
        list_three = [3, 2, 1]
        list_answer = copy.deepcopy(list_three)
        list_answer.sort()

        mergesort(list_three)
        self.assertEqual(list_three, list_answer)

        list_three = [3, 2, 1]

        quicksort(list_three)
        self.assertEqual(list_three, list_answer)

    def test_list_size_four(self):
        """
        Test list of size four
        """
        list_four = [4, 3, 2, 1]
        list_answer = copy.deepcopy(list_four)
        list_answer.sort()

        mergesort(list_four)
        self.assertEqual(list_four, list_answer)

        list_four = [4, 3, 2, 1]

        quicksort(list_four)
        self.assertEqual(list_four, list_answer)

    def test_list_equal_elements(self):
        """
        Test list of equal elements
        """
        list_answer = [1, 1, 1, 1, 1, ]
        list_equal_elements = [1, 1, 1, 1, 1, ]

        mergesort(list_equal_elements)
        self.assertEqual(list_equal_elements, list_answer)

        list_equal_elements = [1, 1, 1, 1, 1, ]

        quicksort(list_equal_elements)
        self.assertEqual(list_equal_elements, list_answer)

    def test_list_increasing(self):
        """
        Test list of increasing order
        """
        list_increasing = [i for i in range(10)]
        list_answer = copy.deepcopy(list_increasing)
        list_answer.sort()

        mergesort(list_increasing)
        self.assertEqual(list_increasing, list_answer)

        list_increasing = [i for i in range(10)]

        quicksort(list_increasing)
        self.assertEqual(list_increasing, list_answer)

    def test_list_decreasing(self):
        """
        Test list of decreasing order
        """
        list_decreasing = [i for i in range(9, -1, -1)]
        list_answer = copy.deepcopy(list_decreasing)
        list_answer.sort()

        mergesort(list_decreasing)
        self.assertEqual(list_decreasing, list_answer)

        list_decreasing = [i for i in range(9, -1, -1)]

        quicksort(list_decreasing)
        self.assertEqual(list_decreasing, list_answer)

    def test_list_random(self):
        """
        Test list of random elements at size 10 and 11
        """
        random.seed(0)
        list_randA = [random.randrange(1, 50, 1) for i in range(10)]
        list_randB = copy.deepcopy(list_randA)
        list_answer = copy.deepcopy(list_randA)
        list_answer.sort()

        mergesort(list_randA)
        self.assertEqual(list_randA, list_answer)

        quicksort(list_randB)
        self.assertEqual(list_randB, list_answer)

        list_randA = [random.randrange(1, 50, 1) for i in range(11)]
        list_randB = copy.deepcopy(list_randA)
        list_answer = copy.deepcopy(list_randA)
        list_answer.sort()

        mergesort(list_randA)
        self.assertEqual(list_randA, list_answer)

        quicksort(list_randB)
        self.assertEqual(list_randB, list_answer)


if __name__ == "__main__":
    unittest.main()
