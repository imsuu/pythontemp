shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
#shoplist[-1] 指的是序列的最后一个项目， shoplist[-2] 将获取序列中倒数第二个项目
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
#序列切片包括起始位置，但不包括结束位置。
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
#全部
print('characters start to end is', name[:])

#切片操作中提供第三个参数，步长（Step）（在默认情况下，步长大小为 1）
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])
print(shoplist[::-2])
