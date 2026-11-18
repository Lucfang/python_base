"""重新认识函数"""
# 函数也是对象
a1 = 100
a2 = 'hello'
a3 = [6, 7, 8, 9]


def welcome():
    print('你好啊')


print(type(a1))
print(type(a2))
print(type(a3))
# welcome函数是function类的实例对象
print(type(welcome))

# 函数可以动态添加属性
welcome.desc = '这是一个打招呼的函数'
welcome.version = '1.0'
print(welcome.desc)
print(welcome.version)
print(welcome.__dict__)

# 函数可以赋值给变量
say_hello = welcome
say_hello()
print(say_hello.__dict__)


# 可变参数 vs 不可变参数

def hello(data):
    print('B', data, id(data))
    data = 888
    print('A', data, id(data))


print('before', a1, id(a1))
hello(a1)
print('after', a1, id(a1))


def hi(data):
    print('B', data, id(data))
    data[2] = 77
    print('A', data, id(data))


print('before', a3, id(a3))
hi(a3)
print('after', a3, id(a3))

# 函数也可以作为参数
def caller(f):
    print('caller函数调用了')
    f()

caller(welcome)

# 函数也可以作为返回值
def test():
    print('这只是一个测试')
    def show_msg(msg):
        print(msg)
    return show_msg
result = test()
result('hahahaha,哈哈哈哈')