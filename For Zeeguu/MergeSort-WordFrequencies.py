class WordFrequency():
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

# takes two sorted lists
# must return a new sorted list
def merge_lists(left_list, right_list):
    i = 0
    j = 0
    my_sorted_list = []
    while i < len(left_list) or j < len(right_list):

        # we are finished with left array
        if (i == len(left_list)):
            # copy everything that remains from the right_array
            my_sorted_list.append(right_list[j])
            j+=1
        elif (j == len(right_list)):
            #copy everything that remains from left array
            my_sorted_list.append(left_list[i])
            i+=1
        elif (left_list[i].word <= right_list[j].word):   # lista[index] = elementul (de pe index)
            my_sorted_list.append(left_list[i])
            i += 1
        elif left_list[i].word > right_list[j]:
            my_sorted_list.append(right_list[j])
            j += 1
    return my_sorted_list


# always returns an array which is sorted...
def split_and_merge_list(my_list):
    middle_list = len(my_list) // 2 # the index of the mid elem
    left_list = []
    right_list = []

    if len(my_list) < 2: # an array with one element, is ... sorted!
        return my_list # asta nu inteleg - ce returneaza
    else:
        #split
        for i in range(0, middle_list):
            left_list.append(my_list[i]) # creeaza stanga
        for i in range(middle_list, len(my_list)):
            right_list.append(my_list[i]) # creeaza dreapta

    left_sorted_list = split_and_merge_list(left_list)
    right_sorted_list = split_and_merge_list(right_list)
    #merge...
    return merge_lists(left_sorted_list, right_sorted_list)

"""w1 = WordFrequency('de', 1)
w2 = WordFrequency('le', 2)
w3 = WordFrequency('pour', 3)
w4 = WordFrequency('jour', 4)

lista_cuvinte = [w1, w2, w3, w4]"""


f = open("../top10000fr.txt", "r")
french_list = f.readlines()
f.close
word_freq_list = []

for each_line in french_list: # each line contains [word, freq]
    word_and_freq = WordFrequency(each_line[0], each_line[1])
    word_freq_list.append(word_and_freq)


print split_and_merge_list(word_freq_list)


