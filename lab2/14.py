list = ["a", "b", "c"]
list1 = [1, 2, 3]
list2 = list + list1
print(list2)

for x in list:
    list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)