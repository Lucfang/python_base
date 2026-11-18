"""内存分析"""
from chapter05.file_03 import Person

a = 666
# 内存地址
print(id(a))
print(hex(id(a)))

b = a
print(id(b))

print(a, b)

a = 888
print(id(a))
print(id(b))

print(a, b)

del b

stu_list = ['张三', '李四', '王五']
print(id(stu_list))
print(id(stu_list[0]))

stu_list[0] = '阿三'
print(id(stu_list))
print(id(stu_list[0]))


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f'大家好，我叫{self.name}, {self.age}, {self.gender}')


p1 = Person('lcf', 30, '女')
p2 = Person('Kai', 32, '男')

print(id(Person))
print(id(p1))
print(id(p2))

