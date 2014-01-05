
top1000frtxt=open("top10000fr.txt", "r")
all_words = top1000frtxt.readlines() #slow - lista cuvintelor frecventa cu /n
all_words_without_space = []
for each_word in all_words:
    each_word_without_space = each_word[:-1]
    all_words_without_space.append(each_word_without_space)


def importance_range(the_word, frequency_list):
    position = frequency_list.index(the_word)
    return (position // 1500) + 1

print importance_range("jambes", all_words_without_space)


# alte variante de rezolvare

def importance_range2(the_word, frequency_list):
    position = frequency_list.index(the_word)
    if position // 1500 == 0:
        return 1
    elif position // 1500 == 1:
        return 2
    elif position // 1500 == 2:
        return 3
    elif position // 1500 == 3:
        return 4
    elif position // 1500 == 4:
        return 5
    elif position // 1500 == 5:
        return 6
    else:
        return 7
print importance_range2("jambes", all_words_without_space)


