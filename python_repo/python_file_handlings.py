# Python file handlings
# to open a file

f = open("sample.txt", "w") # 'r' to read 'w' to write

# to read a file
# content = f.read()
# print(content)

# to write a file
f.write("pineapple")

# f.close() # to close a file, after close we can't do operations like read and write
f.close()

# f = open("sample.txt", "r+")
# f.write("hello \n hi")
# content = f.read()
# print(content)


f = open("sample.txt", "a+") # append method
f.write("\nwhat \n why")
f.close()
f = open("sample.txt", "r")
print(f.read())
f.close()

# to print the first line of the file
f = open("sample.txt")
w = f.readline()
print(w)
f.close()