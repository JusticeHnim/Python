"""
Given a list of words "words = ["apple", "banana", "kiwi", "orange", "grape"]".
Filter out words that have a length > 4 and start with a vowel (a, e, i, o, u).

Expected Output: ['apple', 'orange']
"""
words = ["apple", "banana", "kiwi", "orange", "grape"]

def isVowel(word):
    if word.startswith("a") or word.startswith("e") or word.startswith("i") or word.startswith("o") or word.startswith("u"):
        return True
    
answer = [w for w in words if isVowel(w) and len(w) > 4]
print(answer)