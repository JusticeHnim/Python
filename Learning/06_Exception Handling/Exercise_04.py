"""
Exercise 6.4 (Medium/Hard): File Reader with Cleanup
Concept: Catching FileNotFoundError and utilizing the finally block.
Task: Write a function read_file_safely(filename) that attempts to open and read a text file. 
Handle FileNotFoundError if the file does not exist. 
Use a finally block to ensure a message "Attempted to process file." is printed regardless of the outcome.
Input Examples: "existing_file.txt" vs "missing_file.txt"
Expected Output: File content (or error message) followed by the finally cleanup message
"""