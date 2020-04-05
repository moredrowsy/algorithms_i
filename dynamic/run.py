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
        inf = float('inf')

        # problem 1
        weights = [
            [0, 1, inf, 1, 5],
            [9, 0, 3, 2, inf],
            [inf, inf, 0, 4, inf],
            [inf, inf, 2, 0, 3],
            [3, inf, inf, inf, 0]
        ]

        print(f"\nWeights matrix:")
        result = floyd(weights)

        print("\nFloyd's Shortest Paths")
        print("Distances")
        print_matrix(result['distances'])
        print("Paths")
        print_matrix(result['paths'])

        source, target = 1, 4
        print(f"Shortest path from {source} to {target}:")
        print_floyd_path(result['paths'], source, target)

        # problem 2
        weights = [
            [0, 8, 2],
            [5, 0, inf],
            [inf, 3, 0]
        ]

        print(f"\nWeights matrix:")
        result = floyd(weights)

        print("\nFloyd's Shortest Paths")
        print("Distances")
        print_matrix(result['distances'])
        print("Paths")
        print_matrix(result['paths'])

        source, target = 1, 2
        print(f"Shortest path from {source} to {target}:")
        print_floyd_path(result['paths'], source, target)

        # problem 3
        weights = [
            [0, 4, inf, inf, inf, 10, inf],
            [3, 0, inf, 18, inf, inf, inf],
            [inf, 6, 0, inf, inf, inf, inf],
            [inf, 5, 15, 0, 2, 19, 5],
            [inf, inf, 12, 1, 0, inf, inf],
            [inf, inf, inf, inf, inf, 0, 10],
            [inf, inf, inf, 8, inf, inf, 0]
        ]

        print(f"\nWeights matrix:")
        print_matrix(weights)

        result = floyd(weights)

        print("\nFloyd's Shortest Paths")
        print("Distances")
        print_matrix(result['distances'])
        print("Paths")
        print_matrix(result['paths'])

        source, target = 1, 2
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
