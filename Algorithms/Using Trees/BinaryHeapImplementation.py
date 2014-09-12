__author__ = 'ada'

# the binary tree will be represented by a list
# the top of the tree and the parents have to be smaller than their children

class binary_heap_implement():
    def__init__(self):
        self.heap_list = [0]
        self.current_size = 0

# inserting an item in the heap: the elem is inserted at the end of the list - it has to be higher value than the parent
# ==> compared to its parent until it will no longer be bigger than the parent value == percUp method
# child on position p ==> parent on position p//2

# perc_up is a helper function for insert function
def perc_up(self, index_of_elem):
    while index_of_elem // 2 > 0:
        if self.heap_list[index_of_elem] < self.heap_list[index_of_elem//2]:
            replacer = self.heap_list[index_of_elem//2]
            self.heap_list[index_of_elem//2] = self.heap_list[index_of_elem]
            self.heap_list[index_of_elem] = replacer
        index_of_elem = index_of_elem //2


def insert(self, new_item):
    self.heap_list.append[new_item]
    self.current_size +=1
    perc_up(self.current_size)


# perc_down is the helper function for delete_min function
def perc_down(self, index_of_elem):
    while (index_of_elem * 2) <= self.current_size:
        if self.heap_list[index_of_elem] > self.heap_list[index_of_elem * 2 ] or self.heap_list[index_of_elem] > self.heap_list[((index_of_elem * 2) + 1)]:
            if self.heap_list[index_of_elem * 2] < self.heap_list[((index_of_elem * 2) + 1)]:
                replacer = self.heap_list[index_of_elem * 2]
                self.heap_list[index_of_elem * 2] = self.heap_list[index_of_elem]
                self.heap_list[index_of_elem] = replacer
            else:
                replacer = self.heap_list[((index_of_elem * 2) + 1)]
                self.heap_list[((index_of_elem * 2) + 1)] = self.heap_list[index_of_elem]
                self.heap_list[index_of_elem] = replacer
        index_of_elem = index_of_elem *2


# shorter version:

def perc_down(self, index_of_elem):
    while (index_of_elem * 2) <= self.current_size:
        min_child == self.minChild(index_of_elem) # returneaza pozitia/indexul pe care se afla min child
        if self.heap_list[index_of_elem] > self.heap_list[min_child]:
                replacer = self.heap_list[index_of_elem * 2]
                self.heap_list[index_of_elem * 2] = self.heap_list[index_of_elem]
                self.heap_list[index_of_elem] = replacer

        index_of_elem = min_child

# verifica care dintre copiii parentului de pe index of element este mai mic
def minChild(self, index_of_elem):
    if (i * 2 + 1) > self.current_size: # daca nu exista right child, the min child e left
        return index_of_elem * 2
    if self.heap_list[index_of_elem * 2] < self.heap_list[((index_of_elem * 2) + 1)]:
        return index_of_elem * 2
    else:
        return index_of_elem * 2 + 1

def delete_min(self):
    min_elem = self.heap_list[1]
    #self.heap_list.delete(min_elem) #????????? /
    #min_elem = self.heap_list.pop()
    self.heap_list[1] = self.heap_list[self.current_size]
    self.heap_list.pop()
    self.perc_down(1)
    #return self.heap_list
    return min_elem # ??why not returning the list?





















