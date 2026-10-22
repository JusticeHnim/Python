"""
Given a list of names "names = ["alice", "BOB", "charlie", "David"].
Use List Comprehension to format all name in Capitalized form (first letter uppercase, rest lowercase)

Expected Output: ['Alice', 'Bob', 'Charlie', 'David']
"""
names = ["alice", "BOB", "charlie", "David"]
answer = [name.capitalize() for name in names]
print(answer)