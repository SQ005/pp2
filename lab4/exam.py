import json

with open("data.json", "r") as json_file:
    a = json.load(json_file)
# print(json.dumps(a, indent = 2))
# print(type(a))
# print(a['imdata'])
for i in a['imdata']:
    print(i['l1PhysIf']['attributes']['dn'])
               
import os
print(os.getcwd())