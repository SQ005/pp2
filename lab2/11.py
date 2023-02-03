thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

mylist = ["messi", "alip", "marochkin"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1


print(" ")
mylist = ["messi", "alip", "marochkin"]
[print(x) for x in mylist]