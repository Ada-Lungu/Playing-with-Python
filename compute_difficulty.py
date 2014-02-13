
english_difficulties = {}
english_difficulties ['Oh'] = 1
english_difficulties ['Romeo'] = 1
english_difficulties ['wherefore'] = 20
english_difficulties ['art'] = 20


# this function takes a text, and a dictionary with difficulties 
# of individual words. then computes a number which is the sum 
# of all the difficulties of the individual words. when a word 
# is not in the word_difficulties dictionary you should assign 
# it a difficulty of 21. 
# If a word appears multiple times, you should consider it only once.
def compute_difficulty(text, word_difficulties):
	pass


# Examples that should not throw assertion failures when the function 
# is implemented
assert (compute_difficulty("Oh Romeo, Romeo! wherefore art thou Romeo?",
	english_difficulties) == 53)

assert (compute_difficulty("Oh, oh, oh!", english_difficulties) == 1)