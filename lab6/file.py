#1///
import os
for dirs, files in os.walk('C:\\temp',False):
   if len(dirs) > 0: 
      print(dirs)
   if len(files) > 0: 
      print(files)
        
   if len(dirs) > 0 and len(files) > 0: 
      joinedlist = dirs + files
      print(joinedlist)


#2///
import os
PATH = 'row.txt'
a = 'row.txt'
# if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
#    print("File exists and is readable")
# else:
#    print("Either the file is missing or not readable")
if os.path.isfile(a) and os.access(a, os.R_OK):
   print("File exists and is readable")
else:
   print("Either the file is missing or not readable")
f = open("row.txt", "r")
print(f.read())
f = open("row.txt", 'a')
f.write("Now we can write")
f.close()
f = open("row.txt", "r")
print(f.read())


#3///
# from pathlib import Path
# my_file = Path("C:\temp")
# if my_file.is_file():   
#    print("file exist")
# else:
#    print("file not exist")

# import os
# print("Test a path exists or not:")
# path = r'C:\temp'
# print(os.path.exists(path))
# print("\nFile name of the path:")
# print(os.path.basename(path))
# print("\nDir name of the path:")
# print(os.path.dirname(path))


# #4///
# num_lines = sum(1 for line in open('text.txt'))
# print(num_lines)


# # #5///
# import os
# os.remove("text.txt")
# f = open("text.txt", "x")
# f.writelines(["See you soon!", "Over and out."])
# f.close()
# f = open("text.txt", "r")
# print(f.read())

# #6///
# import string, os
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as f:
#        f.writelines(letter)


# #7///
# import shutil
# from shutil import copyfile
# copyfile('row.txt', 'text.txt')


# #8///
# import os
# if os.path.exists("text.txt"):
#    os.remove("text.txt")
# else:
#    print("The file does not exist")
