# utils.py

import re

# Define valid operators and operands
VALID_OPERATORS = {'AND', 'OR', 'NOT'}
VALID_OPERANDS = {'age', 'salary', 'experience', 'department'}

def validate_rule_string(rule_string):
    """
    Validate the rule string to ensure it contains valid operators and operands.
    
    Parameters:
    rule_string (str): The rule string to validate.
    
    Returns:
    bool: True if the rule string is valid, False otherwise.
    str: Error message if invalid, empty string if valid.
    """
    
    # Simple regex to match the expected structure
    pattern = r'\b(?:' + '|'.join(VALID_OPERANDS) + r')\s*(?:<=|>=|<|>|==|!=)\s*\d+|\w+\b'
    matches = re.findall(pattern, rule_string)
    
    if not matches:
        return False, "Rule string does not match expected format."
    
    # Check for valid operators and operands in the rule string
    tokens = rule_string.split()
    for token in tokens:
        if token in VALID_OPERATORS:
            continue  # Valid operator
        if not any(token.startswith(operand) for operand in VALID_OPERANDS):
            return False, f"Invalid operand: {token}"

    return True, ""
