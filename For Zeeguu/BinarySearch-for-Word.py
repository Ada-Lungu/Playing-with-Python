"""class FreqList: # we create a class and a new type BS

    freq_list = BinarySearch() # cream un obiect de tip Binary Search (process named instantiation)==> objects or instances of class BS
    # a function like BinarySearch() that creates a new object is a Constructor
    freq_list.left = 0  # left is an attribute to object BS
    freq_list.right = len(freq_list)-1
    freq_list.middle = len(freq_list)//2"""


def __init__(self, left, right, middle):

    self.left = left # left is an attribute to object BS
    self.right = right
    freq_list.middle = len(freq_list)//2

def binary_search(freq_list, the_word):

    left = 0
    right = len(freq_list)-1
    middle = len(freq_list)//2
    counter_searches = 0

    while left<=right:
        if the_word == freq_list[middle]:
            return middle, counter_searches
        elif the_word < freq_list[middle]:
            counter_searches +=1
            right = middle-1
            middle = (left + right) // 2
        elif the_word > freq_list[middle]:
            counter_searches +=1
            left = middle+1
            middle = (left + right) // 2
    return -1, counter_searches


clear_list=[]
f = open("../top10000fr.txt", "r")
french_freq_words = f.readlines()
f.close()

for each in french_freq_words:
    clear_word = each[:-1]
    clear_list.append(clear_word)

sorted_list = sorted(clear_list) # sorted alphabetically
print binary_search(sorted_list, 'aux')



