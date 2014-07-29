__author__ = 'ada'

class BinaryTree():
    def __init__(self, root):

        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
             new_tree = BinaryTree(new_node)
             new_tree.left_child = self.left_child
             self.left_child = new_tree

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_tree = BinaryTree(new_node)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, new_val):
        self.key = new_val

    def get_root_val(self):
        return self.key
















