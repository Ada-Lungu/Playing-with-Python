
def factorial(n):  # n! = n(n-1)! ; 0! = 1
    if n == 0:
        return 1
    else:
        factorial = n * factorial(n-1)  # or return  n * factorial(n-1)
    return factorial

# this is a Recursive Function = calling a function inside itself

def fibonacci(n): # fibonacci(n) = fibonacci (n-1) + fibonacci (n-2)
    if n == 0 or  n == 1:
        fibonnaci = 1
    else:
        fibonnaci = fibonnaci(n-1) + fibonnaci(n-2)
        assert isinstance(fibonnaci, object)

    return fibonnaci