import calculator

def visualizeMatrix(matrix):
    if matrix:
        for i in range(len(matrix)):
            print(matrix[i])
        print("\n")

A = [
    [2, -1, 3],
    [4, 1, 5],
    [6, 0, 2]
]

B = [
    [1, 3, 2],
    [2, 4, 7]
]

C = [
    [1, 1, 1],
    [4, 5, 6],
    [7, 8, 9]
]

D = [
    [0, 3],
    [1, -2],
    [5, 8]
]

E = [
    [1, 3, -1, -1, -1],
    [5, 4, 3, 1, 7],
    [-1, -1, 0, 3, 2],
    [9, 9, 7, 10, 3],
    [1, 3, -2, 5, 0]
]

F = [
    [1, 0, 2, -1],
    [3, 1, 0, 2],
    [2, 1, 1, 1],
    [1, 3, 2, 0]
]

# # Inverse matrix tests
# visualizeMatrix(calculator.transpose(A))
# visualizeMatrix(calculator.transpose(B))

# # Add matrices
# visualizeMatrix(calculator.add(A, B))
# visualizeMatrix(calculator.add(A, C))

# # Multiply matrices
# visualizeMatrix(calculator.multiply(A, B))
# visualizeMatrix(calculator.multiply(B, D))

# # Find determinant
# print(calculator.determinant(A)) # should be -36
# print(calculator.determinant(E)) # should be -1368
# print(calculator.determinant(F)) # should be -6

# # Find inverse matrix
# visualizeMatrix(calculator.inverse(A))
# visualizeMatrix(calculator.inverse(E))
# visualizeMatrix(calculator.inverse(F))