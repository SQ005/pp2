# text1 = "mySuperVar" #camelcase
# text2 = "my_super_var" #snakecase
# text3 = "MySuperVar" #Pascalcase


#1///
import re
def match(text):
    
    pattern = "a.*b"
    x = re.search(pattern, text)
    print(x)

match(text = input())
#2///
def match(text):
    pattern = "a.b{2,3}"
    x = re.search(pattern, text)
    print(x)

match(text = input())
#3///
import re
text = input()
pattern = "[a-z]+_[a-z]+"
x = re.search(pattern, text)
print(x)

#4///
import re
text = input()
pattern = "[A-Z][a-z]+"
x = re.search(pattern, text)
print(x)
#5///
import re
text = input()
pattern = "a.+b"
x = re.search(pattern, text)
print(x)
#6///
import re
text = input()
pattern = "[.,\s]"
print(re.sub(pattern, ":", text))
#7///
word = input("Enter you snake_case word: ")
list1 = re.split("_", word)

for i in range(1, len(list1)):
    list1[i] = list1[i].capitalize()
print(''.join(list1))
#8///
import re
text = input()
print(re.findall('[A-Z][^A-Z]*', text))

#9///
text = input("Enter a string: ")
str1 = re.sub('([a-z])([A-Z])', r'\1 \2', text)
print(str1)
#10///camel case string to snake case
import re
def f(mObject):
    print (mObject.group("g1"))
    print (mObject.group("g2"))
    return mObject.group("g1") + "_" + mObject.group("g2"). lower()

text = "mySuperVar" #camel case
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"
print(re.sub(pattern, f, text))


text = "my_super_var"
pattern = "(?P<g1>\w)(?P<>g2)\w"
print(re.sub(pattern, f, text))

