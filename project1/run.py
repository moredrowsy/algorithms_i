"""
Project 1
"""

from sort import mergesort, quicksort
from tower_of_hanoi import TowerOfHanoi


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
        mergesort(list1, len(list1))
        mergesort(list2, len(list2))
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        list1 = [3, 5, 0, 4, 8, 2, 1]
        list2 = [3, 5, 0, 4, 8, 2]
        print("\nUnsorted list")
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        print("\nRunning quick sort")
        quicksort(list1, len(list1))
        quicksort(list2, len(list2))
        print(f"list1: {list1}")
        print(f"list2: {list2}")

    def tower_hanoi(self):
        A = [3, 2, 1]
        B = []
        C = []

        game1 = TowerOfHanoi(A, B, C, "A", "B", "C")

        print("\nSetup")
        game1.print_pegs()

        game1.solve(display=True)

        print("\nSolution")
        game1.print_pegs()


if __name__ == "__main__":
    Run().sorting()
    Run().tower_hanoi()
