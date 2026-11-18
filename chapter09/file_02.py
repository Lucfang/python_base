"""手写迭代器"""
from cn2an import an2cn


# 迭代器是一次性的，状态只会向前推进，且不会自动重置(迭代器在遍历的过程中会被"消耗")
# region
# names = ['张三','李四','王五']
# it = iter(names)
# print(next(it))
# print(next(it))
# print(next(it))

# for item in it:
#     print(item)
# endregion


# 需求：让for循环可以遍历Person实例对象

# region
# class Person:
#     def __init__(self, name, age,gender,address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#
#     def __iter__(self):
#         return PersonIterator(self)
#
# class PersonIterator:
#     def __init__(self, p):
#         # 将外部传进来的数据保存好
#         self.p = p
#         # 设置迭代器的初始化位置(指针位置)
#         self.index = 0
#         # 配置好要遍历的内容
#         self.attrs = [p.name,p.age,p.gender,p.address]
#     # 迭代器__iter__方法会返回迭代器自身
#     def __iter__(self):
#         return self
#     # 每次调用__next__方法，会根据当前状态，返回下一个元素
#     def __next__(self):
#         # 如果指针的位置超出范围就抛出异常
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.attrs[self.index]
#         # 更新迭代器状态(指针位置)
#         self.index += 1
#         return value


# p1 = Person('张三',18,'男','北京昌平')
# for item in p1:
#     print(item)

# it = iter(p1)
# for item in it:
#     print(item)
# endregion

# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         # 设置迭代器的初始化位置(指针位置)
#         self.__index = 0
#         # 配置好要遍历的内容
#         self.__attrs = [name, age, gender, address]
#
#     def __iter__(self):
#         self.__index = 0
#         return self
#
#     def __next__(self):
#         # 如果指针的位置超出范围就抛出异常
#         if self.__index >= len(self.__attrs):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.__attrs[self.__index]
#         # 更新迭代器状态(指针位置)
#         self.__index += 1
#         return value
#
# # p1既是迭代对象也是迭代器
# p1 = Person('张三',18,'男','北京昌平')
# for item in p1:
#     print(item)
# endregion

# 进阶：迭代器玩的就是__next__
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置迭代器的初始化位置(指针位置)
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        # 如果指针的位置超出范围就抛出异常
        if self.__index >= len(self.__attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attrs[self.__index]
        if isinstance(value, str):
            value = value.upper()
        if isinstance(value, int):
            value = an2cn(value)
        # 更新迭代器状态(指针位置)
        self.__index += 1
        return value


# p1既是迭代对象也是迭代器
p1 = Person('zhangsan', 18, '男', '北京昌平')
for item in p1:
    print(item)
