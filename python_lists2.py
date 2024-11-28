# python - change list items
# to change the value of a specified item, refer to the index number

thislist = ["can", "man", "van", "wan"]
thislist[2] = "what" # index 2 is van , van changes into what
print(thislist)

# change a range of item values
# change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

list11 = ["apple", "banana", "cherry", "orange", "kiwi"]
list11[:3] = ["black", "white"]

print(list11)

#adding at the end of the list

list11.append("guava")
print(list11)

#insert items in the list at an specified index
list11.insert(2, "banana") #banana at index 2
print(list11)

#extend the list, or merging lists
list22 = ["carrot", "cabbage", "beans"]

list11.extend(list22)
print(list11)

#add any iterable
#you can add any iterable object (tuples, sets, dictionaries, etc..)
tuple11 = ("fan", "mixer", "griender")
list22.extend(tuple11)
print(list22)