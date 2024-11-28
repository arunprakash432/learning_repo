# LIST COMPREHENSION
# list comprehension offers the shorter syntax.
# when you want to create a new list based on the values of existing list.
# THE SYNTAX
# newlist = [expression for item in iterable if condition == True]
samp11 = list(range(11, 30))
print(samp11)
list11 = [i for i in samp11 if i%2==0] #even number
print(list11)
print("---------------------------------------")
list22 = [j for j in samp11 if j%2==1] #odd number
print(list22)
print(len(list22))

#strings
samp22 = ["aaa", "aa", "a", "bbb", "bb", "b"]
print(len(samp22))
print("*********************************")
#only starting with a
aonly = [s for s in samp22 if "a" in s]
print(aonly)
print("no of a contains samp, ", len(aonly))
#starting with b 
bonly = [d for d in samp22 if "b" in d]
print(bonly)
print("the number b contains is , ", len(bonly))

# change letter to uppercase
upperee = [h.upper() for h in samp22]
print(upperee)
print("_________________________________")
# retur c instead of a
ccc = [g if g != "a" else "c" for g in samp22]
print(ccc)