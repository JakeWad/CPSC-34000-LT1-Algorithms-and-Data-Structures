from stack_list import Stack, Empty

def eval_expr(expression):
    """
    This function evaluates an arithmetic expression using a stack. The expression can contain digits and the operators '+' and '-'.
    The '+' and '-' operators have the same precedence, and the expression is evaluated from left to right.
 
    Parameters:
    expression (str): The arithmetic expression to evaluate. The expression can contain digits (0-9) and the operators '+' and '-'.
 
    Returns:
    int: The result of the arithmetic expression.
    """
    # Initialize stacks for numbers and operators
    num_stack = Stack()
    op_stack = Stack()
    
    # Parse the expression
    num = ''
    for char in expression:
        if char.isdigit():
            num += char
        elif char in ['+', '-']:
            # Push the accumulated number onto the number stack
            if num:
                num_stack.push(int(num))
                num = ''
            
            # Push the operator onto the operator stack
            op_stack.push(char)
    
    # Push the last accumulated number onto the number stack
    if num:
        num_stack.push(int(num))
    
    # Reverse the stacks
    rev_num_stack = Stack()
    rev_op_stack = Stack()
    while not num_stack.is_empty():
        rev_num_stack.push(num_stack.pop())
        rev_op_stack.push(op_stack.pop())
    
    # Initialize the result with the first number from the reversed number stack
    result = rev_num_stack.pop()
    
    # Perform the operations
    while not rev_op_stack.is_empty():
        operator = rev_op_stack.pop()
        num = rev_num_stack.pop()
        
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
    
    return result

if __name__ == '__main__':
    expression = "1+2-3+4-5"
    print(eval_expr(expression))  # Output: -1
