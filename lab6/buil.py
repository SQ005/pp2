#1///
input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("Calculating sum of element of input list")
mult = 1
for n in list:
  mult *= int(n)
print("Mult = ",mult)
#2///
def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "Upper case characters : %s,Lower case characters : %s" % (u,l))

up_low(s = str(input()))
#3///
def ispalindrome(s):
    return ''.join(reversed(s))
s = ("KAZAK")
k = ispalindrome(s)
if s == k:
    print("Is Palindrome")
else:
    print("Is not palindrome")
#4///
from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after miliseconds:") 
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2123, 25100))
#5///
def true():
    x = all(mytuple)
    print(x)
mytuple = (123, "apple", "777")
true()


