# python - access list items.
# List items are indexed and can access by them referring to the index number.
# first item has index 0
# second item has index 1 and goes on to the final item.

list1 = ["car", "bus", "bike", "flight", "train" ]
print(list1[3]) # it will print 4th item on the list1

# Negative indexing.
# it means indexing starts from end
# -1 , -2, ...
print(list1[-3])

# Range of Indexes
# specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

print(list1[2:4]) # while it prints, it includes index 2, excludes 4.
print(list1[:4])
print(list1[:5])
print(list1[-1:-3])

# check the items is present in list
if "car" in list1:
    print("car is present in list")
else:
    print("it is not present in list")