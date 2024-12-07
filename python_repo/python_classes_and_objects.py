class goa:
    name = ""
    drink=""
    def party(self):
        print("Let\'s party ....")
    def beach(self):
        print("Watching the beaches ....")

ramesh = goa()
suresh = goa()

ramesh.name="Ramesh"
ramesh.drink="Yes"
suresh.name="Suresh"
suresh.drink="No"
print(ramesh.name)
print("drink ",ramesh.drink)
print(suresh.name)
print("drink: ", suresh.drink)

ramesh.party()
suresh.beach()

class laptop:
    price=""
    processor=""
    ram=""
    
hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price="10k "
hp.processor="intel i5 "
hp.ram="16gb "

print("Specifications of HP Laptop: \n",hp.price,hp.processor,hp.ram)

dell.price="20k "
dell.processor="intel i6 "
dell.ram="20gb "

print("\n*****************")
print("Specifications of Dell Laptop: \n",dell.price,dell.processor,dell.ram)
print("\n*********************")
lenovo.price="30k "
lenovo.processor="intel i7 "
lenovo.ram="25gb "
print("Specifications of Lenovo Laptop: \n",lenovo.price,lenovo.processor,lenovo.ram)
