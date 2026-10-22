logs = [ 
    "INFO: System started", 
    "ERROR: Disk full", 
    "WARNING: High memory usage", 
    "ERROR: Network timeout", 
    "INFO: User logged in", 
]

def filter_error(log_list):
    for log in log_list:
        if "ERROR" in log:
            yield log

print(next(filter_error(logs)))