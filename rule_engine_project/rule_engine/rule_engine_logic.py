import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left  # Left operand
        self.right = right  # Right operand
        self.value = value  # Condition or operator

    def modify(self, new_value=None, new_operator=None):
        """Modify the node's condition or operator."""
        if new_value:
            self.value = new_value
        if new_operator and self.type == "operator":
            self.value = new_operator


def parse_condition(condition):
    print(f"Parsing condition: '{condition}'")  # Debugging
    match = re.match(r"(\w+)\s*(>|<|=)\s*'?([\w\s]+)'?", condition)
    if match:
        return match.groups()
    raise ValueError(f"Invalid condition format: {condition}")


def tokenize_rule(rule_string):
    rule_string = rule_string.replace('(', ' ( ').replace(')', ' ) ')
    rule_string = rule_string.replace('AND', ' AND ').replace('OR', ' OR ')
    return rule_string.split()


def parse_expression(tokens):
    operators = {'AND': 1, 'OR': 0}
    stack = []
    output = []

    while tokens:
        token = tokens.pop(0)
        if token == '(':
            output.append(parse_expression(tokens))
        elif token == ')':
            break
        elif token in ['AND', 'OR']:
            while stack and stack[-1] in operators and operators[token] <= operators[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
        else:
            if len(tokens) > 0 and tokens[0] in ['>', '<', '=']:
                operator = tokens.pop(0)
                condition = f"{token} {operator} {tokens.pop(0)}"
                output.append(Node('operand', value=condition))
            else:
                output.append(Node('operand', value=token))
    while stack:
        output.append(stack.pop())
    return build_ast(output)


def build_ast(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if isinstance(token, Node):
            stack.append(token)
        else:
            right = stack.pop()
            left = stack.pop()
            node = Node(node_type="operator", left=left, right=right, value=token)
            stack.append(node)
    return stack[0]


def eval_condition(condition, user_data):
    field, operator, value = parse_condition(condition)
    user_value = user_data.get(field)
    if user_value is None:
        return False

    try:
        if operator == '>':
            return int(user_value) > int(value)
        elif operator == '=':
            return str(user_value) == value
        elif operator == '<':
            return int(user_value) < int(value)
        return False
    except (TypeError, ValueError):
        raise ValueError(f"Invalid comparison between {user_value} and {value}")


def evaluate_rule(ast, user_data):
    if ast.type == "operand":
        return eval_condition(ast.value, user_data)
    elif ast.type == "operator":
        left_eval = evaluate_rule(ast.left, user_data)
        right_eval = evaluate_rule(ast.right, user_data)
        if ast.value == "AND":
            return left_eval and right_eval
        elif ast.value == "OR":
            return left_eval or right_eval
    return False


def validate_attributes(user_data, catalog):
    """Validates that the attributes in user_data are part of a given catalog."""
    for attr in user_data:
        if attr not in catalog:
            raise ValueError(f"Attribute '{attr}' is not in the catalog.")
    return True


# Example catalog of valid attributes
attribute_catalog = ['age', 'department', 'salary', 'experience']


def modify_ast(ast, modification_type, new_value=None, new_operator=None):
    """Recursively modifies the AST based on modification_type."""
    if modification_type == 'condition':
        ast.modify(new_value=new_value)
    elif modification_type == 'operator':
        ast.modify(new_operator=new_operator)
    if ast.left:
        modify_ast(ast.left, modification_type, new_value, new_operator)
    if ast.right:
        modify_ast(ast.right, modification_type, new_value, new_operator)
