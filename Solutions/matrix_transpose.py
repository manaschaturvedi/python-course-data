# Approach 1
transposed = []
matrix = [[1, 2], [3,4], [5,6], [7,8]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


# Approach 2: List comprehensions
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print (transpose)