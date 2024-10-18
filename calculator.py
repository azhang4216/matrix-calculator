def transpose(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(ROWS)] for j in range(COLS)]

def add(matrix1, matrix2):
    ROWS, COLS = len(matrix1), len(matrix1[0])
    if ROWS != len(matrix2) or COLS != len(matrix2[0]):
        print("The matrices are not the same dimension. Cannot be added.")
    else:
        return [[matrix1[i][j] + matrix2[i][j] for j in range(COLS)] for i in range(ROWS)]

def multiply(matrix1, matrix2):
    ROWS1, COLS1 = len(matrix1), len(matrix1[0])
    if COLS1 != len(matrix2):
        print("The number of columns in the first matrix must equal the number of rows in the second matrix. Cannot be multiplied.")
    else:
        COLS2 = len(matrix2[0])
        return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(COLS1)) for j in range(COLS2)] for i in range(ROWS1)]
    
def determinant(matrix):
    N = len(matrix)
    if N != len(matrix[0]):
        print("Determinants can only be found for square matrices.")
    else:
        '''
        Gaussian elimination method - O(n ^ 3)
        -> reduce the matrix to a form where all elements below the main diagonal are 0s
        -> determininant will be the product of the non-zero diagonal elements
        '''
        matrix_copy = [row[:] for row in matrix]   # so we don't modify the original matrix input
        det = 1

        for i in range(N):
            # Step 1. find the pivot element, which is the diagonal element we are working with for this row i
            pivot = matrix_copy[i][i]

            if pivot == 0:
                # find a row to swap, because 0 pivot cannot eliminate the numbers below it 
                swapped = False

                for j in range(i + 1, N):
                    if matrix_copy[j][i] != 0:
                        # swap rows
                        matrix_copy[i], matrix_copy[j] = matrix_copy[j], matrix_copy[i]
                        det *= -1                  # swapping rows changes the sign of determinant
                        pivot = matrix_copy[i][i]
                        swapped = True
                        break
                if not swapped:
                    # special case: no non-zero pivot -> determinant is 0
                    return 0
                
            # normalize the pivot row, ie. everything below the pivot in the same column should become 0
            for j in range(i + 1, N):
                pivot_factor = matrix_copy[j][i] / pivot
                for k in range(i, N):
                    matrix_copy[j][k] -= pivot_factor * matrix_copy[i][k]

        # multiply the diagonal elements for the determinant
        for i in range(N):
            det *= matrix_copy[i][i]
        
        # rounding the determinant to avoid floating-point issues
        return round(det)

def inverse(matrix):
    N = len(matrix)

    # simple checks for conditions of matrix
    if N != len(matrix[0]):
        print("Only the inverse of square matrices can be calculated.")
        return 
    
    det = determinant(matrix)
    if det == 0:
        print("This matrix is singular and does not have an inverse.")
        return 
    
    # create an augmented matrix [A | I]
    augmented = [row[:] + [1 if i == j else 0 for j in range(N)] for i, row in enumerate(matrix)]

    # use Gaussian elimination method to change the original matrix into the identity matrix
    for i in range(N):
        # make the pivot element 1
        pivot = augmented[i][i]
        for j in range(i, 2 * N):
            augmented[i][j] /= pivot
        
        # eliminate the column entries above and below the pivot
        for j in range(N):
            if j != i:
                factor = augmented[j][i]
                for k in range(i, 2 * N):
                    augmented[j][k] -= factor * augmented[i][k]

    return [row[N:] for row in augmented]

