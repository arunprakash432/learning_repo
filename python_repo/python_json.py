# python json
# json is a syntax for storing and exchanging data
# json is text, written with javascript object notation

# python has a builtin package called json
# which can be used to work with json data

import json

# convert json to python
x = '{"name":"arun ", "age":"22", "city":"dpi"}'
y=json.loads(x) # for using the json strings json.loads()
print(y)

# convert python to json
z = {
    "name": "arun",
    "age" : "22",
    "city": "Dpi"
}
zz = json.dumps(z) # convert from python to json using json.dumps()
print(zz)