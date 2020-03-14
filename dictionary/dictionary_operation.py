user = {
    "name": "张三",
    "age": 18,
    "address": "China",
}
print(user)

# 遍历所有键值对
for key, value in user.items():
    print(key)
    print(value)

print('----------------')
# 遍历所有键
for key in user.keys():
    print(key)


print('----------------')
# 按顺序遍历所有键
for key in sorted(user.keys()):
    print(key)

print('----------------')
# 遍历所有值
for value in user.values():
    print(value)