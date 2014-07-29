__author__ = 'ada'

# for each opening break I put it in the stack, for each ending break I delete an opening from the stack
# the paranthesis are not balanced if: during the process I stumble upon an ending break, and have no opening in the stack
# 2. at the end I have left one or more openings in the stack

#balanced = if at the end the stack is empty

"""def is_paranthesis_balance_try1(paranthesis_string):

    is_balanced = True
    open_paranth_stack = Stack()
    for each_symbol in paranthesis_string:
        if each_symbol == "(":
            open_paranth_stack.push(each_symbol)
        else:
            while not open_paranth_stack.isEmpty():
                open_paranth_stack.pop()
            if open_paranth_stack.isEmpty:
                is_balanced = False"""


from Pythonds.basic.stack import stack
def is_paranthesis_balance(paranthesis_string):

    is_balanced = True
    open_paranth_stack = Stack()
    index = 0

    while index < len(paranthesis_string)-1:

        if paranthesis_string[index] == "(":
             open_paranth_stack.push(paranthesis_string[index])
        else:
            # ")" variante: 1. stack e gol=>is_balanced=False   , stergem un open b
            if open_paranth_stack.isEmpty():
                is_balanced = False
            else:
                open_paranth_stack.pop()
        index += 1

    if is_balanced and open_paranth_stack.isEmpty():
        return True
    else:
        return False

print is_paranthesis_balance("(()))")


# for all kind of paranthesis

from Pythonds.basic.stack import stack
def is_paranthesis_balance(paranthesis_string):

    is_balanced = True
    open_paranth_stack = Stack()
    index = 0

    while index < len(paranthesis_string)-1:

        if paranthesis_string[index] == "(":
             open_paranth_stack.push(paranthesis_string[index])
        else:
            # ")" variante: 1. stack e gol=>is_balanced=False   , stergem un open b
            if open_paranth_stack.isEmpty():
                is_balanced = False
            else:
                top_symbol = open_paranth_stack.pop()
                if not matches(top_symbol,str_symbol):
                    is_balanced = False
        index += 1

    if is_balanced and open_paranth_stack.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    if opens.index(open) == closes.index(close)
        return True


print is_paranthesis_balance("(()))")






