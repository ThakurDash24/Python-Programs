def get_matrix_input():
    print("Enter the elements for the 2x2 matrix:")
    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            element = float(input(f'Enter the element [{i+1},{j+1}]: '))
            row.append(element)
        matrix.append(row)
    return matrix

def extract_elements(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    return a, b, c, d

def calculate_determinant(matrix):
    a, b, c, d = extract_elements(matrix)
    return a * d - b * c

# Main program
matrix = get_matrix_input()
res = calculate_determinant(matrix)
print(f'Determinant of the given matrix is: {res}')
