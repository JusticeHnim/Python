"""
Exercise 7.4 (Medium): Subset and Superset Verification
Concept: Checking subset and superset relationships using issubset() and issuperset().
Task: Write a function check_permission_level(required_permissions, user_permissions). Return True if user_permissions is a superset of required_permissions; otherwise, return False.
Input Examples: check_permission_level({"read", "write"}, {"read", "write", "execute"}) and check_permission_level({"read", "admin"}, {"read", "write"})
Expected Output: True and False
"""