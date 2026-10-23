"""
Exercise 6.5 (Hard): Custom Age Validator using raise
Concept: Explicitly raising exceptions with custom error messages.
Task: Write a function register_user(username, age). 
If age is less than 18 or negative, raise a ValueError with the message "User must be at least 18 years old.". 
Wrap the function call in a try-except block to catch and print the error message.
Input Examples: register_user("Alice", 20) and register_user("Bob", 15)
Expected Output: "Registration successful for Alice" and "Error: User must be at least 18 years old."
"""