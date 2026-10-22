"""
Exercise 5.2 (Medium): Basic Email Validator 
Concept: Using re.match() or re.search() with character classes (\w, ., @). 
Task: Write a function is_valid_email(email) that checks if a string is a valid email address 
(contains characters before @, a domain name, and a dot followed by a top-level domain like .com or .org).
Input List: ["user@example.com", "invalid_email.com", "john.doe@company.org"] 
Expected Output: [True, False, True]
"""
import re

def is_valid_email(email):
    pattern = r"^[\w.]+@[\w-]+\.[a-zA-Z]{2,}$"
    return(bool(re.search(pattern, email)))

input_list = ["user@example.com", "invalid_email.com", "john.doe@company.org"]
answer = [is_valid_email(email) for email in input_list]
print(answer)