# python arrays
# python does not have built-in support for arrays,
# but python lists can be used instead.

# Arrays are used to store multiple values in one single variable.
cars = ["bmw", "audi", "rangerover", "thar"]
x = len(cars)
print(cars, x)
cars[0] = "maruti"
print(cars, x)

for y in cars:
    print(y)

# pop() method is used to remove an element of the array.
cars.pop(1)
print(cars, x)
# remove() method is also used to remove an element of the array
cars.remove("thar")
print(cars)