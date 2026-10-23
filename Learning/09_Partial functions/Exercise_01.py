"""
Exercise 9.1 (Easy): Discount Price Calculator
Concept: Freezing arguments using functools.partial.
Task: Write a base function apply_discount(price, discount_rate). Use partial() to create two specialized functions:
1. vip_discount(price): applies a fixed 20% discount (0.20).
2. flash_sale_discount(price): applies a fixed 50% discount (0.50).
Input Example: vip_discount(1000) and flash_sale_discount(1000)
Expected Output: 800.0 and 500.0
"""