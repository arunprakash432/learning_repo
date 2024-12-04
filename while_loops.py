# PYTHON LOOPS
# python has two primitive loops
# 1. while loops
# 2. for loops

# The while loop
# excute a set of statements as long as a condition is true

i = 1 # indexing variable, which is set to be 1
while i <= 6:
    print(i)
    i += 1

# "break" statement
# with the break statement we can stop the loop even if the while condition is true:
print("************************************")
j = 2
while j < 20:
    print(j)
    if j == 10:
        break
    j += 1

# "continue" statement
# with continue statement we can stop the current iteration, and continue with the next:

s = 0
while s < 8:
    s += 1
    if s == 4:
        continue # number 4 gonna missing in the result
    print(s)
else:
    print("after 8")