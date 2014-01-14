# gives a list of the words and their frequencies

def list_of_word_frequency2(freq_list):
    final_list = []
    position_word = 0
    for each_word in freq_list:
            position_word +=1
            new_list = []
            new_list.append(each_word)
            new_list.append(position_word)
            final_list.append(new_list) # [[1,2],[]]
    return final_list

# [[du,1], [le,2], [aux,3]] gives the frequency of a word given
# it works just for some of the words in the list, the second part of the list - ?
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

"""f = open("top10000fr.txt", "r")
french_freq_list = f.readlines()
f.close()
clear_list = []
for each in french_freq_list:
    clear_word = each[:-1]
    clear_list.append(clear_word)"""

clear_list = ["de", "du", "aux", "bi", "retro", "fix"]

print list_of_word_frequency2(clear_list)
print binary_search(list_of_word_frequency2(clear_list), "de")
