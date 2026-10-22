"""
Exercise 5.5 (Advanced): Log Entry Parser
Concept: Named capture groups (?P<name>...) or regex groups ().
Task: Parse a standard server log line and extract the timestamp, log level (INFO/ERROR/WARN), and message into a dictionary.
Input: log_line = "2026-10-22 10:15:30 [ERROR] Database connection failed"
Expected Output: { "timestamp": "2026-10-22 10:15:30", "level": "ERROR", "message": "Database connection failed" }
"""
import re 

log_line = "2026-10-22 10:15:30 [ERROR] Database connection failed"
# Mẫu Regex dùng cú pháp (?P<tên_group>pattern)
pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.+)"

match = re.search(pattern, log_line)

if match:
    # Hàm .groupdict() sẽ tự động chuyển các nhóm có tên thành Dictionary
    result = match.groupdict()
    print(result)
else:
    print("không tìm thấy")