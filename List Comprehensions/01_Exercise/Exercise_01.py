"""
Given a list numbers = [-5, 3, -1, 10, 7, -2, 4]. Use List Comprehension
to filter out negative numbers and compute the squares of the positive numbers.

Expect Output: [9, 100, 49, 16]
"""
numbers = [-5, 3, -1, 10, 7, -2, 4]
answer = [ num*num for num in numbers if num > 0]
print(answer)