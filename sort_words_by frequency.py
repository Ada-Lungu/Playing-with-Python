

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


# frequent_words
# {"Top 500":[le, de, du, ou], "Next 500":[bien, malade]}

def frequency_categorize(frequent_words):
    top_frequency = {}
    under_500 = []
    entre_500_1000 = []
    over_1000 = []
    for each_word in frequent_words:
            if frequent_words.index(each_word) < 500:
                under_500.append(each_word)
                top_frequency["Top 500"] = str(under_500)
            elif 500 < frequent_words.index(each_word) < 1000:
                entre_500_1000.append(each_word)
                top_frequency["500-1000"] = str(entre_500_1000)
            else:
                over_1000.append(each_word)
                top_frequency["over 1000"] = str(over_1000)
        else:
            print "No frequency for this one."
    return top_frequency


frequent_words = ['de', 'la', 'et', 'les', 'des', 'en', 'un', 'du', 'dans', 'pour']
print frequency_categorize(frequent_words)
