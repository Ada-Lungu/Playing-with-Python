
def generate_quiz(text, word):

    list_text_up_to_word = []
    list_text_after_word = []
    list_of_text = text.split() #["","","",""] ['ce', 'sa', 'mai', 'povestim', 'ca', 'este', 'fara', 'sens.']
    missing_word = ""

    for i in range(0, list_of_text.index(word)):
        list_text_up_to_word.append(list_of_text[i])
        text_up_to_word = ''.join(list_text_up_to_word)
    # ML: Linia precedenta ... deci tu join-ui cuvintele 
    #  fara spatziu intre ele? ... hmm.
    # ML: Linia precedenta... oare pentru fiecare cuvant trebuie 
    #  sa faci join? sau este suficient sa faci join dupa ce ai 
    #  lista calculata deja? 

    for j in range(list_of_text.index(word)+1, len(list_of_text)):
        list_text_after_word.append(list_of_text[j])
        text_after_word = ''.join(list_text_after_word)
    # ML: Same as before

    for i in range(0, len(word)):
        missing_word += "."

    # ML: aici vrei sa pui spatziu si dupa missing_word nu doar inainte, nu?
    # ML: pe langa asta, functzia trebuie sa returneze doar textul. asa am cerut... :)
    return list_of_text, text_up_to_word + ' ' + missing_word + text_after_word

text1 = "Mihai Eminescu este al 7-lea dintre cei 11 copii ai caminarului Gheorghe Eminovici."
word1 = "este"

print generate_quiz(text1, word1)







