"""
Exercise 7.5 (Hard): Disjoint Sets and Common Interest Finder
Concept: Checking disjoint sets using isdisjoint() and finding shared items across sets.
Task: Write a function find_shared_interests(user1_tags, user2_tags). First, check if the two tag sets are disjoint using isdisjoint(). If they have no common tags, return "No common interests". Otherwise, return the intersection of the two tag sets.
Input Examples: find_shared_interests({"python", "ai", "web"}, {"java", "c++"}) and find_shared_interests({"python", "ai", "web"}, {"ai", "data", "python"})
Expected Output: "No common interests" and {'python', 'ai'}
"""