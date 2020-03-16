# 读取文件内容，默认为只读模式
with open('test.txt', encoding='utf-8') as f:
    contents = f.read()
    print(contents.rstrip())

# 逐行读取
with open('test.txt', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
with open('test.txt', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())

# 写入文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('写入测试\n')
    f.write('继续测试\n')




