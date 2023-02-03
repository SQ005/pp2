thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#for x in thisdict:
  #print(thisdict[x])

#for x in thisdict.values():
  #print(x)

#for x in thisdict.keys():
    #print(x)

for x, y in thisdict.items():
    print(x,y)

mydict = thisdict.copy()
print(mydict)

yourdict = dict(thisdict)
print(yourdict)
