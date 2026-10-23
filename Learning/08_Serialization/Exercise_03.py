"""
Exercise 8.3 (Hard): Binary Object Serialization with Pickle
Concept: Serializing custom class instances using pickle.
Task: Define a class Player(name, level, score). Instantiate an object player1 = Player("DragonSlayer", 50, 9950). Use pickle.dumps() to convert it into bytes, then use pickle.loads() to recreate the object and print its score.
Expected Output: Bytes representation and restored player's score: 9950.
"""