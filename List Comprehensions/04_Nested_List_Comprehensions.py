"""
Concept Tested: Using Nested List Comprehension to flatten a two-dimensional matrix 
with conditional filters.
Nested List Comprehension la list comprehension long nhau, dung de lam phang ma tran.

Task: Giving a matrix (a list of lists containing numbers). Creating a new flat list 
that only contains numbers greater than 5.
Input: matrix = [[2, 7, 4], [9, 1, 6], [5, 8, 3]]
Output: [7, 9, 6, 8]
"""

matrix = [[2, 7, 4], [9, 1, 6], [5, 8, 3]]
# Vong lap ngoai (for row in matrix) viet truoc, vong lap trong (for num in row) viet sau
answer = [num for row in matrix for num in row if num > 5]
print(answer)