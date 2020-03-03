"""
Project 1
"""

from sort import mergesort, quicksort
from tower_of_hanoi import TowerOfHanoi
from matrix_multiply import matrix_multiply, strassen_multiply
from matrix_multiply.matrix_multiply import *


class Run(object):
    """
    Run Project 1
    """

    def sorting(self):
        """
        Run sorting algorithm for Merge sort and Quick sort
        """
        print("Running sorting func\n")

        list1 = [3, 5, 0, 4, 8, 2, 1]
        list2 = [3, 5, 0, 4, 8, 2]
        print("Unsorted list")
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        print("\nRunning merge sort")
        mergesort(list1)
        mergesort(list2)
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        list1 = [3, 5, 0, 4, 8, 2, 1]
        list2 = [3, 5, 0, 4, 8, 2]
        print("\nUnsorted list")
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        print("\nRunning quick sort")
        quicksort(list1)
        quicksort(list2)
        print(f"list1: {list1}")
        print(f"list2: {list2}")

    def tower_of_hanoi(self):
        A = [4, 3, 2, 1]
        B = []
        C = []

        toh = TowerOfHanoi(A, B, C, "A", "B", "C")

        print("\nTower of Hanoi Setup")
        toh.print()

        toh.solve(display=True)

        print("\nTower of Hanoi Solution")
        toh.print()

    def matrix_multiplication(self):
        print("\nInitial 8x8 matrices")
        A = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [
            1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
        B = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [
            1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
        print(A)
        print(B)

        print("\nClassical Matrix Multiplication")
        C = matrix_multiply(A, B)
        print(C)

        print("\nStrassen Matrix Multiplication")
        D = strassen_multiply(A, B)
        print(D)


if __name__ == "__main__":
    Run().sorting()
    Run().tower_of_hanoi()
    Run().matrix_multiplication()
