# "and" keyword
# it's a logical operator
# is used to combine conditional statements

a = 10
b = 20
c = 30
if c > b and c > a :
    print("both conditins are true")

# "or" keyword 
# it's a logical operator
# used to combine conditional statements
# atleast one of the conditions are true

if c > b or b > c:
    print("check b > c or c > b")

# "not" keyword
# it's a logical operator
# used to reverse the result of the conditional statement
if not a > b :
    print("a is not greater than b, but it shows")

# "NESTED IF "
# you can have if statements if statements, called nested if statements
x = 50
if x > 10:
    print("x is above 10")
    if x > 20:
        print("its also above 20")
    else:
        print("but not above")

# "pass" statement
# if statements can't be empty
# put pass statement to avoid getting error
y = 10
if x > y:
    pass
