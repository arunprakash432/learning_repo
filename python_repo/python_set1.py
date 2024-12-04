# python - set
# used to store multiple items in a single variable
# unorered, unchangeable , unindexed
# written with curl brackets
# it doesn't allow duplicate values

set1 = {"apple", "banana", "cherry", "cherry"}
print(set1)
print("*******************************")

# 1 and True considered as same values
# 0 and False considered as same values
set2 = {True, 1, 2, "hi"}
print(set2)

#get the lenght of the set
print(len(set2))
set3= {1,2,3}
print(len(set3))
print(type(set3))

#set constructor
set4 =set((1,2,34,5,46))
print(set4)
print(type(set4))