# python inheritance
#single inheritance
class dad():
    def phone(self):
        print("Dad\'s phone: ")

class mom(dad): 
    def sweet(self):
        print("Mom\'s Sweet: ")

class son(dad): #Multiple inheritance
    def laptop(self):
        print("Son\'s Laptop: ")


arun = son()
arun.phone()
#arun.sweet()

sathya = mom()
sathya.phone()