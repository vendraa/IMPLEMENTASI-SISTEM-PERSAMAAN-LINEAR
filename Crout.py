def crout_decomposition(matrix):
    n = len(matrix)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for j in range(n):
        U[j][j] = 1
        for i in range(j, n):
            sum = 0
            for k in range(j):
                sum += L[i][k] * U[k][j]
            L[i][j] = matrix[i][j] - sum

        for i in range(j + 1, n):
            sum = 0
            for k in range(j):
                sum += L[j][k] * U[k][i]
            U[j][i] = (matrix[j][i] - sum) / L[j][j]

    return L, U

# Testing
A = [[2, -1, 3], [4, 4, -2], [-4, -2, 8]]
L, U = crout_decomposition(A)
print("Matrix A:")
for row in A:
    print(row)
print("Lower Triangular Matrix (L):")
for row in L:
    print(row)
print("Upper Triangular Matrix (U):")
for row in U:
    print(row)
