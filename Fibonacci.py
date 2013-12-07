def fibonacci(num):

	if num == 0 or num == 1:
		return num
	else:
		return fibonacci(num-1) + fibonacci(num-2)


dicty = {0:0 , 1:1 }
def fibonacci_with_hints(num):

	if dicty.has_key(num):
		return dicty[num]
	else:
		dicty[num]= fibonacci_with_hints(num-1) + fibonacci_with_hints(num-2)
		return dicty[num]

print fibonacci_with_hints(60)


