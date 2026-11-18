"""装饰器"""

# 装饰器是一种【可调用对象】(通常是函数)，它能接收一个函数作为参数，并且会返回一个新函数
# 装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能

'''
关键点：
1.接收被装饰的函数，同时返回新函数(wrapper)
2.装饰器"吐出来"的是wrapper函数，以后别人调用的也是wrapper函数
3.为了保证参数的兼容性，wrapper函数要通过*args, **kwargs接收参数
4.wrapper函数中主要做的是：调用原函数(被装饰的函数)、执行其他逻辑，但要记得将原函数的返回值return出去
'''
# 实际应用：在不改变原函数的前提下，给函数统一加上：日志、计时、校验、缓存等功能

"""类装饰器"""
'''
1.包含__call__方法的类，就是类装饰器
2.像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用
3.__call__方法通常接收一个函数作为参数，并且会返回一个新函数
'''

class Test1:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('Test1追加的逻辑')
            return func(*args, **kwargs)
        return wrapper

class Test2:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('Test2追加的逻辑')
            return func(*args, **kwargs)
        return wrapper

@Test1()
@Test2()
def mul(a, b):
    res = a * b
    print(f'{a} * {b} = {res}')
    return res

# result = mul(4, 5)
# print(result)

class SayHello:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'你好，我要开始计算{self.msg}了')
            return func(*args, **kwargs)
        return wrapper

# 使用@语法糖使用类装饰器
# @SayHello()
# def add(x, y):
#     res = x + y
#     print(f'{x} + {y} = {res}')
#     return res

# 手动装饰
# say = SayHello()
# add = say(add)

# result = add(6,8)
# print(result)

@SayHello('减法')
def sub(x, y):
    res = x - y
    print(f'{x} - {y} = {res}')
    return res

# print('&' * 20)
# result = sub(16, 8)
# print(result)

# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print('hello,我要开始计算了')
#         res = func(*args, **kwargs)
#         return res
#     return wrapper

# 带参数的装饰器(三层嵌套：外层接收配置、中间层接收函数、内层接收具体参数)
# def say_hello(msg):
#     def outer(func):
#         def warpper(*args, **kwargs):
#             print(f'hello,我要开始计算{msg}了')
#             return func(*args, **kwargs)
#
#         return warpper
#
#     return outer


# @say_hello('加法')
# def add(x, y):
#     res = x + y
#     print(f'{x} + {y} = {res}')
#     return res


# result = add(1, 2)
# print(result)


# 手动装饰，写起来会麻烦一些，不推荐 推荐：@装饰器名
# add = say_hello(add)
# result = add(1, 2)
# print(result)


# @say_hello('减法')
# def subtract(x, y):
#     res = x - y
#     print(f'{x} - {y} = {res}')
#     return res


# print('*' * 20)
# result = subtract(10, 2)
# print(result)

# 多个装饰器一起使用
def test1(func):
    print('a我是test1装饰器')

    def wrapper(*args, **kwargs):
        print('test1追加的逻辑')
        return func(*args, **kwargs)

    return wrapper


def test2(func):
    print('b我是test2装饰器')

    def wrapper(*args, **kwargs):
        print('test2追加的逻辑')
        return func(*args, **kwargs)

    return wrapper

@test1
@test2
def addition(x, y):
    res = x + y
    print(f'{x} + {y} = {res}')
    return res


print('^' * 20)
result = addition(5, 6)
# func = test1(test2(addition))
# result = func(4,5)
print(f'结果：{result}')
print('^' * 50)

