""" 特殊的字面量——None """

''' 
None是一个特殊字面量，它表示：空值/无值/无意义
NoneType
False
不能参与运算，也不能拼接字符串
不给函数设置返回值，函数默认返回None
'''
print(type(None))

print(bool(None))

msg = None

if not msg:
    print('hello world')