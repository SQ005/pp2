a = ["messi", "messi", "ronaldo"]
x = a.count("messi")

print(x)

points = [1, 2, 3, 4, 5, 6, 7, 8, 8, 4, 3, 3, 2, 9]
y = points.count(8)
print(y)

fruits = ['apple', 'banana', 'cherry']
footballers = ['Messi', 'Ronaldo', 'Zainudinov']

fruits.extend(footballers)
print(fruits)

v = footballers.index('Zainudinov')
print(v)

print(len(points))
# A list can contain different data types
list1 = [1, "apple", True]
print(list1)

print(type(list1))
thislist = list(("apple", "banana", "cherry"))
print(thislist)