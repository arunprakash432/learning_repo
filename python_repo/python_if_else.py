# Python Conditions and If statements
# python supports logical conditions from mathematical operations
# Equals : a == b
# Not Equals: a != b
# Less than or equal to : a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# if statement is written by using the if keyword

a = 10
b = 20
if a < b:
    print("a is smaller than b")
else:
    print("then it's not")

# Indentation
# python mostly relies on indentation to define the scope in the code, whitespaces at the beginning of the line ..
c = 22
d = 33
if c < d:
    print("just check something about indentation")
# result indentation: shows indentation error

# elif keyword
# if the previous conditions were not true, then try this condition.
e = 30
f = 40
if e > f:
    print("e is greater than f")
elif e < f:
    print("f is greater than e")

# short hand
# This technique is known as Ternary Operators or conditional expressions
# one line "if" statement
if e < f: print("e is smaller than f, one line if statement")

# one line if else statement
g = 111
h = 222
print("g is greater") if g > h else print("g is smaller")

# multiple statements in one line:
gg = 111
hh = 222
print("gg") if gg > hh else print("hh") if gg < hh else print("none")