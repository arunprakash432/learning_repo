# python - access set items
# cannot access in a set by referring to an index or a key.
# but you can loop through set items using for loop, 
# or if a specified value is present in a set, by using the "in" keyword

set1 = {1, 2, 3, 4, 5}
for x in set1:
    print(x)

# check if "1 " present in the set
print(1 in set1)
# check if "5" not present in the set
print(5 not in set1)

#once set is created , you cannot change its items, but you can add new items.
