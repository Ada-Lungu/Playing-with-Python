
def generate_quiz(text, word):

    list_text_up_to_word = []
    list_text_after_word = []
    list_of_text = text.split() #["","","",""] ['ce', 'sa', 'mai', 'povestim', 'ca', 'este', 'fara', 'sens.']
    missing_word = ""

    for i in range(0, list_of_text.index(word)):
        list_text_up_to_word.append(list_of_text[i])
        text_up_to_word = ''.join(list_text_up_to_word)

    for j in range(list_of_text.index(word)+1, len(list_of_text)+1):
        list_text_after_word.append(list_of_text[j])
        text_after_word = ''.join(list_text_after_word)

    for i in range(0, len(word)):
        missing_word += "."

    return list_of_text, text_up_to_word + ' ' + missing_word + text_after_word

text1 = "ce sa mai povestim ca este fara sens."
word1 = "este"

print generate_quiz(text1, word1)







