# python lists - sorts
# sort() method that will sor the list alphanumerically, ascending, by default:

some_list = ["chicago", "newyork", "indiana", "losangles"]
some_list.sort()
print(some_list)

#sort the list numerically
number_list = [2,3,5,3,6,1,8,6,9]
number_list.sort()
print(number_list)

#sort descending
number_list.sort(reverse=True)
print(number_list)

#customize sort function
def myfunc(n):
    return abs(n - 70)
listtt = [22, 55, 66, 77, 88,22,]
listtt.sort(key=myfunc)
print(listtt) # this function sort numbers based on how close to the number 70 defined in the function

#case insesitive sort 
# by default , sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
list_caseins = ['a', 'A', 'b', 'B', 'c', 'C']
list_caseins.sort()
print(list_caseins)
print("______________________")
list_caseins.sort(reverse=True)
print(list_caseins)
print("__________________________")
# Reverse order
# reverse() method reverses the current sorting order of the elements.
list_reverse = [1, 2, 3, 44, 55, 66, 22, 11, 1]
list_reverse.reverse()
print(list_reverse) #reverse the order of the elements
