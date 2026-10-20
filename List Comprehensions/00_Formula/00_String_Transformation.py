#Concept Tested: [expression for item in iterable] : Cau truc co ban nhat cua LC
#expression la bien hoac bieu thuc, item la bien dem cua vong lap, iterable la danh sach lap

"""
Task: Cho danh sách tên names. Hãy dùng List Comprehension để tạo một danh sách mới 
chứa tất cả các tên đã được chuyển thành chữ in hoa toàn bộ (dùng phương thức .upper()).
Input: names = ["alice", "bob", "charlie", "david"]
Expected Output: ['ALICE', 'BOB', 'CHARLIE', 'DAVID']
"""
names = ['cong', 'minh', 'yeu', 'anh', 'thu']
upper_names = [name.upper() for name in names]
print(upper_names)