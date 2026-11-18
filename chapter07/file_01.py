"""错误与异常"""
# Exception
from chapter01.file_07 import result


# 错误：代码本身有语法错误，解释器无法执行代码。 【无法通过异常处理机制解决】

# age = 18
# if age >= 18
#     print('成年人')

# 异常：代码在语法上没问题，但执行过程中出现了问题。 【可以通过异常处理机制解决】

# 1. ZeroDivisionError：当除数为0时触发
# x = 100 / 0

# 2. TypeError：当操作的数据类型不正确或不兼容时触发
# result = '10' + 5

# 3.AttributeError：当对象没有指定的属性或方法时触发

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# p1 = Person('张三', 18)
# print(p1.gender)

nums = [6, 7, 8, 9]
# nums.add(10)

# 4.IndexError：当索引超出范围(索引越界)时触发
# print(nums[5])

# 5.NameError：当使用了不存在的变量时触发
# print(school)

# 6.KeyError：当访问字典中不存在的key时触发
person = {'name': '张三', 'age': 18}
# print(person['gender'])

# 7.ValueError:当值不合法，但类型正确时触发
# int('hello')