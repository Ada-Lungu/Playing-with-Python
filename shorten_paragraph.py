
# 1. textul < 42 cuvinte => return text
# 2. textul > 42 cuvinte & include cuvnatul in primele 42 => text [42]
# 3. textul > 42 cuvinte & nu include cuv in primele 42 ==> pana la cuvant


def extract_shorter_relevant_example(text, my_word):
    final_text = ""
    forty_list=[]
    list_words = text.split() # ==> gives me a list of the words ["these", "types", ",", "the"]
    nr_words = len(list_words)
    index_my_word = list_words.index(my_word)
    string_list_words = ' '.join(list_words)

    if nr_words <= 42:
        final_text = final_text + string_list_words
        list_final_text = final_text.split()
        return nr_words, len(list_final_text), final_text
    #  len(list_words)=10
    for i in range(0,43):
        forty_list.append(list_words[i]) # lista cu primele 42 cuvinte
    string_forty_list = ' '.join(forty_list) # string cu primele 42 cuv

    if index_my_word <= 42:
        final_text = final_text + string_forty_list
        list_final_text = final_text.split()
        return nr_words, len(list_final_text), final_text

    else:
        for i in range(43, index_my_word+1):
            forty_list.append(list_words[i])
            string_forty_list = ' '.join(forty_list)
        final_text = final_text + string_forty_list
        list_final_text = final_text.split()
        return nr_words, len(list_final_text), final_text

text_1 = "once one is at level b1 he is already brave enough to start reading texts in the target language. however, he will still encounter word that he does not understand quite often. thus, he theoretically could start reading literature on the target language, but practically, it is so annoying to constantly search for words will be so boring as to completely repel him. "
word_1 = "encounter"

text_3 = "once one is at level b1 he is already brave enough to start reading texts in the target language. however, he will still encounter word that he does not understand quite often. thus, he theoretically could start reading literature on the target language, but practically, it is so annoying to constantly search for words will be so boring as to completely repel him. "
word_3 = "boring"

text_2 = "we are together all in this one, no matter what they say;)"
word_2 = "what"

print extract_shorter_relevant_example(text_1, word_1)
print extract_shorter_relevant_example(text_3, word_3)
print extract_shorter_relevant_example(text_2, word_2)

mircea_text = ""
for i in range(0,60):
    mircea_text += "w"+str(i)+" "
print "\nmircea's test 1... searching for w3"
print extract_shorter_relevant_example(mircea_text, "w3")
print "\nmircea's test 3... searching for w52"
print extract_shorter_relevant_example(mircea_text, "w52")


