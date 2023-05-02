import csv

# data_names = ["Rusya", "Petrosyan"]
# with open("db.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         # [name_1,name_2]
#         # data_names
#         ["name", "number"]
#     )

# with open("db.csv", newline = '') as file:
#     reader = csv.DictReader(file, delimiter = ';')
#     for row in reader:
#         print(row['Name'],'|',row['number'])


with open("new_file.csv", "w") as file:
    writer = csv.writer(file,delimiter = ';')
    writer.writerow(['row 1 el 1','' 'row 1 el 2', 'row 1 el 3'])
    writer.writerow(['row 2 el 1', 'row 2 el 2', 'row 2 el 3'])
    writer.writerow(['row 3 el 1', 'row 3 el 2', 'row 3 el 3'])
        
# phonebook = [
#     "name", "number",
#     "Kuka", "87023489809",
#     "Zhora", "87729323342"
#     "Nurik", "87000232312"
# ]

# with open("db.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(
#         phonebook
#     )