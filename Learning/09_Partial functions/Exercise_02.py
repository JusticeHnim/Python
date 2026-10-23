"""
Exercise 9.2 (Medium): Base Conversion Helper
Concept: Fixing keyword arguments in built-in functions.
Task: Python's built-in int(x, base=10) converts string numbers in different bases. Use partial() to create:
1. parse_binary(binary_str): converts binary strings (base=2) to integers.
2. parse_hex(hex_str): converts hexadecimal strings (base=16) to integers.
Input Examples: parse_binary("1010") and parse_hex("FF")
Expected Output: 10 and 255
"""