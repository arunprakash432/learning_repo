# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent Class
# Parent class is the class being inherited from, also called base class.
# Child Class
# Child class is the class that inherits from another class, also called derived class.

# create a parent class.
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class student(person): # Child class
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = student("Arun", "Prakash")
x.printname()

# super() function
# that will make the child class inherit all the methods and properties from its parent:
