
# imi creeaza un dictionar cu cuvintele dintr-un text si de cate ori apar in text + lista cu cuvintele in ordinea descrescatare frecventei lor

def word_count(text, stop_words):

    words_occurrencies = {}
    list_words = []
    words_text = text.split()

    for each_word in words_text: # take each word from the list and insert it in the dictionary with the proper number value
        if each_word not in words_occurrencies:
            if len(each_word) > 2 and each_word not in stop_words:
                words_occurrencies[each_word] = 1
        else:
            words_occurrencies[each_word] += 1

    # gives a list with the keys sorted by value
    list_words = sorted(words_occurrencies, key=words_occurrencies.get, reverse=True)

    return words_occurrencies, list_words


f = open("machiavelli.txt","r")
machiavelli_text = f.read().lower() # f.read - gives a string with the text lines
machiavelli_text_alpha_only = ""
for each_char in machiavelli_text:
    if each_char.isalpha() or each_char == " " or each_char == "\n":
        machiavelli_text_alpha_only += each_char
f.close()


f = open("stop.txt", "r")
unwanted_words = f.read() # stringul unwanted words
stop_words = unwanted_words.split(',') # lista cu stop words
f.close()


words_occurrencies, list_words = word_count(machiavelli_text_alpha_only, stop_words)
print list_words
print words_occurrencies



# !!! nu pot modifica un string
# sortez cuvintele in ordinea frecventei => lista
# elimin punctuatia/ din text string
# elimin articlolele












