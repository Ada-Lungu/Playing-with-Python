__author__ = 'ada'

# the binary tree will be represented by a list
# the top of the tree and the parents have to be smaller than their children

class binary_heap_implement():
    def__init__(self):
        self.heap_list = [0]
        self.current_size = 0

# inserting an item in the heap: the elem is inserted at the end of the list - it has to be higher value than the parent
# ==> compared to its parent until it will no longer be bigger than the parent value == percUp methd

#
def perc_up(self, index_of_elem):
    while index_of_elem >= 0:
        if self.heap_list[index_of_elem] > self.heap_list[index_of_elem // 2]:
            replacer = self.heap_list[index_of_elem // 2]
            self.heap_list[index_of_elem // 2] = self.heap_list[index_of_elem]
            self.heap_list = replacer[index_of_elem]
    index_of_elem = index_of_elem //2


def insert(self, new_item):
    self.heap_list.append(new_item)
    self.current_size +=1
    self.perc_up(self.current_size)

def perc_down(self, indx):
    while (indx)










