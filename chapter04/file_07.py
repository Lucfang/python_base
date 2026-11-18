"""数据容器：字典"""
'''字典(dict)：key-value'''

d1 = {'Kai': 94, '世勋': 94, 'DO': 91}
print(d1, type(d1))

'''字典中的key不能重复，若出现重复，则后写会覆盖之前写的'''
d2 = d1 = {'Kai': 94, '世勋': 94, 'DO': 94, 'DO': 92}
print(d2, type(d1))

'''空字典'''
dd1 = {}
dd2 = dict()
print(dd1, type(dd1))
print(dd2, type(dd2))

'''
注意：
字典中的key必须是不可变类型，但value可以是任意类型
字典是可以嵌套的
'''

'''查询'''
result = d1['Kai']
print(result)

result = d1.get('lcf', '96')
print(result)

'''新增 or 修改：如果key不存在就新增，如果key存在就修改'''
d1['lcf'] = 96
print(d1)

'''批量修改'''
d1.update({'Kai': 1994, 'lcf': 1996})
print(d1)

'''删除'''
del d1['DO']
print(d1)

result = d1.pop('世勋')
print(result, d1)

result = d1.pop('do', '删除失败')
print(result, d1)

'''清空'''
d1.clear()
print(d1)

"""常用方法"""
'''keys()：获取字典中所有键,返回值是dict_keys类型'''
dd = {'Kai': 94, '世勋': 94, 'DO': 91}
result = dd.keys()
print(result, type(result))

# 注意：dict_keys和列表类似，可以被遍历，但是需要注意的是：它不能通过下表去访问元素
for item in result:
    print(item, dd[item])

# 借助内置的list函数，可以将dict_keys转换成list
l1 = list(result)
print(l1, type(l1))

'''values():获取字典中的所有值,返回值是dict_values类型'''
result = dd.values()
print(result, type(result))

'''items():获取字典中所有的键值对，返回值是dict_items'''
result = dd.items()
print(result, type(result))

'''字典不能使用while循环遍历，但是可以使用for循环遍历'''
for key in dd:
    print(key, dd[key])

for key in dd.keys():
    print(key, dd[key])

d = {'Kai': 94, '世勋': 94, 'DO': 91}
res = max(d, key=d.get)
print(res, type(res))
