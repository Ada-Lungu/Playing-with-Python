__author__ = 'ada'

from Pythonds.basic.stack import Stack
from Pythonds.trees.binaryTree import BinaryTree

def build_parse_tree(math_express):
    # we need: a list with the math_express elements
    # a binary tree
    # a stack where we'll store the current parents +> put the first parent/the first current node
    # a current node variable

    math_express_list = math_express.split()
    parse_tree = BinaryTree()
    parent_stack = Stack()
    parent_stack.push(parse_tree)
    current_node = parse_tree

    for each_elem in math_express_list:
        if each_elem == "(":
            current_node.insertLeft()
            parent_stack.push(current_node)
            current_node = current_node.getLeftChild()

        elif each_elem in ['+', '-', '*', '/', ')']:
            current_node.setRootVal(each_elem)
            current_node.insertRight()
            parent_stack.push(current_node)
            current_node = current_node.getRightChild()

        elif each_elem not in ['+', '-', '*', '/', ')']:
            current_node.setRootVal(each_elem)
            parent = parent_stack.pop()
            current_node = parent

        elif each_elem == ")":
            current_node = parent_stack.pop()

        else:
            raise ValueError
    return parse_tree # ?????? how it appends all to it?


math_expression = ( ( 10 + 5 ) * 3 )
build_parse_tree(math_expression)

"""pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()  #defined and explained in the next section"""















