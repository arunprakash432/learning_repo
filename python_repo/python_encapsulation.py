# python encapsulation

class company():
    def __init__(self):
        self.__companyname = "Software Company"
    def display(self):
        print(self.__companyname)

c1 = company()
c1.__companyname = "hello company"
c1.display()
# _(single underscore) = privated and public protected
# __(double underscore) = can't acces outside the class

