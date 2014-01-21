
def binary_search (freq_list, the_word):

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
f = open("top10000fr.txt", "r")
french_freq_words = f.readlines()
f.close()

for each in french_freq_words:
    clear_word = each[:-1]
    clear_list.append(clear_word)

sorted_list = sorted(clear_list) # sorted alphabetically
print binary_search(sorted_list, 'aux')



