"""三种权限 及 getter与setter"""

class Person:
    def __init__(self, name, age, gender):
        # 公有属性：当前类中、子类中、类外部都可以访问
        self.name = name
        # 受保护的属性：当前类中、子类中都可以访问
        self._age = age
        # 私有属性：仅能在当前类中访问
        self.__gender = gender

    def speak(self):
        print(f'我叫{self.name},年龄是{self._age},性别是{self.__gender}')

    # 注册age属性的getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age

    # 注册age属性的setter方法，当修改Person实例的age属性时，下面的age方法就会被自动调用
    @age.setter
    def age(self, value):
        self._age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        print('性别不能修改，如有问题请联系管理员')


class Student(Person):
    def hello(self):
        print(f'我是学生,我叫{self.name},年龄是{self._age}')


p1 = Person('Lcf', 30, '女')
p1.speak()
# 在类的外部，如果强制访问【受保护的属性】也可以访问到，但是十分不推荐
# 在类的外部，如果强制访问【私有属性】不能访问到，而且会报错
print(p1.name, p1._age)
print(p1.age)

p1.age = 18
# python底层是通过重命名的方式实现私有属性的
print(p1.__dict__)

s1 = Student('Lcf', 30, '女')
s1.hello()
