"""
Exercise 6.3 (Medium): Multiple Exception Handler
Concept: Catching multiple distinct exceptions (ValueError &amp; ZeroDivisionError).
Task: Write a function calculate_reciprocal(value_str) that converts value_str to a float and calculates 1 / value. 
Use separate except blocks to handle ValueError (if text is invalid) and ZeroDivisionError (if value is 0).
Input Examples: "4", "0", and "abc"
Expected Output: 0.25, error message for zero division, error message for invalid input
"""

def calculate_reciprocal(value_str):
    try:
        value = float(value_str)
        division = 1 / value
    except ZeroDivisionError:
        print("Don't use number 0.")
        return
    except ValueError:
        print("Error value, don't use alphabet.")
        return
    else:
        print(division)
        return

calculate_reciprocal("4")
calculate_reciprocal("0")
calculate_reciprocal("abc")