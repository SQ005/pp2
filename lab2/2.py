class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction():
  return True

if myFunction():
  print("Yes")

else:
  print("No")

x = 200
print(isinstance(x,int))