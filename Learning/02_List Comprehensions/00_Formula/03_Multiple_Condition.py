"""
Concept Tested: Using logic operators (or, and,...) or string methods (.startswith(), len()) 
in filter clause.
operator la toan tu, method la phuong thuc

Task: Giving a words list
words = ['apple', 'banana', 'kiwi', 'cherry', 'fig', 'avocado']. Creating a new list 
only words begin 'a' or length greater than 4 character.
Input: words = ['apple', 'banana', 'kiwi', 'cherry', 'fig', 'avocado'].
Output: ['apple', 'banana', 'cherry' , 'avocado']
"""

words = ['apple', 'banana', 'kiwi', 'cherry', 'fig', 'avocado']
answer = [word for word in words if word.startswith("a") or len(word)>4] # .startswith(value, start, end)
print(answer)

