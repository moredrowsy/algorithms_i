"""
Project 1
"""

from sort import mergesort, quicksort


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
        print("Printing unsorted list")
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        print("\nRunning merge sort")
        mergesort(list1, 0, len(list1)-1)
        mergesort(list2, 0, len(list2)-1)
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        list1 = [3, 5, 0, 4, 8, 2, 1]
        list2 = [3, 5, 0, 4, 8, 2]
        print("\nPrinting unsorted list")
        print(f"list1: {list1}")
        print(f"list2: {list2}")

        print("\nRunning quick sort")
        quicksort(list1, 0, len(list1)-1)
        quicksort(list2, 0, len(list2)-1)
        print(f"list1: {list1}")
        print(f"list2: {list2}")


if __name__ == "__main__":
    Run().sorting()
