class phone():
    storage="256GB "
    def __init__(self,brand,price,chargertype):
        self.brand = brand
        self.price = price
        self.chargertype = chargertype
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("Chargertype: ",self.chargertype)
        print("Storage: ",self.storage)

phone.storage = "100Gb"
samsung=phone("Samsung","10k","Type-c")
samsung.display()

redmi=phone("Redmi", "20k", "Type-B")
redmi.display()