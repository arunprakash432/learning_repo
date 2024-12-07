import python_modules as pm #module file.py

#syntax:
# module_name.function_name

pm.greeting("Varun")

a = pm.a1
b = pm.a2
c = pm.a3
print(a,b,c)

d = dir(pm)
print(d)
import platform # platform is a python built-in modules in python

x = platform.system()
print(x)

# dir() function
# it's a built-in function to list all the function names or variable names in a module.
# using dir() function

x = dir(platform)
print(x)

# from keyword
# using this we can import parts of the module
from python_modules import a1

print(a1)