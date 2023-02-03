fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

fruits = ["aplle", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "b" in x]

print(newlist)

oldlist = [x for x in fruits if x != "apple"]
print(oldlist)

newlist = [x for x in range(10)]
print(newlist)

oldlist = [x for x in range(10) if x < 5]
print(oldlist)

upper = [[x.upper() for x in fruits]]
print(upper)

upper = ['hello' for x in fruits]
print(upper)

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)