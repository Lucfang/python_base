"""数据处理函数"""
from functools import reduce

# map函数：对一组数据中的每一个元素，统一执行某种操作(加工)，并生成一组新数据
# 语法格式：map(操作函数，可迭代对象)
'''
注意点：
1.延迟执行：map不会立刻计算，只有在"需要结果"时才执行计算
2.返回的时迭代器对象，且一旦遍历，就会被"耗尽"
3.map不会影响元素数量
'''

# 统一数据处理
nums = [60, 70, 80, 90]
# map函数的返回值是一个迭代器对象，需要我们自己手动去遍历或者手动类型转换
result = map(lambda x: x * 2, nums)
print(list(result), type(result))
print(nums)

# 字符串转换
names = ('python', 'java', 'js')
result = map(lambda s: s.upper(), names)
print(tuple(result))
print(names)

# 类型转换
str_number = {'1', '2', '6', '7', '8', '9'}
result = map(int, str_number)
print(set(result))
print(str_number)

# filter函数：从一组数据中，筛选出符合条件的元素(过滤)，并组成一组新数据
# 语法格式：filter(过滤函数，可迭代对象)
'''
1.延迟执行：filter不会立刻筛选，只有在"需要结果"时才执行
2.返回的是迭代器对象，且一旦遍历完成就会被"耗尽"
3.filter可能会影响元素数量
'''

# filter函数的特殊用法：如果不传递过滤函数，那么自动会过滤掉"假值"
data = [0, 1, '', 'hello', [], (), 5]
result = filter(None, data)
print(list(result))

# 筛选数值
result = filter(lambda n: n > 70, nums)
print(list(result), type(result))
print(nums)

person = [
    {'name': 'zs', 'age': 20, 'gender': '男'},
    {'name': 'ls', 'age': 16, 'gender': '男'},
    {'name': 'ww', 'age': 17, 'gender': '男'},
    {'name': 'zl', 'age': 18, 'gender': '男'},
    {'name': 'qq', 'age': 12, 'gender': '男'}
]

result = filter(lambda p: p['age'] >= 18, person)
print(list(result))

# 过滤非法字符串
person_names = ['zs', 'ls', None, 'ww', 'qq']
result = filter(lambda n: n, person_names)
print(list(result))

# sorted函数：对一组数据进行排序，返回一组新数据
# 语法格式：sorted(可迭代对象，key=xxx,reverse=xxx)
# max函数、min函数，也可以传递key参数，用于设置筛选依据

result = sorted(nums, reverse=True)
print(result)

result = sorted(names, key=len)
print(result)

result = sorted(person, key=lambda p: p['age'])
print(result)

r = max(person, key=lambda p: p['age'])
print(r)

# reduce函数：将一组数据不断"合并"，最终归并成一个结果
# 语法格式：reduce(合并函数,可迭代对象,初始值)
# 备注：reduce函数需要从 functools 模块中引入才能使用

result = reduce(lambda x, y: x + y, nums, 10)
print(result)

# 字符串拼接
str_list = ['ab', 'cd', 'ef']
result = reduce(lambda x, y: x + y, str_list)
print(result)
