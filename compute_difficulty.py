
"""english_difficulties = {}
english_difficulties ['Oh'] = 1
english_difficulties ['Romeo'] = 1
english_difficulties ['wherefore'] = 20
english_difficulties ['art'] = 20"""


# this function takes a text, and a dictionary with difficulties 
# of individual words. then computes a number which is the sum 
# of all the difficulties of the individual words. when a word 
# is not in the word_difficulties dictionary you should assign 
# it a difficulty of 21. 
# If a word appears multiple times, you should consider it only once.


 # STEPS: search each word from text in word_diff dict, extract the value associated with it ==> Checking if there is a key inside a dict: dict.has_key("key-name")
    # if the word does not exist==> 21 value
    # calculate the sum of all the values
    # return the total value


"""for each_word in words_text:
        if each_word in word_difficulties:
            sum_difficulties += word_difficulties[each_word]

for each_word in text:
        if each_word in word_difficulties.keys():
            sum_difficulties += word_difficulties[each_word]"""



def compute_difficulty(text, word_difficulties):
    import re
    sum_difficulties = 0
    words_text = re.findall(r"[\w']+", text)

    for each_word in words_text:
        if word_difficulties.has_key(each_word):
            sum_difficulties += word_difficulties[each_word]
        else:
            sum_difficulties+=21

    return words_text, sum_difficulties

text = "Deci cum, ce sa mai spunem oare acum?"
word_difficulties= {"ce":1, "spunem":5, "oare":10, "sa":13, "acum":12, "mai":7,}

print compute_difficulty(text, word_difficulties)



# Examples that should not throw assertion failures when the function 
# is implemented
"""assert (compute_difficulty("Oh Romeo, Romeo! wherefore art thou Romeo?",
	english_difficulties) == 53)

assert (compute_difficulty("Oh, oh, oh!", english_difficulties) == 1)"""