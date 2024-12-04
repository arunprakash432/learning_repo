#python loop lists

hardwares = ["mouse", "keyboard", "ram", "rom", "cd"]
for x in hardwares:
    print(x)

# loop through the index numbers
# loop through the list items by referring to their index number.
# use range() and len() functions to create a suitable iterable.
print(len(hardwares))
for i in range(len(hardwares)):
    print(hardwares[i])

# using the while loop
# using len() function to determine the length of the list
print("--------------------------")
j = 0
while j < len(hardwares):
    print(hardwares[j])
    j = j + 1
print("----------------------------")
# loop using list comprehension
numbers12 = list(range(1, 10))
[print(y) for y in numbers12]