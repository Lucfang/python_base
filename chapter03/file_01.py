""" 函数 """


# 定义函数
def welcome():
    print('欢迎来到python小课堂')
    print('现在正在学习的是function')


# 调用函数
welcome()

''' 函数参数的使用 '''


def order(num, dish):
    print(f'您点的是{num}份{dish}')


order(1, '鱼香肉丝')
order(2, '辣椒炒肉')

''' 位置参数 '''


def greet(name, gender, age, height):
    print(f'我叫{name},性别{gender},年龄{age},身高{height}')


greet('lcf', '女', 30, 165)

'''关键字参数'''
greet(height=165, age=30, gender='女', name='lcf')

''' 限制传参方式:
    1./前边只能用位置参数，*后面只能用关键字参数
    2./和*同时使用时，/必须在*的前面 '''

''' 参数默认值：默认参数必须要放在必选参数的后面 '''


def hello(name, gender, age, height, msg='hello'):
    print(f'我叫{name},性别{gender},年龄{age},身高{height}')
    print(f'我想说{msg}')


hello('张三', '男', 18, 183, 'we are one,exo')

''' 
可变参数
定义函数时，在形参名前加*，可以接收任意数量的位置参数，并打包成一个元组
定义函数时，在形参前面加**，可以接收任意数量的关键字参数，并打包成一个字典
可变位置参数、可变关键字参数，可以同时使用，但是必须先写可变位置参数
可变位置参数、可变关键字参数，也能与其他类型的参数一起使用
'''


def test1(*args):
    print(args)


test1(1, 2, 3)


def test2(**kwargs):
    print(kwargs)


test2(name='lcf', age=30, height=165)


def test3(a, b, *args, c='KAI', **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)


test3('EXO', 12, '男子团体', '12人', c='金钟仁', gender='男', desc='94line')

''' 函数返回值 '''


def add(a, b):
    print(f'{a} + {b} = {a + b}')
    return a + b


result = add(1, 2)

print(result)

''' 阶乘函数 '''
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(5)
print(result)

''' 函数说明文档 '''
def multiply(a, b):
    """
    计算两个数相乘的结果
    :param a: 第一个数
    :param b: 第二个数
    :return: 两者相乘的结果
    """
    return a * b

result = multiply(5, 6)
print(result)