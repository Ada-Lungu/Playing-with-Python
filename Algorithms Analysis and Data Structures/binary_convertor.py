__author__ = 'ada'

from pythonds.basic.stack import Stack
def binary_convertor(decimal_num):

    rest_stack = Stack()

    while decimal_num > 0:
        rest = decimal_num % 2
        rest_stack.push(rest)
        decimal_num = decimal_num // 2

    binary_str = " "
    while not rest_stack.isEmpty():
        binary_str += str(rest_stack.pop())

    return binary_str

print binary_convertor(354)


