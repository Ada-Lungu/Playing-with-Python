def word_of_index(numbers):

    correspondent_words = []

    f = open("top10000fr.txt", "r")
    french_words = f.readlines()
    f.close()

    for each_num in numbers:
        word = french_words[each_num]
        correspondent_words.append(word)
    text_words = ' '.join(correspondent_words)

    return text_words

numbers = [9100, 696,4866,35,3101,1106,20,483,574,3,1867,14,2,3905,9,64,3564,16,2552,326,12,515,2552,3480]

print word_of_index(numbers)




"""Pour decouvrir le cadeau, utilizes le following algorithm: chacque numero represent une position dans le fichier top10000fr.txt :)

9100
696
4866
35
3101
1106
20
483
574
3
1867
14
2
3905
9
64
3564
16
2552
326
12
515
2552
3480"""