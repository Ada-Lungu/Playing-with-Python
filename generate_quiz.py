
def generate_quiz(text, word):

    words_up_to_word = []
    words_after_word = []
    text_split = text.split()
    missing_word = ""

    for i in range(0, text_split.index(word)):
        words_up_to_word.append(text_split[i])
    text_up_to_word = ' '.join(words_up_to_word)

    for j in range(text_split.index(word)+1, len(text_split)):
        words_after_word.append(text_split[j])
    text_after_word = ' '.join(words_after_word)

    for i in range(0, len(word)):
        missing_word += "."

    return text_up_to_word + ' ' + missing_word + ' ' + text_after_word


text = "Mihai Eminescu este al 7-lea dintre cei 11 copii ai caminarului Gheorghe Eminovici."
word = "7-lea"

print generate_quiz(text, word)







