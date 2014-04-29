__author__ = 'ada'

def BinaryTree(r): # create a binary tree
    return [[r, [], []]

# insert a left node to the current root, check if there is already smth

def insert_left(root, new_branch):
    the_replaced_elem = root.pop(1) # pop(1) = left element
    if len(the_replaced_elem) > 0:
        root.insert(1, [new_branch, [the_replaced_elem],[]])
    else:
        root.insert(1, [new_branch, [], []])

def insert_right(root, new_branch):
    the_replaced_elem = root.pop(2)
    if len(the_replaced_elem) > 0:
        root.insert(2, [new_branch, [the_replaced_elem],[]])
    else:
        root.insert(2, [new_branch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root, newvalue):
    root[0] = newvalue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insert_left(r,4)
insert_left(r,5)
insert_right(r,6)
insert_right(r,7)
l = getLeftChild(r)
print(l)








