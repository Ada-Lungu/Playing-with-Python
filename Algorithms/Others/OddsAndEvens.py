__author__ = 'ada'

def even_or_odd(number):
  even = "Even"
  odd = "Odd"
  if (number%2 == 0) or number == 0:
    return even
  else:
    return odd

print even_or_odd(6)
print even_or_odd(12)
print even_or_odd(7)
print even_or_odd(11)



def is_prime(n):
  #Return True if n is a prime number otherwise return False'

  counter = 0
  for i in range(1, n+1):
    if n//i == 0:
      counter +=1

  if counter > 2:
    return False
  else:
      return True

print is_prime(12)