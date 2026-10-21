"""
Given a 2D matrix "matrix = [[1, 2], [3, 4], [5, 6]]". 
Use a Nested List Comprehension to transpose the matrix into 
a 2-row by 3-column matrix.
Expected Output: [[1, 3, 5], [2, 4, 6]]
"""
matrix = [[1,2], [3, 4], [5, 6]]
answer = [[row[i] for row in matrix] for i in range(2)] #row[0] == matrix[0][0] i=0,1
print(answer)