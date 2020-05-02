"""
Chain Matrix Multiplication: Finding the optimum order to chain multiply
matrices with the minimum number of elementary multiplications
"""


def chain_matrix_multiply(dimensions):
    """
    Chain Matrix Multiplication: Finding the optimum order to chain multiply
    matrices with the minimum number of elementary multiplications.

    Time Complexity: O(n^3)
    Complexity breakdown:
        for loop diagonal: n - 1
        for loop i: n
        for loop k: n + 1
        total: (n - 1)(n)(n + 1) = O(n^3)

    Parameters
    ----------
    dimensions (1D array): List of all matrix dimensions. Len of array is
        number of matrices + 1

    Example of dimensions array:
        A0     A1     A2     A3     A4     A5
        5x2    2x3    3x4    4x6    6x7    7x8

        dimensions = [5, 2, 3, 4, 6, 7, 8]

    Return
    ------
    {seperations: 2D array of seperation indices, cost: total multiplications}

    NOTE
    ----
    multiplications[]: Holds the minimum total elementary multiplications for
        each permutation from i "through" j.
        Ex: i = 2, j = 4; Total multiplications is from A2 through A4
    seperations[]: Hold matrix indices for order seperations for minimum cost
    """
    n = len(dimensions) - 1
    multiplications = [[float('inf') for j in range(n)] for i in range(n)]
    seperations = [[float('inf') for j in range(n)] for i in range(n - 1)]

    # main diagonal has 0 cost
    for i in range(n):
        multiplications[i][i] = 0

    # calculate non-main diagonals
    for diagonal in range(1, n):
        for i in range(n - diagonal):
            j = i + diagonal

            for k in range(i, j):
                cost = multiplications[i][k] + multiplications[k+1][j] + \
                    dimensions[i] * dimensions[k+1] * dimensions[j+1]

                if cost < multiplications[i][j]:
                    multiplications[i][j] = cost
                    seperations[i][j] = k

    return {'seperations': seperations, 'cost': multiplications[0][n-1]}


def print_optimal_order(sep, source, target, prefix="A"):
    """
    Print matrix order by the seperations array with given index of starting
    matrix through ending matrix.

    EX: source = 0, target = 5; Will print order from Matrix 0 to Matrix 5

    Parameters
    ----------
    sep (2D array): List of matrix order seperations
    source (int): Index of starting matrix
    target (int): Index of ending matrix
    """
    if source == target:
        print(f"{prefix}{source}", end="")
    else:
        print("(", end="")
        print_optimal_order(sep, source, sep[source][target])
        print_optimal_order(sep, sep[source][target] + 1, target)
        print(")", end="")
