"""
Concept Tested: [expression for item in iterable if condition] : ket hop them cu phap
loc du lieu if o cuoi
condition la dieu kien

Task: Cho danh sach cac so numbers. Hay dung List Comprehensions de loc ra danh sach moi
chi chua cac so lon 10.
Input: numbers = [4, 15, 8, 23, 42, 2, 11, 7]
Output: [15, 23, 42, 11]
"""

numbers = [4, 15, 8, 23, 42, 2, 11, 7]
ans = [ number for number in numbers if number>10]
print(ans)