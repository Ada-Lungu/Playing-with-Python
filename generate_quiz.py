
def generate_quiz(text, word):

    list_text_up_to_word = []
    list_text_after_word = []
    list_of_text = text.split() 
    missing_word = ""

    for i in range(0, list_of_text.index(word)):
        list_text_up_to_word.append(list_of_text[i])
    text_up_to_word = ' '.join(list_text_up_to_word)

    for j in range(list_of_text.index(word)+1, len(list_of_text)):
        list_text_after_word.append(list_of_text[j])
    text_after_word = ' '.join(list_text_after_word)

    for i in range(0, len(word)):
        missing_word += "."

    return text_up_to_word + ' ' + missing_word + ' ' + text_after_word


text = "Mihai Eminescu este al 7-lea dintre cei 11 copii ai caminarului Gheorghe Eminovici."
word = "7-lea"

print generate_quiz(text, word)







