"""生成器"""
'''
Ⅰ 生成器：
1.生成器函数：函数体中如果出现了yield关键字，那该函数是【生成器函数】
2.生成器对象：调用【生成器函数】时，其函数体不会立刻执行，而是返回一个【生成器对象】

Ⅱ 写在【生成器函数】中的代码，需要通过【生成器对象】来执行：
1.调用【生成器对象】的__next__方法，会让【生成器函数】中的代码开始执行
2.当【生成器函数】中的代码开始执行后，遇到yield会"暂停"执行，并且其内部会记录"暂停"的位置
3.后续调用__next__方法时，都会从上一次"暂停"的位置，继续运行，直到再次遇到yield
4.遇到return会抛出StopIteration异常，并将return后面的表达式，作为异常信息
5.yield后面所写的表达式，会作为本次__next__方法的返回值

Ⅲ 生成器对象是一种特殊的迭代器(本质是通过yield自动实现了迭代器协议)

Ⅳ yield也能写在循环里

Ⅴ yield from 能把一个【可迭代对象】里的东西依次yield出去(for + yield)

Ⅵ 使用：生成器.send(值) 可以让生成器继续执行的同时给上一次yield传值
备注1：next只能取值，send既能取值，也能送值
备注2：第一次启动生成器，不能传值

Ⅶ 无论是迭代器还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容(注意：容易挤爆内存)

'''

'''
生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方式
语法格式：(表达式 for 变量 in 可迭代对象)
什么时候适合用生成器表达式? 当"每个结果，只依赖当前这一个元素"时
'''

nums = [5, 6, 7, 8, 9, 10]

# 列表推导式
result = [n * 2 for n in nums]
print(result)

# 生成器表达式
result2 = (n * 2 for n in nums)
print(list(result2))

# region
# def fibo(total):
#     prev = 1
#     curr = 1
#
#     for index in range(total):
#         if(index < 2):
#             yield 1
#         else:
#             value = prev + curr
#             prev = curr
#             curr = value
#             yield value
#
# f1 = fibo(10)
# print(f1)
# # for item in f1:
# #     print(item)
#
# # 无论是迭代器还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容(注意：容易挤爆内存)
# result = list(f1)
# print(result)
# endregion

# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__attr__ = ['name', 'age', 'gender', 'address']
#
#     def __iter__(self):
#         yield from self.__attr__
#         # yield self.name
#         # yield self.age
#         # yield self.gender
#         # yield self.address
#
#
# p1 = Person('张三', 18, '男', '北京昌平')
# for item in p1:
#     print(item)

# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     a = yield ('a我是第一个yield返回的数据')
#     print(a)
#     b = yield ('b我是第二个yield返回的数据')
#     print(b)
#     return 'hello'
#
# d = demo()
# d.send(None)
# # r1 = next(d)
# # print(r1)
# r2 = d.send(666)
# print(r2)
# try:
#     d.send(888)
# except StopIteration as e:
#     print(e)
# endregion

# region
# def demo():
#     nums = [6, 7, 8, 9, 10]
#     # for n in nums:
#     #     yield n
#     yield from nums
#
# d = demo();
# for n in d:
#     print(n)
# endregion

# region
# def create_car(total):
#     for index in range(1, total + 1):
#         yield f'我是第{index}台车'
#
# # 生成器对象
# cars = create_car(5)
#
# # c1 = next(cars)
# # print(c1)
#
# for car in cars:
#     print(car)

# endregion

# region
# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     yield ('我是第一个yield返回的数据')
#     a = 200
#     print(a)
#     yield ('我是第二个yield返回的数据')
#     b = 300
#     print(b)
#     return 'hello'
#
#
# d = demo()
# # 验证：生成器对象d 和迭代器一样，也拥有:__iter__ 和 __next__方法
# print(hasattr(d, '__iter__'))
# print(hasattr(d, '__next__'))
# # 验证：生成器对象的__iter__方法，和迭代器一样，返回的也是它本身
# result = iter(d)
# print(result)
#
# print(d, type(d))
#
# # for item in d:
# #     print(item)
#
# it = iter(d)
# while True:
#     try:
#         value = next(it)
#         print(value)
#     except StopIteration:
#         break

# r1 = next(d)
# print(r1)
# r2 = next(d)
# print(r2)
# try:
#     next(d)
# except StopIteration as e:
#     print(e)
# endregion
