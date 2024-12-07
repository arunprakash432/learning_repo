class laptop:
    def __init__(self):
        self.ram = ""
        self.proc = ""
    def display(self):
        print("Ram: ", self.ram)
        print("Processor: ", self.proc)

hp = laptop()

hp.ram = "15gb "
hp.proc = "i5 "
hp.display()

dell = laptop()
dell.ram = "20gb "
dell.proc = "i6 "
dell.display()
