import random
import math

def random_list_with_ints(num):
	lst = random_list(num)
	new_list = [0] * num
	for i in range(num):
		new_list [i] = math.floor(lst[i] * 100)
	return new_list	
		

def random_list(num):
	my_list = [0] * num
	for i in range(num):
		my_list[i] = random.random()
	return my_list

print random_list_with_ints(8)


