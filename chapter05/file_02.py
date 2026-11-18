from datetime import datetime
class Person:
    # 类属性，保存在类身上
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存公共数据
    max_age = 120
    plant = '地球'

    # 说明：当一个函数被定义在了类中时，那这个函数就被称为方法
    # __init__()：初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # __init__()参数：当前正在创建的实例对象(self),其他的自定义参数
    # __init__()方法会自动调用
    def __init__(self, name, age, gender):
        # 给实例添加属性，实例属性 【实例.属性名 = 值】
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己独一份的实例属性，各个实例之间是互不干扰的
        self.name = name
        # self.age = age
        self.gender = gender
        if age <= Person.max_age:
            self.age = age
        else:
            print(f'年龄超出范围了，已经将年龄设置为最大值：{Person.max_age}')
            self.age = Person.max_age

    # 实例方法
    # 自定义方法：给实例添加行为
    # 自定义方法的参数：调用方法的实例对象(self)、其他参数
    # 自定义方法只有一份，保存在类身上，所有该类的实例对象，都可以调用自定义方法
    def speak(self, msg):
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender},我想说:{msg}')

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    # 类方法
    # 类方法参数：当前类本身(cls)、自定义参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    # 类方法也能通过实例调用到，但是非常不推荐
    @classmethod
    def test(cls, data):
        print('我是类方法', cls, data)

    @classmethod
    def change_plant(cls, value):
        cls.plant = value

    @classmethod
    def create(cls, info_str):
        name,year,gender = info_str.split('-')
        current_year = datetime.now().year
        age = current_year - int(year)
        return cls(name, age, gender)

    # 静态方法
    # 静态方法参数：只有自定义参数
    # 静态方法内部不会访问任何类和实例相关的内容
    # 静态方法常用于定义与类相关的工具方法
    # 静态方法也能通过实例调用到，但是非常不推荐
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - int(year)
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]



p1 = Person('Kai', 32, '男')
p2 = Person('lcf', 30, '女')

# print(p1, type(p1))
# print(p2, type(p2))

# print(p1.name, p1.age, p1.gender)
# print(p2.name, p2.age, p2.gender)

# p1.name = 'Who'
# print(p1.name, p1.age, p1.gender)

print(Person.is_adult(2005))
print(Person.mask_idcard('142232200509026789'))

print(Person.__dict__)
# Person的实例对象身上没有自定义方法
print(p1.__dict__)
print(p2.__dict__)

Person.test(7)
Person.change_plant('宇宙')

p3 = Person.create('简哈-1994-男')
print(p3.__dict__)

p4 = p1.create('简单-1994-男')
print(p4.__dict__)

# p2.adress = '山西'
# print(p2.__dict__)

# print(type(p1))
# print(type(p2))

# 自行自定义的方法过程：实例对象自身 =》 实例【缔造者】身上
p1.speak('好好学习，天天向上')
p1.run(800)

Person.run(p2, 100)


def speak():
    print('我是函数，不是类中的方法')


p1.speak = speak
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)

p1.speak()

print(Person.max_age, p1.max_age, p2.max_age)
print(Person.plant, p1.plant, p2.plant)
