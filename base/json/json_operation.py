import json

message = ['a', 'b', 'c', 'd']

# json.dump()存储为json数据
with open('text.txt', 'w', encoding='utf-8') as f:
    json.dump(message, f)

# json.load()加载json数据
with open('text.txt', 'r', encoding='utf-8') as f:
    res = json.load(f)
    print(res)
