
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

    words_occurrencies = {}
    list_words = []
    words_text = text.split()

    for each_word in words_text: # take each word from the list and insert it in the dictionary with the proper number value
        if each_word not in words_occurrencies:
            if len(each_word) > 2: # (or) if each_word != "or" "and":
                words_occurrencies[each_word] = 1
        else:
            words_occurrencies[each_word] += 1

    # verific value al cuvantului din lista in dict, si il pun in lista pe pozitia respectiva

    """for each_pair in words_occurrencies:
        list_values.insert(words_occurrencies[each_word],key)"""


    for each_word in sorted(words_occurrencies, key=words_occurrencies.get, reverse=True):
        list_words.append(each_word)

    return words_occurrencies, list_words

f = open("machiavelli.txt","r")
machiavelli_text = f.read() # f.read - gives a string with the text lines
words_machiavelli_text = machiavelli_text.split()
clear_text = ""
for each_char in words_machiavelli_text:
    if each_char.isalpha():
        clear_text += each_char
f.close()

print word_count2(clear_text)




# !!! nu pot modifica un string

# sortez cuvintele in ordinea frecventei => lista

# elimin punctuatia/ din text string
# elimin articlolele












