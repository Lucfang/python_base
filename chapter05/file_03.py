"""继承"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name},年龄是{self.age},性别是{self.gender},我想说:{msg}')


# 【子类、派生类】继承【父类、超类、基类】
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 调用父类的初始化方法
        # 方式一
        super().__init__(name, age, gender)
        # 方式二
        # Person.__init__(self, name, age, gender)
        # 子类独有的属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade

    # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会【覆盖】父类中的方法
    def speak(self, msg):
        super().speak(msg)
        print(
            f'我是学生，我叫{self.name},学号是{self.stu_id},年龄是{self.age},年级是{self.grade},性别是{self.gender},我想说:{msg}')

    def study(self):
        print(f'我叫{self.name},我努力学习，争取做到{self.grade}年级的第一名')


s1 = Student('lcf', 18, '女', '20251101', '高三')
print(s1, type(s1))
print(s1.__dict__)

# def speak(data):
#     print('我是s1自身的speak方法', data)
# s1.speak = speak

# 查找speak方法的过程：实例自身 =》 Student类 =》 Person类
s1.speak('hello')

s1.study()

# isinstance(instance,Class),判断某个对象是否为指定类或其子类的实例
result = isinstance(s1, Student)
print(result)
# issubclass(Class1,Class2),判断某个类是否是另一个类的子类
result = issubclass(Student, Person)
print(result)

"""多重继承"""


# 多重继承指一个类同时继承多个父类，从而拥有多个父类的属性和方法

class Worker:
    def __init__(self, company):
        self.company = company

    def do_work(self):
        print(f'我在{self.company}做兼职')


class Staff(Person, Worker):
    def __init__(self, name, age, gender, company, technology, hobby):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.technology = technology
        self.hobby = hobby

    def study(self):
        print(f'我在努力学习工作技能，包括{self.technology}')

s = Staff('LCF',30,'女','科技公司','开发：java、python','看书、看电影')
print(s.__dict__)
s.speak('我看工作才怪')
s.do_work()
s.study()
# 通过实例去查找属性或方法时，会先在实例自身上去查找，如果没有，就按照__mro__记录的顺序查找
print(Staff.__mro__)