import json
with open("data.json", "r") as json_file:
    f = json.load(json_file)
    # print(f)

for i in f['imdata']:
    print(i)