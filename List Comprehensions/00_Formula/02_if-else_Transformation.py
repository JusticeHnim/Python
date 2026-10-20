"""
Concept Tested: [true_expr if condition else fale_expr for item in iterable] : if-else nam phia truoc for

Task: Cho danh sach diem scores. Dung List Comprehension de phan loai ket qua:
- Neu diem tu 50 tro len la "Pass"
- Neu diem duoi 50 la "Fail"
Input: scores = [85, 78, 30, 95, 50]
Ouput: ['Pass', 'Pass', 'Fail', 'Pass', 'Pass']
"""

scores = [85, 78, 30, 95, 50]
binary_assessment = ['Pass' if score>=50 else 'Fail' for score in scores]
print(binary_assessment)