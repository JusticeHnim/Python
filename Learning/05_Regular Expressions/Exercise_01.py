"""
Extract All Digits
Concept: Using re.findall() with "\d+".
Task: Given a string containing prices, write a function using re.findall() to extract all numeric values as a list of strings.
Input: text = "Item A costs $45, Item B costs $120, and Item C costs $5."
Expected Output: ['45', '120', '5']

extract: truy xuat
"""
import re

text = "Item A costs $45, Item B costs $120, and Item C costs $5"
cost = re.findall(r"\d+", text)
print(cost)