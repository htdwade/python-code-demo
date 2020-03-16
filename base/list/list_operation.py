lists = ['a', 'b', 'c', 'd']
print(lists)

# append()添加元素到列表末尾
lists.append('e')
print(lists)

# insert()在列表指定位置添加元素
lists.insert(0, 'f')
print(lists)

# del语句删除列表指定元素
del lists[1]
print(lists)

# pop()删除列表末尾元素并返回其值
res = lists.pop()
print(res)
print(lists)

# pop(index)删除列表指定位置的元素并返回其值
res = lists.pop(2)
print(res)
print(lists)

# remove()根据值删除元素
# remove()只删除第一个指定的值，注意值多次出现的情况
lists.remove('b')
print(lists)


lists = ['b', 'c', 'f', 'a', 'b', 'e']
# sort()对列表进行排序
lists.sort()
print(lists)

# 向sort()方法传递参数reverse=True逆序排序
lists.sort(reverse=True)
print(lists)

# sorted()函数临时排序，用于显示列表元素，不会改变列表中的原始顺序
print(sorted(lists))
print(lists)


lists = ['apple', 'banana', 'orange']
# reverse()反转列表
lists.reverse()
print(lists)


# len()获取列表长度
print(len(lists))

# for value in lists进行遍历
for value in lists:
    print(value)

# range()生成一系列数字
for value in range(1, 5):
    print(value)

# 将生成的数字转成列表
numbers = list(range(1, 10))
print(numbers)

# range还可以指定步长
numbers = list(range(1, 10, 2))
print(numbers)


# 获取数字列表的最大值，最小值和总和
numbers = list(range(1, 10))
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# 列表解析，一行代码生成列表
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 复制列表，切片深拷贝，=号浅拷贝
lists1 = ['a', 'b', 'c']
lists2 = lists1[:]
lists3 = lists1
lists1.append('d')
print(lists1)
print(lists2)
print(lists3)
lists2.append('e')
lists3.append('f')
print(lists1)
print(lists2)
print(lists3)

