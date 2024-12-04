# python for loops
# it is used for iterating over a sequence(list, tuple, dictionary, set , string)
# for loop can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "orange", "banana"]
for x in fruits:
    print(x)

# loop through a string:
for y in "varun":
    print(y)

# break statements
# can stop the loop before it has looped through all the items
tupleee = ("a", "b", "c", "d", "e")
for z in tupleee:
    print(z)
    if z == "d": # stops at "d"
        break

print("********************")

#continue
for a in tupleee:
    if a == "d":
        continue
    print(a)

# range() function
# loop through a set of code a specified number of items, we can use the range() function
# range() function returns the sequence of number 
# starting from 0 by default, and increaments by 1 default, and ends at a specified number.

print("#####################################")
for b in range(10): # results only from 0 to 9 , not 10
    print(b)

print("***********************")
for c in range(3, 30):
    print(c)

# it is possible to specify the increment value by adding a third parameter
print("**************************")
for d in range(0,10,2):
    print(d)
else: # else block won't execute if the loop is stopped by a break statement
    print("the range of 10 increamental by 10 is finished")

# nested loops
print("*******************************")
tabless = [k for k in range(10)]
for c in tabless:
    for v in range(0, 10, 2):
        print(c,v)