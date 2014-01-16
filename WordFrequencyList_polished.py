# gives a list of the words and their frequencies: [[du,1], [le,2], [aux,3]]
def list_of_word_frequency2(freq_list):
    final_list = []
    position_word = 0
    for each_word in freq_list:
            position_word +=1
            new_list = []
            new_list.append(each_word)
            new_list.append(position_word)
            final_list.append(new_list)

    return final_list


# sorts alphabetically the created list of frequencies
def bubble_sort_alphabetically(my_list):
    not_sorted_yet = True
    while not_sorted_yet:
        not_sorted_yet = False # ==> sorted
        for i in range(0, len(my_list)-1):
            j = i + 1
            if my_list[i][0] > my_list[j][0]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                not_sorted_yet = True
    return my_list


# [[du,1], [le,2], [aux,3]] gives the frequency of a word given
def binary_search(freq_list, the_word):
    left = 0
    right = len(freq_list)-1
    middle = len(freq_list)//2
    counter_searches = 0
    while left<=right:
        if the_word == freq_list[middle][0]:
            return freq_list[middle][1], counter_searches
        elif the_word < freq_list[middle][0]:
            counter_searches +=1
            right = middle-1
            middle = (left + right) // 2
        elif the_word > freq_list[middle][0]:
            counter_searches +=1
            left = middle+1
            middle = (left + right) // 2
    return -1, counter_searches


f = open("top10000fr.txt", "r")
french_freq_list = f.readlines()
f.close()
clear_list = []
for each in french_freq_list:
    clear_word = each[:-1]
    clear_list.append(clear_word)

print list_of_word_frequency2(clear_list)
list_not_alphabet = list_of_word_frequency2(clear_list) # Cum pot eficientiza ca timp, sa nu imi calculeze inca o data cand calc timpul???
print bubble_sort_alphabetically(list_not_alphabet)
list_alphabet_sorted = bubble_sort_alphabetically(list_not_alphabet)
print binary_search(list_alphabet_sorted, "que")

import time
start = time.clock()
list_of_word_frequency2(clear_list)
end = time.clock()
print "method 1: %2gs" % (end-start)

start = time.clock()
bubble_sort_alphabetically(list_not_alphabet)
end = time.clock()
print "method 2: %2gs" % (end-start)


start = time.clock()
binary_search(list_alphabet_sorted, "que")
end = time.clock()
print "method 3: %.2gs" % (end-start)



