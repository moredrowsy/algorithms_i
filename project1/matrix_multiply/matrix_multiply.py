def matrix_multiply(A, B):
    """
    Classical matrix multiplication of using 3 loops.

    Parameters
    ----------
    A (array): First matrix of m x n
    B (array): Second matrix of n x p

    Return
    ------
    C (array): Resultant array of size m x p
    """
    assert len(A) == len(B[0])
    assert len(A[0]) == len(B)

    C = []
    for i in range(len(A)):
        # temporary array of row elements
        row = []

        for j in range(len(A)):
            # initialze first multiplication
            row.append(A[i][0] * B[0][j])

            for k in range(1, len(A[0])):
                # sum the rest of the multiplications
                row[-1] += (A[i][k] * B[k][j])

        # add finished row to matrix C
        C.append(row)

    return C


def strassen_multiply(A, B):
    """
    Strassen matrix multiplication: recursively multiply by using 4 submatrices.
    Uses 7 multiplication and 18 additions for each call.
    Currently only works for matrix size n = 2, 4, 8, 16, etc.

    Parameters
    ----------
    A (array): First matrix of n x n
    B (array): Second matrix of n x n

    Return
    ------
    C (array): Resultant array of size n x n
    """
    if len(A) == 2:
        return matrix_multiply_2x2(A, B)
    else:
        # split A and B by half
        A11, A12, A21, A22 = halve_matrix(A)
        B11, B12, B21, B22 = halve_matrix(B)

        # compute subcomponents for C submatrices
        P = strassen_multiply(matrix_add(A11, A22), matrix_add(B11, B22))
        Q = strassen_multiply(matrix_add(A21, A22), B11)
        R = strassen_multiply(A11, matrix_sub(B12, B22))
        S = strassen_multiply(A22, matrix_sub(B21, B11))
        T = strassen_multiply(matrix_add(A11, A12), B22)
        U = strassen_multiply(matrix_sub(A21, A11), matrix_add(B11, B12))
        V = strassen_multiply(matrix_sub(A12, A22), matrix_add(B21, B22))

        # compute C submatrices
        C11 = matrix_sub(matrix_add(P, S), matrix_add(T, V))
        C12 = matrix_add(R, T)
        C21 = matrix_add(Q, S)
        C22 = matrix_sub(matrix_add(P, R), matrix_add(Q, U))

        # merge C submatrices into C
        C = []
        for i in range(len(C11)):
            C.append(C11[i] + C12[i])
        for i in range(len(C21)):
            C.append(C21[i] + C22[i])

        return C


def matrix_multiply_2x2(A, B):
    """Multiply matrix A with matrix B of size 2x2. Return resultant matrix
    """
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def matrix_add(A, B):
    """Add matrix A with matrix B. Return resultant matrix
    """
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matrix_sub(A, B):
    """Subtract matrix A with matrix B. Return resultant matrix
    """
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def merge_matrix(A, B):
    n = len(A) + len(B)


def halve_matrix(X):
    """
    Halve the matrix into four submatrices for matrix size n = 2, 4, 8, 16, etc.

    Return
    ------
    Four submatrices of X, of size n/2 each.
    """
    low = 0
    high = len(X)
    mid = (low + high) // 2

    # A = top left, B = top right, C = bottom left, D = bottom right halves
    A = [[X[i][j] for j in range(low, mid)] for i in range(low, mid)]
    B = [[X[i][j] for j in range(mid, high)] for i in range(low, mid)]
    C = [[X[i][j] for j in range(low, mid)] for i in range(mid, high)]
    D = [[X[i][j] for j in range(mid, high)] for i in range(mid, high)]

    return A, B, C, D
