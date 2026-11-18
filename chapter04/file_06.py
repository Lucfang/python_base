"""数据容器：集合"""
'''
集合的特点：无序 不能通过下标访问 去重
可变集合：创建后可以增删元素  set
不可变集合：创建后不可以增删元素 frozenset
'''

s1 = {10, 70, 60, 80, 90, 10, 20, 60, 80}
s2 = {20, '你好', True, 1, 12.4, 67, 98}
print(s1, type(s1))
print(s2, type(s2))

s2.add('everyone')
print(s2)

'''frozenset接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】'''
f1 = frozenset({10, 70, 60, 80, 90, 10, 20, 60, 80})
print(f1, type(f1))
f2 = frozenset([20, '你好', True, 1, 12.4, 67, 98])
print(f2, type(f2))
f3 = frozenset('hello')
print(f3, type(f3))

# f2.add(2)
'''空集合'''
s = set()
f = frozenset()
print(s, type(s))
print(f, type(f))

'''
集合中不能嵌套可变集合，但可以嵌套不可变集合
只有不可变的东西，才能安全放进集合中
'''
ss = {50, 60, 70, 80, 90}
ff = frozenset({10, 70, 80, 90, 10})
ll = [66, 77, 88, 99]
tt = ('hello', True, 1, 12.4, 67, 98)

# ss1 = {10, 20, 30, 40, ss, ll} 报错
ss2 = {ff, tt}
print(ss2, type(ss2))

'''增'''
# 集合.add(元素) 向集合中添加元素
s1.add(777)
print(s1, type(s1))

# 集合.update(元素) 向集合中批量添加元素
s1.update([77, 88, 66, 99])
print(s1, type(s1))

'''删'''
r = {6, 7, 8, 9}
# 集合.remove(元素) 从集合中移除元素，若元素不存在，会报错
r.remove(6)
print(r, type(r))

# 集合.discard(元素) 从集合中移除元素，若元素不存在，不会报错
r.discard(9)
print(r, type(r))

# 集合.pop() 从集合中随机移除一个元素
item = r.pop()
print(item, r)

# 集合.clear() 清空集合
r.clear()
print(r, type(r))

'''常用方法'''
a = {1, 2, 3, 4, 5}
b = {3, 5, 7, 8, 9, 6}
# 集合A.difference(集合B) A中不同于B的元素
result = a.difference(b)
print(result, type(result))

# 集合A.difference_update(集合B) 从集合A中删除集合B中存在的元素
a.difference_update(b)
print(a, b)

# 集合A.union(集合B) 合并两个集合
result = a.union(b)
print(result, type(result))

# 集合A.issubset(集合B) 判断集合A是否是集合B的子级
result = a.issubset(b)
print(result)
c = {6, 7, 8}
r = c.issubset(b)
print(r)

# 集合A.issuperset(集合B) 判断集合A是否是集合B的超集
result = a.issuperset(b)
print(result)
result = b.issuperset(c)
print(result)

# 集合A.isdisjoint(集合B) 判断集合A和集合B是否没有交集
x = {1, 2, 3, 7}
y = {6, 7, 8, 9}
result = x.isdisjoint(y)
print(result)

'''数学运算'''
# 并集：|
result = x | y
print(result)
# 交集：&
result = x & y
print(result)
# 差集：-
result = x - y
print(result)
# 对称差集：^
result = x ^ y
print(result)

'''集合不能使用while循环，但可以使用for循环'''
for item in result:
    print(item)
