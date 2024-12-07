class laptop():
    chargertype="Type-c"
    
    def __init__(self): #instance method
        self.brand=""
        self.price=10
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)

    @classmethod #class method
    def ram(cls):
        cls.ram="20gb "
        print("It has ram")

    @staticmethod #static method
    def info():
        print("It\'s is a good mobile....")

hp=laptop()
hp.setprice("20000")
hp.getprice()
laptop.ram()
hp.info()