import json

data = {
    "to user": "Nurik",
    "text": "hello",
    "attachments": ['1 png', '2 wap'],
    "type": "direct",

}

json_str = json.loads(data) 
print(type(json_str))
# print(json_str)
