"""
Exercise 9.5 (Hard): Custom Currency Converter
Concept: Freezing positional and keyword arguments for API simulation.
Task: Write a function convert_currency(amount, exchange_rate, fee_percentage=0.01). Use partial() to create convert_usd_to_vnd(amount) with fixed exchange_rate=25000 and fee_percentage=0.02.
Input Example: convert_usd_to_vnd(100)
Expected Output: Total converted value in VND taking into account the fee.
"""