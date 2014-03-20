
# reading a file and counting each word how many times appears in the context

def word_count(text):

    words_text = text.split() # lista cu cuvinte din text [ce, sa, mai, zicem, ce, sa,]
    words_occurancies = {}

    for i in range(0, len(words_text)-1):
        for j in range(i+1, len(words_text)):
            word_counter=1
            if words_text[i] not in words_occurancies:
                if words_text[i] == words_text[j]:
                    word_counter+=1
                    words_occurancies[words_text[i]] = word_counter
                else:
                    words_occurancies[words_text[i]] = word_counter
            else:
                continue

    return words_occurancies

"""if words_text[len(words_text)] not in dict_words_already_found:
dict_words_already_found(words_text[len(words_text)]) = 1
else:
dict_words_already_found(words_text[len(words_text)]) = word_counter + 1"""


file_text= "Ce sa mai ce sa zicem ce sa mai povestim ce cum sa judecam"
print word_count(file_text)

# lipseste ultimul cuvant: judecam



#Varianta 2
#parcurg doar o data textul si pun in dictionar

def word_count2(text):

    words_text = text.split()
    words_occurrencies = {}

    for each_word in words_text: # take each word from the list and insert it in the dictionary with the proper number value
        if each_word not in words_occurrencies:
            if len(each_word) > 2: # (or) if each_word != "or" "and":
                words_occurrencies[each_word] = 1
        else:
            words_occurrencies[each_word] += 1
    return words_occurrencies

"""f = open("machiavelli.txt","r")
machiavelli_text = f.readlines() # gives a list with the text lines
f.close()
print word_count2(machiavelli_text
"""


file_text= "Ce sa mai ce sa zicem ce sa mai povestim ce cum sa judecam"
print word_count2(file_text)














