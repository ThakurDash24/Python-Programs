def find_character(matrix, char):
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == char:
                print(f"Row index: {row_index}, Column index: {col_index}")
                return
    print("Not found")

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
char = 'h'
find_character(matrix, char)  
