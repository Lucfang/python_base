from abc import ABC, abstractmethod

"""抽象类"""


# 抽象类是一种不能直接实例化的类，它通常作为【规范】，让子类去继承并实现其中定义的【抽象方法】

# 继承了ABC类的类就成了抽象类
class MustRun(ABC):
    # 抽象方法
    @abstractmethod
    def run(self):
        pass

    def speak(self):
        print(f'你好，我叫{self.name}')

class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name},我在努力奔跑')


p1 = Person('鲁春芳', 30, '女')
p1.run()
p1.speak()
