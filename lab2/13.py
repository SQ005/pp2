thislist = ["apple", "banana", "cherry", "orange", "mango"]
thislist.sort()
print(thislist)

thislist = [100, 23, 50, 82, 65]
thislist.sort()
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "mango"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 23, 50, 82, 65]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["apple", "orange", "banana"]
mylist = thislist.copy()
print(mylist)