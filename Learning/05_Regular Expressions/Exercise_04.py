"""
Exercise 5.4 (Hard): Sensitive Data Masking Concept: Using re.sub() with groups to mask information. 
Task: Write a function to mask a 16-digit credit card number (XXXX-XXXX-XXXX-XXXX), replacing the first 12 digits 
with * and keeping only the last 4 digits visible. 
Input: card = "1234-5678-9012-3456" 
Expected Output: "****-****-****-3456" 
"""
import re 
def mask_credit_card(card): 
	# Pattern: Bắt 3 cụm 4 chữ số đầu, và tạo Group 1 () cho 4 chữ số cuối 
	pattern = r"\d{4}-\d{4}-\d{4}-(\d{4})" 
	#\1 đại diện cho giá trị của Group 1 đã giữ lại (4 chữ số cuối) 
	masked_card = re.sub(pattern, r"****-****-****-\1", card) 
	return masked_card 
# Kiểm tra kết quả
card = "1234-5678-9012-3456" 
print(mask_credit_card(card)) 