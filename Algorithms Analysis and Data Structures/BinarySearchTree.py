__author__ = 'ada'


class Binary_Search_Tree(self, size):


class TreeNode:
    def __init__(self,key, val, left, right, parent):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

# Methods: has_right/left_child / is_right/left_child /
""" What we want to know about a node:
has children left/right
is left/right child
is the root/the leaf
has any cildren/both children?"""

def has_left_child(self):
    return self.left_child

def has_right_child(self):
    return self.right_child

def is_right_child(self):
    return self.parent and self.parent.right_child == self

def is_left_child(self):
    return self.parent and self.parent.left_child == self

def is_root(self):
    return not self.parent # True if it's not parent/ else if it is parent False

def is_leaf(self):
    return not (self.left_child and self.right_child)

def has_any_children(self):
    return self.right_child or self.left_child

def has_both_children(self):
    return self.right_child and self.left_child

# or/and ==> boolean expression? returns True or False



# this method helps building the binary search tree + checks to see of the tree already has a root, if not it will create a TreeNode / else==> uses _put method
def put(self,key, val):
    if self.root:
        self._put(key, val, self.root)
    else:
        self.root = TreeNode(key, val)
        self.size += 1

# compare the new key with the key in current node ==> if smaller to the left, if greater to the right
# create the new node woth TreeNode
def _put(self, key, val):
    if key < currentNode.key: # WHERE THIS currentNode COMES FROM?
       if currentNode.has_left_child():
           currentNode._put(key, val, currentNode.left_child) # if the current node has a left child => recursive/ search if left child has a left child...
       else:
           currentNode.left_child == TreeNode(key, val, parent=currentNode) #? why need to mention this, parent current node e subinteles, nu?

    else:
        if currentNode.has_right_child():
            currentNode._put(key, val, currentNode.right_child)
        else:
            currentNode.right_child == TreeNode(key, val, parent=currentNode)


# GET method, gives the value of a key

# DID NOT GET "GET" method
def get(self,key):
    if self.root:
        res = self._get(key,self.root)
        if res:
               return res.payload
        else:
               return None
    else:
        return None

def _get(self, key, currentNode):
    if not currentNode:
        return None # ???
    if currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        if currentNode.has_left_child():
            self._get(key,currentNode.left_child)
    else:
        if currentNode.has_right_child():
            self._get(key, currentNode.right_child)


# DELETE method, finds the node that has the key and removes it

def del(self, key):
    if self.size > 1:
        node_to_remove = self._get(key, self.root) # verifica care nod are key = key
        if node_to_remove: # cand e gasit node-ul respectiv
            self.remove(node_to_remove) # removes the item, without returning anything
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
    elif self.size == 1 and self.root.key == key:
        self.root = None
        self.size = 0
    else:
        raise KeyError('There is no tree')

# in deleting the node with the key, we have 3 scenarious

# 1. the node has no children=> leaf ==> then we have to delete the reference in its parent as being its child

    if currentNode.is_leaf():
        if currentNode.is_left_child: # if currentNode == currentNode.parent.left_child:
            currentNode.parent.left_child = None
        else:
            currentNode.parent.right_child = None


















































