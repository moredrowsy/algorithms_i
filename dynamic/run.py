"""
Dynamic Algorithms
"""
from binomial_coefficient import binomial_coefficient
from floyd import floyd, print_floyd_path


class Run(object):
    """
    Run Dynamic Algorithm's methods
    """

    def binomial(self):
        """Run Binomial Coefficient algorithm"""
        n, k = 4, 2
        coefficient = binomial_coefficient(n, k)
        print(f"Binomial Coefficient\nC[{n}][{k}] = {coefficient}")

    def floyd_algorithm(self):
        """Run Floyd's Shortest Paths Algorithm"""
        INF = float('inf')

        # problem 1
        weights = [
            [0, 1, INF, 1, 5],
            [9, 0, 3, 2, INF],
            [INF, INF, 0, 4, INF],
            [INF, INF, 2, 0, 3],
            [3, INF, INF, INF, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        result = floyd(weights)

        print("\nFloyd's Shortest Paths")
        print("Distances")
        print_matrix(result['distances'])
        print("Paths")
        print_matrix(result['paths'])

        source, target = 1, 4
        print(f"Shortest path from {source} to {target}:")
        print_floyd_path(result['paths'], source, target)


def print_matrix(A, pad_size=3, sep=" ", end="\n"):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{(A[i][j]):>{pad_size}}", end=sep)
        if i == len(A) - 1:
            print(end, end="")
        else:
            print()


if __name__ == "__main__":
    Run().binomial()
    Run().floyd_algorithm()
