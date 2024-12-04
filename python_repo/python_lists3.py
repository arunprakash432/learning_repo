# python - remove list items
# remove() method removes the specified item
# example

sample_list = ["aaa", "bbb", "ccc", "ddd"]
sample_list.remove("bbb")
print(sample_list)

# Remove the specified index
# pop() method removes the specified index
# in pop() method , if we do not specify the last item, it will removes the item in the list
sample_list.pop(0)
print(sample_list)

# del keyword also removes the specified index in the lists
del sample_list[1]
print(sample_list)

# clear() method empties the list.
# list will still remains , but it has no content.
sample_list.clear()
print(sample_list)