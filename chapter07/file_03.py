"""异常处理2"""
# 当程序遇到不符合预期情况时，可以使用raise语句手动触发(抛出)异常
'''
异常传递机制：
1.如果异常没有被当前代码块所捕获处理，那该异常就会沿着调用链，逐层传递给其调用者
2.如果所有调用者，都没有捕获该异常，那最终程序将因【未处理异常】而意外终止
'''
'''
自定义异常类
1.由开发人员自己定义一个异常类，用来表示代码中"更具体、更有业务含义"的异常
2.具体规则：定义一个类(类名通常以Error结尾)，继承Exception类或它的子类
'''

class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__(f'【校名异常】{msg}')

def check_school_name(name: str):
    if len(name) < 3:
        raise SchoolNameError('校名过短')
    else:
        print('学校名是合法的')

try:
    check_school_name("王")
except Exception as e:
    print(f'程序异常，{e}')

# raise SchoolNameError('学校名称重复')

# def test1():
#     print('*********test1开始***********')
#     try:
#         result = '100' + 100
#     except Exception as e:
#         print(f'程序异常：{e}')
#     print('*********test1结束***********')
#
# def test2():
#     print('*********test2开始***********')
#     test1()
#     print('*********test2结束***********')
#
# def test3():
#     print('*********test3开始***********')
#     test2()
#     print('*********test3结束***********')
#
# test3()




# print('欢迎使用年龄判断系统')
# try:
#     age = int(input('请输入你的年龄：'))
#     if 18 <= age <= 120:
#         print('成年人')
#     elif 0 <= age < 18:
#         print('未成年人')
#     else:
#         raise ValueError('年龄应该是0-120之间的整数')
#         # print('输入的年龄有误(年龄应该是0-120之间的整数)')
# except Exception as e:
#     print(f'我是异常处理逻辑，异常时{e}')


