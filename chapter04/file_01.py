""" 数据容器:列表 """
list1 = [2026, 11, 7, 30, 6]
list2 = ['北京', '包头', '西安', '杭州']
list3 = [23, '尚硅谷', True, None, [100, 200, 300]]

print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))

''' 正索引 '''
print(list1[3])

''' 负索引 '''
print(list2[-3])

'''
函数 vs 方法
当一个函数隶属于某个对象时，那该函数就是该对象的一个方法
b() 函数
a.b() 调用a的b方法
'''

""" 新增 """
'''在列表尾部追加一个元素'''
list1.append(1)
'''在列表指定下标处添加一个元素'''
list1.insert(6, 10)
'''将可迭代对象中的内容依次取出，追加到列表尾部'''
list1.extend([2020, 8, 3])
list1.extend(range(30, 35))

print(list1)

""" 删除 """
'''删除指定位置的元素'''
result = list1.pop(1)
print(result)
print(list1)
'''删除列表中第一次出现的指定值'''
list1.remove(3)
print(list1)
'''删除指定位置的元素'''
del list1[11]
print(list1)
'''删除列表中的所有元素'''
list1.clear()
print(list1)

"""修改"""
list3[0] = 30
print(list3)

"""查询"""
print(list3[0])

"""常用方法:浅层操作"""
index = list2.index('北京')
print(index)

count = list3.count(30)
print(count)

list2.reverse()
print(list2)

num_list = [30, 2026, 7, 9, 2, 18]
num_list.sort()
print(num_list)

list2.sort()
print(list2)

"""常用内置函数"""
result = sorted(list2, reverse=True)
print(result)

length = len(list2)
print(length)

max_value = max(num_list)
print(max_value)

minValue = min(num_list)
print(minValue)

sum_value = sum(num_list)
print(sum_value)

'''enumerate中start，遍历可以从指定位置开始，但是不改变原数组的索引值'''
for index, item in enumerate(num_list, start=1):
    print(index, item)
