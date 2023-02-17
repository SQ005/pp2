#1///
n = int(input())

s = [i**2 for i in range (1, n)]
# print(s)
#2///
n = int(input())
s1 = [i for i in range (0, n) if i % 2 == 0]
print(s1)
#3///
n = int(input())
s2 = [i for i in range (0, n) if i % 3 == 0 & i % 4 == 0]
print(s2)
#4///
a = int(input())
b = int(input())
s3 = [i**3 for i in range (a, b)]
print(s3)
#5///
n = int(input())
def odd(n):
    while n>=0:
        yield n
        n-=1
for i in odd(n):
    print(i)