# python scope
# a variable is only available from inside the region it is created

# local scope

def myfunc():
    x = 300
    print(x)

myfunc()

# function inside function
def myfunc1():
    x = 500
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc1()

# global scope

y = 100
def myfunc2():
    print(y)
myfunc2()

# global keyword

z = 1000
def myfunc3():
    global z 
    z = 2000
    print(z)
myfunc3()
print(z)

# nonlocal keyword
# is used to work with variables inside nested functions.
# makes the variable belong to the outer function

def myfunc4():
    zz = "arun"
    def myfunc5():
        nonlocal zz
        zz = "varun"
    myfunc5()
    return zz
print(myfunc4())
