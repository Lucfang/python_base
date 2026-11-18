""" 作用域 """
''' 
全局作用域 VS 局部作用域 
注意：局部作用域和局部变量，会在函数调用时创建，在函数执行结束后销毁
     全局作用域和全局变量，会在程序开始时创建，在程序结束后销毁
'''
a = 100
b = 200


def test():
    global a
    a = 300
    c = '尚硅谷'
    d = 'python'
    print(a)
    print(b)
    print(c)
    print(d)


test()
print(a)
