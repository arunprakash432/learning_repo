# PYTHON LISTS(ARRAYS)
# List are used to store multiple items in single variable.
# There are 4 built-in collection data types in python used to store collection of data.
# 1. List
# 2. Set
# 3. Tuple
# 4. Dictionary  with all different quality and usage.
# List are created with square brackets.
# example

list1 = ["a", "b", "c", "d"]
print("The first four English Alphabets are", list1)

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, first index value is [0], second index value is [1], and goes on etc....

# List Length
# To determine how many items a list has, use len() function

print(len(list1))

# List items - Data types
# it can be of any data type: str, int, boolean
listofall = [True, False, "male1", "female2", 23, 34]
print(listofall)

# Data type
print(type(listofall))

# The list constructor
# It is also possible to create with list() constructor when creatiing a new list.
sample_list = list(("apple", "samsung", "redmi"))
print(sample_list)