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


# frequency_categorize( ["amie", "monocle", "jolie"], frequent_words) =


# frequent_words
# {"Top 500":[le, de, du, ou], "Next 500":[bien, malade]}
def frequency_categorize(frequent_words):
    top_frequency = {}
    under_500 = []
    entre_500_1000 = []
    over_1000 = []

    for each_word in frequent_words:
            if frequent_words.index(each_word) < 5:
                under_500.append(each_word)
            elif 500 < frequent_words.index(each_word) < 10:
                entre_500_1000.append(each_word)
                top_frequency["500-1000"] = str(entre_500_1000)
            elif frequent_words.index(each_word) > 1000:
                over_1000.append(each_word)
                top_frequency["over 1000"] = str(over_1000)
            else:
                print "No frequency for this one."

    return top_frequency


frequent_words = ['de', 'la', 'et', 'les', 'des', 'en', 'un', 'du', 'dans', 'pour']
print frequency_categorize(frequent_words)


# the position of a word

top1000frtxt=open("../top10000fr.txt", "r")
all_words = top1000frtxt.readlines() #slow

def word_position(the_word):
    for each_word in all_words:
        just_the_word = each_word[:-1]
        if just_the_word == the_word:
            return all_words.index(each_word)


import time

start = time.clock()
for i in range(1000):
    word_position('variant')
end = time.clock()
print "method 1: %.2gs" % (end-start)


def word_position_line_by_line(the_word, file_name):
    freq_file = open(file_name, "r")
    line_nr = -1
    for line in freq_file:
        line_nr += 1
        just_the_word = line[:-1]
        if just_the_word == the_word:
            return line_nr
    freq_file.close()
    return -1

start = time.clock()
for i in range(1000):
    word_position_line_by_line('variant', 'top10000fr.txt')
end = time.clock()
print "method 2: %.2gs" % (end-start)





















