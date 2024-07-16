def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f'Enter the element [{i+1},{j+1}]: '))
            row.append(element)
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
   
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


rows_A, cols_A = 3, 3
rows_B, cols_B = 3, 4


print("Matrix A:")
A = get_matrix_input(rows_A, cols_A)

print("Matrix B:")
B = get_matrix_input(rows_B, cols_B)

result = multiply_matrices(A, B)
print("Resultant matrix after multiplication:")
for row in result:
    print(row)
