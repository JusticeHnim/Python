"""
Exercise 9.3 (Medium): Logger with Preset Log Levels
Concept: Building specialized logging functions with partial().
Task: Write a function log_message(level, message). Use partial() to create three dedicated functions: log_info(message), log_warning(message), and log_error(message) where level is pre-set to "INFO", "WARNING", and "ERROR".
Input Example: log_info("Server started") and log_error("Connection failed")
Expected Output: "[INFO] Server started" and "[ERROR] Connection failed"
"""