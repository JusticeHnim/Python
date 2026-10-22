"""
Given a list of test scores "scores = [45, 85, 30, 90, 60].
Use if-else within a List Comprehension to assign the label "Pass" if the score
is >=50, otherwise assign "Fail".

Expected Output: ['Fail', 'Pass', 'Fail', 'Pass', 'Pass']
"""
scores = [45, 85, 30, 90, 60]
answer = ["Pass" if score >= 50 else "Fail" for score in scores]
print(answer)