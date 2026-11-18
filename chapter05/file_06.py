"""object类"""


# python中，所有的类都继承了object类，即：object类是所有类的顶层父类
# 因为object是所有类的父类，所以python中的所有对象，都间接是object类的实例

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


print(issubclass(Person, object))
print(issubclass(int, object))
print(issubclass(str, object))
print(issubclass(list, object))
print(issubclass(tuple, object))
print(issubclass(dict, object))
print(issubclass(set, object))

p1 = Person('zs', 18, '男')
print(isinstance(p1, object))
print(isinstance(100, object))
print(isinstance('hello', object))
print(isinstance(True, object))
print(isinstance((10,20,6,7,8,9), object))

# 所有对象都继承了object类所提供的各种属性和方法。从而保证了每个对象都具备统一的基本能力
for item in object.__dict__:
    print(item)

# 对象身上自己的东西
print(p1.__dict__)
# 对象可以访问到的东西(自己的、继承过来的)
print(dir(p1))

print(p1.__str__())