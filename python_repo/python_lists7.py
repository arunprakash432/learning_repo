# python list copying
# use copy() method to copy a list
some_list = ["tv", "fan", "chair", "table"]
another_list = some_list.copy()
print(another_list)

# use the list() method
# another way to make a copy is to use the built-in method list()
# list() method

print("--------------------------------")
list_a = [2, 3, 4, 5, 5]
list_b = list(list_a)
print(list_b)
print("-----------------------------")
# use the slice operator
# copy the list using : (slice) operator

list_c = [3, 4, 2, 1, 5, 6]
list_d = list_c[:]
print(list_d)
