# python functions
# function is a block of code which only runs when its called.
# you can pass data , known as parameters, into a function.
# a function can return data as a result.
# creating a function with "def" keyword

def myfunc():
    print("This is myfunction")
myfunc()

print("******************************")

# arguments.
# information can be passed into functions as arguments.
# arguments are specified after the function name, inside the parantheses.
# you can add as many arguments as you want, just separate them with comma.

def firstfunc(ttt):
    print(ttt , " x 2")

firstfunc("1")
firstfunc("2")

# the terms parameter and arguments can be used for the same thing :
# information that are passed to a function

# function expects 2 arguments , and gets 2 arguments
def twoar(one, two):
    print(one, " = ", two)
twoar("A", "B")

# Arbitrary Arguments , *args
def manyargs(*argss):
    print("Family members are : ", argss[0:3])
manyargs("arun", " varun", " prakash")

