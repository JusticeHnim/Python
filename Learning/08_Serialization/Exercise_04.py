"""
Exercise 8.4 (Medium/Hard): Custom Datetime JSON Serializer
Concept: Handling non-serializable objects like datetime in json.dumps().
Task: Write a custom serializer function serialize_datetime(obj) to pass into the default parameter of json.dumps(). Convert datetime objects into ISO format strings (YYYY-MM-DDTHH:MM:SS).
Input Data: data = {"event": "Python Workshop", "timestamp": datetime.now()}
Expected Output: Valid JSON string containing timestamp in ISO string format.
"""