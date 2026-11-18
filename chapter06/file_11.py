"""闭包"""
'''
前置知识一：
1.每次调用函数时，python都会为函数创建一个新的局部作用域
2.函数执行完毕后，这个局部作用域会被销毁，其中的局部变量也会随之被释放

前置知识二：
1.在python中，【内层函数】可以访问其【外层函数】作用域中的变量
2.访问外层函数变量无需使用nonlocal，但修改外层变量时要使用nonlocal
'''

# 什么是闭包？闭包 = 内层函数 + 被内层函数所引用的外层变量
'''
闭包产生的条件：
1.要有函数嵌套
2.在【内层函数】中，要访问【外层函数】的变量
3.【外层函数】要返回【内层函数】（闭包"活下来"的条件）
'''
'''
注意点：
1.调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响
2.内层函数中用到的外层变量是可变对象，多个闭包之间依然相互影响
'''

'''
闭包的优点：
1.可以"记住状态"：不用全局变量，也不用写类，就能在多次调用之间保存数据
2.可以做"配置过的函数"：先传一部分参数，把环境固定住，得到一个定制版函数
3.可以实现简单的"数据隐藏"：外层变量对外不可见，只能通过内层函数访问
4.是装饰器(decorator)等高级语法的基础
'''

'''
闭包的缺点：
1.理解成本高：对初学者不太友好，滥用会让代码难读
2.如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用
3.很多场景下，其实用【类+实例属性】会更清晰，闭包不一定是最优解
'''


# outer函数中，被inner所使用到的那些变量会被封存到【闭包单元(cell)】中
# 这些cell会组成一个__closure__元组，最终放在了inner函数身上
def outer():
    msg = 'hello world'
    num = 10
    nums = []
    print(hex(id(num)))

    def inner(value):
        nonlocal num
        num += 1
        nums.append(value)
        print(num, nums)

    return inner


f = outer()
f(10)
f(20)
print('*' * 20)
ff = outer()
ff(50)
# 打印__closure__元组
print(f.__closure__)
print(f.__closure__[0].cell_contents)


def beauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)

    return show_msg


show = beauty('*', 10)
show('你好啊 你好啊')


class Beauty:
    def __init__(self, char, num):
        self.char = char
        self.num = num

    def show(self, msg):
        print(self.char * self.num + msg + self.char * self.num)


b = Beauty('*', 10)
b.show('hello everyone')
