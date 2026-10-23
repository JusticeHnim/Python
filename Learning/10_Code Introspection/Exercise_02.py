"""
Exercise 10.2 (Medium): Safe Attribute Getter
Concept: Dynamic attribute verification using hasattr() and getattr().
Task: Create a class Car with attributes brand="Toyota" and speed=120. Write a function get_car_info(car_obj, attr_name) that uses hasattr() to check if attr_name exists. If it exists, return getattr(car_obj, attr_name); otherwise, return "Attribute does not exist!".
Input Examples: get_car_info(my_car, "brand") and get_car_info(my_car, "color")
Expected Output: "Toyota" and "Attribute does not exist!"
"""