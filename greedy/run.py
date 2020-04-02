"""
Greedy Approach Algorithms
"""
import sys
from prim import prim


class Run(object):
    """
    Run project 1's methods
    """

    def prim(self):
        """Run sorting algorithm for Merge sort and Quick sort
        """
        INF = sys.maxsize

        # problem 1
        weights = [
            [0, 1, 3, INF, INF],
            [1, 0, 3, 6, INF],
            [3, 3, 0, 4, 2],
            [INF, 6, 4, 0, 5],
            [INF, INF, 2, 5, 0],
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        final_set = prim(weights)

        print("\nMST (Prim's Algorithm)")
        print(final_set)

        # problem 2
        weights = [
            [0, 13, 3, 22, 8, INF, INF, INF],
            [13, 0, INF, 9, INF, INF, INF, INF],
            [3, INF, 0, INF, 9, INF, INF, INF],
            [22, 9, INF, 0, INF, 10, INF, INF],
            [8, INF, 9, INF, 0, 15, 10, INF],
            [INF, INF, INF, 10, 15, 0, INF, 12],
            [INF, INF, INF, INF, 10, INF, 0, INF],
            [INF, INF, INF, INF, 12, INF, INF, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        final_set = prim(weights)

        print("\nMST (Prim's Algorithm)")
        print(final_set)


if __name__ == "__main__":
    Run().prim()
