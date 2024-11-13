import json
import re
import time

def extract_json_from_string(input_string):
    # Regular expression to find JSON-like content
    json_pattern = re.compile(r'\{.*\}', re.DOTALL)
    match = json_pattern.search(input_string)
    print(match.group(0))
    
    if match:
        json_str = match.group(0)
        # Replace single quotes with double quotes
        json_str = re.sub(r"(?<=\{)\'|\'(?=\})|(?<=: )\'|\'(?=,)|(?<=, )\'|\'(?=:)|(?<=\{)\'|\'(?=\})", '"', json_str)
        
        # Check if the last 3 characters are not '}}}'
        # if not json_str.endswith('}}}'):
        #     # Calculate how many '}' are needed
        #     missing_braces = 3 - json_str.count('}', -3)
        #     json_str += '}' * missing_braces
        
        parsed_json = json.loads(json_str)
        
        
        
        return parsed_json