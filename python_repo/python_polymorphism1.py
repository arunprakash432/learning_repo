class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l = 10
        b = 20
        print(l*b)
s1 = shape()
print(s1.area())
r1 = rectangle()
r1.area()

# another example..
class person():
    def __init__(self, name):
        self.name = name

class student(person):
    def __init__(self, name,grade):
        super().__init__(name)
        self.grade = grade
    def display(self):
        print(self.name, self.grade)

s1 = student("arun", "A")
s1.display()

# vehicle example;
class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
c1 = car()
c1.start()

class employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        print(self.name, self.salary, self.department)

m1 = manager("Demo", "10k","computer" )
m1.display()

# polymorphism
# means "many forms"
# refers to methods/functions/operators with the same name that can be executed on many objects or classes
