"""匿名函数"""


# 概念：所谓【匿名函数】就是没有名字的函数，它无需使用def关键字去定义
# 语法：python中使用lambda关键字来定义【匿名函数】，格式为：lambda 参数: 表达式
# 使用场景：当一个函数只用一次、只做一点点小事，使用匿名函数会更加简洁
'''
注意点：
1.只能写一行，不能写多行代码
2.不能写代码块(if、for、while)
3.冒号右边必须是表达式，且只能写一个表达式
4.表达式结果自动作为返回值
'''
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def calculate(func, a, b):
    print(f'计算结果为{func(a, b)}')

calculate(add, 10, 20)
calculate(sub, 10, 20)

addtion = lambda x,y: x + y
result = addtion(10, 20)
print(result)

calculate(lambda x,y: x + y, 10, 20)
calculate(lambda x,y: x - y, 30, 20)

is_adult = lambda age: '成年' if age >= 18 else '未成年'
print(is_adult(12))
