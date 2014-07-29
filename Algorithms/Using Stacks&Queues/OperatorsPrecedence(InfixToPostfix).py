__author__ = 'ada'

from Pythonds.basic.stack import Stack

def infix_to_postfix_convertor(infix_expression):
    # cream un dictionar de map-uire a levelurilor de precedence a operanzilor/operators
    priority = {}
    priority["("] = 0
    priority["+"] = 1
    priority["-"] = 1
    priority["/"] = 2
    priority["*"] = 2

    operators_stack = Stack()
    postfix_output_list = []

    # cream o lista din infix expressions string
    token_list = infix_expression.split()

    for each_token in token_list:
        if each_token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or each_token in "0123456789":
            postfix_output_list.append(each_token)
        elif each_token == "(":
            operators_stack.push(each_token)
        elif each_token == ")":
            top_token = operators_stack.pop()
            while top_token != "(":
                postfix_output_list.append(top_token)
                top_token = operators_stack.pop()
        else:
            while not operators_stack.isEmpty() and priority[operators_stack.peek()] >= priority[each_token]:
                top_token = operators_stack.pop()
                postfix_output_list.append(top_token)
            operators_stack.push(each_token)

    while not operators_stack.isEmpty:
        postfix_output_list.append(operators_stack.pop())

    return postfix_output_list


print(infix_to_postfix_convertor("A * B + C * D"))

s = Stack()
s.push(2)
print s.isEmpty()
print s.isEmpty

if not s.isEmpty():
    print "it's not empty mai!"

if not s.isEmpty:
    print "this one is not!"











