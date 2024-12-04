# python - join lists
# there are several ways to join, or concatenate, two or more lists in python
# easiest way is + operator
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 0]
list_c = list_a + list_b
print(list_c)
print("************************************")
# appending all items one by one
for x in list_b:
    list_a.append(x)

print(list_a)

# extend() method
print("************************")
list_a.extend(list_b)

print(list_a)

#python - list methods in w3schools.com