# python lambda
# a lamda function is a small anonymous function.
# a lamda function can take any number of arguments, but can only have one expression.

# syntax
# lamda arguments : expression
x = lambda a : a + 10
print(x(5))

y = lambda a, b : a + b
print(y(10, 20))

z = lambda a, b, c : a * b + c
print(z(2,2,2))

# why use lambda functions:
# lambda is much powerful inside the function

def myfunc(n, b):
    return lambda a :  a + b + n 

mydash = myfunc(10, 20)
print(mydash(5))

