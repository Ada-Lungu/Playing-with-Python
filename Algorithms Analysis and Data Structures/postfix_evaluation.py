__author__ = 'ada'

from pythonds.basic.stack import Stack

def postfix_evaluation(postfix_expression):
    # we put all the operands in a stack until we come across an operator
    operand_stack = Stack()
    token_list = postfix_expression.string()

    for each_token in token_list:
        if each_token in "0123456789":
            operand_stack.push(int(each_token)) # in list the numbers are actually strings, into stacks can be as integers or strings ?
        else:
            first_operand = operand_stack.pop()
            second_operand = operand_stack.pop()
            resulted_operand = doMath(each_token, first_operand, second_operand)
            operand_stack.push(resulted_operand)
    return operand_stack.pop()

def doMath(operator, operand1, operand2):
    if operator == "*":
        result = operand1 * operand2
    elif operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "/":
        result = operand1 / operand2

    return result

print postfix_evaluation("7 8 + 3 2 + /")







