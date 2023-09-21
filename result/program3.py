import re

def is_valid_ip(ip):
    # Regular expression pattern to match a valid IPv4 address
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    if re.match(pattern, ip):
        return True
    else:
        return False


# Test cases
test_cases = [
    "255.255.0.0",     # Valid IP
    "555.555.555.555", # Invalid IP (out of range)
    "256.255.0.0",     # Invalid IP (out of range)
    "0.0.0.0",         # Valid IP
    "192.168.1.1",     # Valid IP
]

for test_case in test_cases:
    try:
        result = is_valid_ip(test_case)
        print(f"Input: {test_case}, Output: {result}")
    except Exception as e:
        print(f"Input: {test_case}, Error: {str(e)}")
