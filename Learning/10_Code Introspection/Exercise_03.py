"""
Exercise 10.3 (Medium/Hard): Dynamic Method Executer
Concept: Checking if an attribute is callable and executing it dynamically.
Task: Create a class Calculator with methods add(a, b) and multiply(a, b). Write a function execute_method(obj, method_name, *args) that checks if method_name exists and is callable using callable(getattr(obj, method_name)). If valid, call the method with *args; otherwise, return "Method not executable!".
Input Examples: execute_method(calc, "add", 5, 3) and execute_method(calc, "brand")
Expected Output: 8 and "Method not executable!"
"""