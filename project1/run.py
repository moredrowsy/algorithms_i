"""
Project 1

- Sorting: Quick sort vs Merge sort
- Tower of Hanoi
- Matrix multiplication: Classical vs Strassen
"""

from sort import mergesort, quicksort
from tower_of_hanoi import TowerOfHanoi
from matrix_multiply import matrix_multiply, strassen_multiply, print_matrix


class Run(object):
    """
    Run project 1's methods
    """

    def sorting(self):
        """
        Run sorting algorithm for Merge sort and Quick sort
        """
        print("\n\nSORTING ALGORITHMS\n" + "=" * 80)

        list1 = [3, 5, 0, 4, 8, 2, 1]
        list2 = [3, 5, 0, 4, 8, 2]
        print("\nUnsorted list")
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

        print("\n\nTOWER OF HANOI\n" + "=" * 80)

        toh = TowerOfHanoi(A, B, C, "A", "B", "C")

        print("\nTower of Hanoi Setup")
        toh.print()

        toh.solve(display=True)

        print("\nTower of Hanoi Solution")
        toh.print()

    def matrix_multiplication(self):
        print("\n\nMATRIX MULTIPLICATION\n" + "=" * 80)

        A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
        B = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

        print("\nMatrix A\n" + "-" * 8)
        print_matrix(A)
        print("\nMatrix B\n" + "-" * 8)
        print_matrix(B)

        print("\nClassical Matrix Multiplication")
        C = matrix_multiply(A, B)
        print("\nMatrix C\n" + "-" * 8)
        print_matrix(C)

        print("\nStrassen Matrix Multiplication")
        D = strassen_multiply(A, B)
        print("\nMatrix D\n" + "-" * 8)
        print_matrix(D)

        print("\nResetting matrices\n" + "-" * 18)

        A = [[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9],
             [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]
        B = [[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9],
             [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16], [16, 15, 14, 13, 12, 11, 10, 9]]

        print("\nMatrix A\n" + "-" * 8)
        print_matrix(A)
        print("\nMatrix B\n" + "-" * 8)
        print_matrix(B)

        print("\nClassical Matrix Multiplication")
        C = matrix_multiply(A, B)
        print("\nMatrix C\n" + "-" * 8)
        print_matrix(C)

        print("\nStrassen Matrix Multiplication")
        D = strassen_multiply(A, B)
        print("\nMatrix D\n" + "-" * 8)
        print_matrix(D)


if __name__ == "__main__":
    Run().sorting()
    Run().tower_of_hanoi()
    Run().matrix_multiplication()
