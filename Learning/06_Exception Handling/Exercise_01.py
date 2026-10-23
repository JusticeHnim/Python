"""Exercise 6.1 (Easy): Safe Division Operator

Concept: Handling ZeroDivisionError with try-except.
Task: Write a function safe_divide(a, b) that divides a by b. 
If b is zero, catch the ZeroDivisionError and return "Cannot divide by zero!". Otherwise, return the division result.
Input Examples: safe_divide(10, 2) and safe_divide(5, 0)
Expected Output: 5.0 and "Cannot divide by zero!"
"""

def safe_divide(a, b):
    return float(a/b)

try:
    answer1 = safe_divide(10, 2)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(answer1)

try:
    answer2 = safe_divide(5, 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(answer2)
