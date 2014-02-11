
# 1. textul < 42 cuvinte => return text
# 2. textul > 42 cuvinte & include cuvnatul in primele 42 => text [42]
# 3. textul > 42 cuvinte & nu include cuv in primele 42 ==> pana la cuvant


def shorten_word_context(text, given_word, max_length):
    final_text = ""
    forty_list=[]
    list_of_text = text.split() # ==> gives me a list of the words ["these", "types", ",", "the"]
    word_count = len(list_of_text)

    if word_count <= max_length:
        return text.capitalize()
    #  len(list_of_text)=10
    for i in range(0,max_length):
        forty_list.append(list_of_text[i]) # lista cu primele 42 cuvinte
    string_forty_list = ' '.join(forty_list) # string cu primele 42 cuv

    if list_of_text.index(given_word) <= max_length:
        final_text = final_text + string_forty_list
        return final_text.capitalize()

    else:
        for i in range(max_length + 1,  list_of_text.index(given_word) + 1):
            forty_list.append(list_of_text[i])
            string_forty_list = ' '.join(forty_list)
        final_text = final_text + string_forty_list
        return final_text.capitalize()

text_1 = "once one is at level b1 he is already brave enough to start reading texts in the target language. however, he will still encounter word that he does not understand quite often. thus, he theoretically could start reading literature on the target language, but practically, it is so annoying to constantly search for words will be so boring as to completely repel him. "
word_1 = "encounter"

text_3 = "once one is at level b1 he is already brave enough to start reading texts in the target language. however, he will still encounter word that he does not understand quite often. thus, he theoretically could start reading literature on the target language, but practically, it is so annoying to constantly search for words will be so boring as to completely repel him. "
word_3 = "boring"

text_2 = "we are together all in this one, no matter what they say;)"
word_2 = "what"

max_lenght = 42

print shorten_word_context(text_1, word_1, max_lenght)
print shorten_word_context(text_3, word_3, max_lenght)
print shorten_word_context(text_2, word_2, max_lenght)

mircea_text = ""
for i in range(0,60):
    mircea_text += "w"+str(i)+" "
print "\nmircea's test 1... searching for w3"
print shorten_word_context((mircea_text, "w3")
print "\nmircea's test 3... searching for w52"
print shorten_word_context(mircea_text, "w52")


