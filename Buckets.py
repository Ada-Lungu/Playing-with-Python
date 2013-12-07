import random
import math

def random_list_with_ints(num):
	lst = random_list(num)
	new_list = [0] * num
	for i in range(num):
		new_list [i] = math.floor(lst[i] * 100)
	return new_list	
		

# imi da o lista cu num numere random
def random_list(num):
	my_list = [0] * num
	for i in range(num):
		my_list[i] = random.random()
	return my_list

# doresc sa impart lista in mai multe buckets num_buckets, lista mea are valori intre  0.0 - 1.0
#==> width-ul fiecarei liste in aflu 1.0/num_buck

# calculez cate elemente sunt in fiecare bucket


def count_elem_in_buck(my_list, low, high):
	count = 0
	for num in my_list:
		if  low < num< high:
			count += 1
	return count


def print_range_buck(num_buckets):

	width_bucket = 1.0/num_buckets

	for i in range(num_buckets):
		low = i * width_bucket
		high = low + width_bucket
		print "range from", low, "to", high

def count_elem_in_buckets(my_list, num_buckets):

	width_bucket = 1.0/num_buckets
	elem_each_buck = [0] * num_buckets

	for i in range(num_buckets):
		low = i * width_bucket
		high = low + width_bucket
		elem_each_buck[i] = count_elem_in_buck( my_list, low, high)
	return elem_each_buck


print_range_buck(6) 
print count_elem_in_buckets(random_list(100), 6 )


