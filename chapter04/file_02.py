"""数组容器：元组(tuple)"""

'''元组是一种与列表类似的数据容器，它与列表的区别时：元组中的元素不可修改'''

t1 = (18, 24, 30, 36, 60)
t2 = ('山西', '北京', '上海', '江苏', '浙江')
t3 = (100, True, '你好', None, (100, 200, 300), [600, 800, 100])

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t3[1])

t3[5][2] = 700
print(t3)

t4 = ()
t5 = tuple()
print(t4, type(t4))
print(t5, type(t5))

t6 = ('你好',)
t7 = (7,)
print(t6, type(t6))
print(t7, type(t7))

'''常用方法'''
result = t2.index('北京')
print(result)

c = t3.count(100)
print(c)

'''常用内置函数'''
max_value = max(t1)
print(max_value)

min_value = min(t1)
print(min_value)

len_value = len(t1)
print(len_value)

res = sorted(t1)
print(tuple(res))

sum_value = sum(t1)
print(sum_value)

'''实际开发中的元组不一定是用户自己定义的，比如函数的可变参数*args就是一个元组'''


def demo(*args):
    print(args)
    print(type(args))
    return sum(args)


res = demo(1, 2, 3)
print(res)
