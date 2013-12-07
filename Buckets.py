import random

def random_list(num):
	my_list = [0] * num
	for i in range(num):
		my_list[i] = random.random()
	return my_list


