__author__ = 'ada'

from test import testEqual
from Pythonds.basic.stack import Stack

def revstring(original_string):

    myStack = Stack()
    for each_char in original_string:
        myStack.push(each_char) #=> creeaza a stack with the letters in the original original_string
    # create the reversed string by taking the element from the top of the stack(last inserted, first taken) and insering it into the string

    reversed_string = ""
    while not myStack.isEmpty():
        reversed_string += myStack.pop()

    return reversed_string

testEqual(revstring("caracao"), "oacarac")



