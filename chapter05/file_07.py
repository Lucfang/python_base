"""多态"""
# 多态的概念：同一个方法名，在不同的对象上调用时，能呈现出不同的行为
'''标准多态'''


class Animal:
    def speak(self):
        print('动物正在发出声音!')


class Dog(Animal):
    def speak(self):
        print('汪汪汪!')


class Cat(Animal):
    def speak(self):
        print('喵喵喵!')

class Pig:
    def speak(self):
        print('哼哼哼!')


def make_sound(animal: Animal):
    # 多态的体现
    animal.speak()


a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()

make_sound(a1)
make_sound(d1)
make_sound(c1)
# 此行代码如果在其他语言中会报错，python不会报错，但是不推荐这样写
make_sound(p1)

'''鸭子多态'''
# 核心理念：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子
# 鸭子类型是一种编程风格，它不检查对象的类型，只关注对象能否“做某件事”(是否有对应的方法)

class Fish:
    def speak(self):
        print('咕噜噜!')

class Bear:
    def speak(self):
        print('哼哼哼!')

def make_animal_sound(animal):
    animal.speak()

f1 = Fish()
b1 = Bear()
make_animal_sound(f1)
make_animal_sound(b1)