def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiplication(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row1, col2)) for col2 in transpose(matrix2)] for row1 in matrix1]

def matrix_inverse(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        print("Matrix is singular, cannot find its inverse.")
        return None
    else:
        adjugate = [[matrix[1][1] / determinant, -matrix[0][1] / determinant],
                    [-matrix[1][0] / determinant, matrix[0][0] / determinant]]
        return adjugate

# Testing
A = [[2, 1], [5, 3]]
print("Original Matrix:")
for row in A:
    print(row)
print("Inverse Matrix:")
inverse_A = matrix_inverse(A)
if inverse_A:
    for row in inverse_A:
        print(row)
