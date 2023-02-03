thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)
x = thisdict.values()
print(thisdict.values())

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

y = car.values()
print(y)
car["year"] = 2020
print(y)

x = thisdict.items()
print(x)