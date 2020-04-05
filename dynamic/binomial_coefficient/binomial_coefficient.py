"""
Binomial Coefficient: Find the coefficient given with n and k
"""


def binomial_coefficient(n, k):
    """
    Calculate binomial coefficient via dynamic approach

    Time complexity: O(nk):
    Complexity breakdown:
        n x k array: nk
        for loop outer: n
        for loop inner: at most k
        total: nk + nk = O(nk)

    Parameters
    ----------
    n (int): First coefficient
    k (int): Second coefficient

    Return
    ------
    int: binomial coefficient of n and k
    """
    # create coefficient array of [0...n][0...k]
    C = [[0 for j in range(k + 1)] for i in range(n + 1)]

    # calculate binomial coefficients in array
    for i in range(n + 1):
        for j in range(0, min(i + 1, k + 1)):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]
