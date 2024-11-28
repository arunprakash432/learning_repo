#python booleans
#it returns either one of the value, true or false
#it is used to check the expression , true or false

print(10>9)
print(10<9)

#When you run a condition in an if statement, python returns either True or False

a = 190
b = 399

if b > a:
    print("B is greater than a")
else:
    print("B is not greater than a")

#Evaluate values and variables
# bool() function allow you to evaluate any value, and give you True of False in return,

#evaluate a string and a number
print(bool("Hello"))
print(bool(10))

#evaluating variables
x = ""  #empty strings returns false boolean, 
y = 111
z = 0 #returns false, , any numbers returns true, except 0
print(bool(x))
print(bool(y))
print(bool(z))

#any list, tuple, set, dictionary are true , except empty ones

# some values are false
#empty values, such as (), [], {}, "", and the number 0, and the value None. False value will return False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))

#object made from a class with a __len__ function that return 0 or false:
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

#we can create a function that return boolean value:

def myFunction():
    return True

print(myFunction())

#execute code based on the boolean answer of the function

def sample_funtion():
    return False

if sample_funtion():
    print("Yes")
else:
    print("NO")

#python has many builtin function that returns boolean values , like isinstace(),
# isinstance() used to determine if an object is of a certain data type:

sss = 333
print(isinstance(sss, int))