"""
Exercise 6.2 (Easy/Medium): Integer Conversion Guard
Concept: Handling ValueError during user input casting.
Task: Write a function get_user_age() that prompts the user for their age using input(). 
Use int() to convert the string to an integer. If a ValueError occurs, print "Invalid age! Please enter numbers only." and return None.
Input Examples: "25" and "twenty"
Expected Output: 25 and None (with error message printed)
"""

def get_user_age():
    try:
        age = int(input())
    except ValueError:
        print("Invalid age! Please enter numbers only.")
        return None
    else:
        return age

print(get_user_age())
