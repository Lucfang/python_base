"""序列操作"""

'''序列的切片操作：序列[起始索引:结束索引:步长]'''
list1 = [10, 20, 30, 40, 20, 60, 80, 70, 90, 70, 80, 90, 60]

l1 = list1[0:5:1]
print(l1)
l2 = list1[1:8:2]  # 20 40 60 70
print(l2)

l3 = list1[::]
print(l3)

l4 = list1[::-1]
print(l4)

tuple1 = (20, 30, 40, 70, 80, 60, 90, 70, 60, 70, 80, 90, 60)
print(tuple1)

t1 = tuple1[0:5:1]
print(t1)

t2 = tuple1[1:8:2]
print(t2)

t3 = tuple1[::]
print(t3)

'''序列的其他操作'''
'''相加：新序列 = 序列1 + 序列2(同类型的序列)'''

list11 = [10, 20, 30, 40]
list12 = [60, 70, 80, 90]
list112 = list11 + list12
print(list112)

tuple11 = (10,20,30,40)
tuple12 = (60,70,80,90)
tuple112 = tuple11 + tuple12
print(tuple112)

str1 = 'hello'
str2 = 'world'
str12 = str1 + str2
print(str12)

'''相乘：序列 * n (n必须为整数)'''

list22 = list12 * 3
print(list22)

tuple22 = tuple12 * 3
print(tuple22)

str22 = str2 * 3
print(str22)