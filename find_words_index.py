
def find_words_index(list_of_words, frequent_words):
    word_positions = {}
    for each_word in list_of_words:
        if each_word in frequent_words:
            word_positions[each_word] = frequent_words.index(each_word)
        else:
            word_positions[each_word] = 10000
    return word_positions


list_of_words = ['dans', 'pour']
frequent_words = ['de', 'la', 'et', 'les', 'des', 'en', 'un', 'du', 'dans', 'pour']
print find_words_index(list_of_words, frequent_words)

