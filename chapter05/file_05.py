"""魔法方法"""

# 概念：以__xxx__命名的特殊方法(双下划线开头和结尾)
# 特点：不需要我们手动调用，我们只需要准备好这些方法，python会在特定的场景下去自动调用

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 当执行print(Person的实例对象) 或 str(Person的实例对象)时调用
    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}'

    # 当执行len(Person的实例对象)时调用
    def __len__(self):
        return len(p1.__dict__)
    # 当执行Person实例对象1 < Person实例对象2时调用
    def __lt__(self, other):
        return self.age < other.age

    # 当执行Person实例对象1 > Person实例对象2时调用
    def __gt__(self, other):
        return self.age > other.age

    # 当执行Person实例对象1 == Person实例对象2时调用
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getattr__(self, item):
        return f'您访问的{item}属性不存在'


p1 = Person('Lcf', 30, '女')
p2 = Person('kai',32,'男')
print(p1)
str1 = str(p1)
print(str1)

print(len(p1))
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)
print(p1.address)