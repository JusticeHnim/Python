"""
Exercise 8.5 (Hard): Safe Pickle File Handler
Concept: Handling FileNotFoundError and UnpicklingError during binary deserialization.
Task: Write a function load_binary_data(filename) that attempts to open a binary file and deserialize it using pickle.load(). Use try-except to catch FileNotFoundError and pickle.UnpicklingError, returning appropriate error messages.
Input Examples: Non-existent file name vs valid binary file name.
Expected Output: "File not found!" or "Corrupted binary data!" or deserialized object.
"""