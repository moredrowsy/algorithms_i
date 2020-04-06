"""
Dynamic Algorithms
"""
from binomial_coefficient import binomial_coefficient
from chain_matrix_multiply import chain_matrix_multiply, print_optimal_order
from floyd import floyd, print_floyd_path


class Run(object):
    """
    Run Dynamic Algorithm's methods
    """

    def binomial(self):
        """Run Binomial Coefficient algorithm"""
        print("\n\nBINOMIAL COEFFICIENT\n--------------------")

        n, k = 4, 2
        coefficient = binomial_coefficient(n, k)
        print(f"\nCoefficient[{n}][{k}] = {coefficient}")

    def floyd_algorithm(self):
        """Run Floyd's Shortest Paths Algorithm"""
        inf = float('inf')

        print("\n\nFLOYD'S ALGORITHM\n-----------------")

        # problem 1
        print("\n\nPROBLEM 1")

        weights = [
            [0, 1, inf, 1, 5],
            [9, 0, 3, 2, inf],
            [inf, inf, 0, 4, inf],
            [inf, inf, 2, 0, 3],
            [3, inf, inf, inf, 0]
        ]

        print(f"\nWeights matrix:")
        print_matrix(weights)
        result = floyd(weights)

        print("\nDistances")
        print_matrix(result['distances'])
        print("\nPaths")
        print_matrix(result['intermediate'])

        source, target = 1, 4
        print(f"\nShortest path from {source} to {target}:")
        print_floyd_path(result['intermediate'], source, target)

        # problem 2
        print("\n\nPROBLEM 2")

        weights = [
            [0, 8, 2],
            [5, 0, inf],
            [inf, 3, 0]
        ]

        print(f"\nWeights matrix:")
        print_matrix(weights)
        result = floyd(weights)

        print("\nDistances")
        print_matrix(result['distances'])
        print("\nPaths")
        print_matrix(result['intermediate'])

        source, target = 1, 2
        print(f"\nShortest path from {source} to {target}:")
        print_floyd_path(result['intermediate'], source, target)

        # problem 3
        print("\n\nPROBLEM 3")

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
        print_matrix(weights)

        result = floyd(weights)

        print("\nDistances")
        print_matrix(result['distances'])
        print("\nPaths")
        print_matrix(result['intermediate'])

        source, target = 1, 2
        print(f"\nShortest path from {source} to {target}:")
        print_floyd_path(result['intermediate'], source, target)

        # problem 4
        print("TESTING PROBLEMS USED IN DIJKSTRA")
        print("\n\nPROBLEM 1")

        weights = [
            [0, 7, 4, 6, 1],
            [inf, 0, inf, inf, inf],
            [inf, 2, 0, 5, inf],
            [inf, 3, inf, 0, inf],
            [inf, inf, inf, 1, 0]
        ]

        print(f"\nWeights matrix:")
        print_matrix(weights)
        print_matrix(weights)

        result = floyd(weights)

        print("\nDistances")
        print_matrix(result['distances'])
        print("\nPaths")
        print_matrix(result['intermediate'])

        source, target = 0, 1
        print(f"\nShortest path from {source} to {target}:")
        print_floyd_path(result['intermediate'], source, target)

        # problem 5
        print("TESTING PROBLEMS USED IN DIJKSTRA")
        print("\n\nPROBLEM 2")

        weights = [
            [0, 50, 10, inf, 45, inf],
            [inf, 0, 15, inf, 10, inf],
            [20, inf, 0, 15, inf, inf],
            [inf, 20, inf, 0, 35, inf],
            [inf, inf, inf, 30, 0, 20],
            [inf, inf, inf, 3, inf, 0]
        ]

        print(f"\nWeights matrix:")
        print_matrix(weights)
        print_matrix(weights)

        result = floyd(weights)

        print("\nDistances")
        print_matrix(result['distances'])
        print("\nPaths")
        print_matrix(result['intermediate'])

        source, target = 0, 5
        print(f"\nShortest path from {source} to {target}:")
        print_floyd_path(result['intermediate'], source, target)

        # problem 6
        print("TESTING PROBLEMS USED IN DIJKSTRA")
        print("\n\nPROBLEM 3")

        weights = [
            [0, inf, 72, 50, 90, 35],
            [inf, 0, 71, 70, 73, 75],
            [72, 71, 0, inf, 77, 90],
            [50, 70, inf, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        print(f"\nWeights matrix:")
        print_matrix(weights)
        print_matrix(weights)

        result = floyd(weights)

        print("\nDistances")
        print_matrix(result['distances'])
        print("\nPaths")
        print_matrix(result['intermediate'])

        source, target = 4, 3
        print(f"\nShortest path from {source} to {target}:")
        print_floyd_path(result['intermediate'], source, target)

    def chain_matrix(self):
        """Run Chain Matrix Multiplication algorithm"""
        print("\n\nCHAIN MATRIX MULTIPLIATION\n--------------------")

        # problem 1
        print("\n\nPROBLEM 1")

        #  A0     A1     A2     A3     A4     A5
        # 5x2    2x3    3x4    4x6    6x7    7x8
        dimensions = [5, 2, 3, 4, 6, 7, 8]
        print("\nDimensions", dimensions)

        result = chain_matrix_multiply(dimensions)
        print("\nSeperation matrix")
        print_matrix(result['seperations'])

        print("\nOrder")
        print_optimal_order(result['seperations'], 0, len(dimensions) - 2)
        print('\nCost:', result['cost'])

        # problem 2
        print("\n\nPROBLEM 2")

        #  A0     A1     A2     A3
        # 20x2   2x30   30x12  12x8
        dimensions = [20, 2, 30, 12, 8]
        print("\nDimensions", dimensions)

        result = chain_matrix_multiply(dimensions)
        print("\nSeperation matrix")
        print_matrix(result['seperations'])
        print_optimal_order(result['seperations'], 0, len(dimensions) - 2)
        print('\nCost:', result['cost'])

        # problem 3
        print("\n\nPROBLEM 3")

        #  A0     A1     A2     A3     A4
        # 10x4   4x5    5x20   20x2   2x50
        dimensions = [10, 4, 5, 20, 2, 50]
        print("\nDimensions", dimensions)

        result = chain_matrix_multiply(dimensions)
        print("\nSeperation matrix")
        print_matrix(result['seperations'])
        print_optimal_order(result['seperations'], 0, len(dimensions) - 2)
        print('\nCost:', result['cost'])


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
    Run().chain_matrix()
