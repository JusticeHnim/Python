"""
Exercise 7.3 (Medium): Safe Set Element Removal
Concept: Distinguishing between remove() and discard().
Task: Write a function remove_member(member_set, name, strict=False). If strict is True, use .remove() and catch the KeyError if the member does not exist. If strict is False, use .discard() to remove silently.
Input Examples: remove_member({"Alice", "Bob"}, "Charlie", strict=True) and remove_member({"Alice", "Bob"}, "Charlie", strict=False)
Expected Output: Print "Member not found!" for strict mode; run cleanly without error for non-strict mode.
"""