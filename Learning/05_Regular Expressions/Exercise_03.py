"""Exercise 5.3 (Medium): Extract Phone Numbers Concept: 
Exact count quantifiers {n} and special character escaping -. 
Task: Given a paragraph, extract all phone numbers formatted as XXX-XXX-XXXX (where X is a digit). 
Input: text = "Call support at 123-456-7890 or manager at 987-654-3210 for assistance." 
Expected Output: ['123-456-7890', '987-654-3210']
"""
import re

text = "Call support at 123-456-7890 or manager at 987-654-3210 for assistance."
#pattern = r"\d{3}-\d{3}-\d{4}"
#match = re.findall(pattern, text)

match = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(match)