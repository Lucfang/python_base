"""模块"""

'''
模块概述：
1.在python中，一个.py文件就是一个模块(Module)
2.模块中可以包含：变量、函数、类等很多内容
3.通常把能够实现某一特定功能的代码，集中放在一个模块中(模块就类似于一个工具箱)
4.模块可以提高代码的可维护性与可复用性，还可以避免命名冲突

模块的分类：
【1】标准库模块：随着python一起安装在我们电脑上的那些模块
    有一些标准库模块是用C语言实现的，这些用C语言实现的模块，又称：【内置模块】
【2】自定义模块
【3】第三方模块
'''

'''
模块命名注意点：
1.要符合标识符命名规则
2.模块名(.py文件名)区分大小写
3.不要与标准库模块同名(一旦同名，python会优先引入标准库模块)
'''

# 常见的模块导入方式：
# 【1】import 模块名
import order
import pay

# 【2】import 模块名 as 别名
import order as o
import pay as p

# 【3】from 模块名 import 具体内容1, 具体内容2,......
from order import max_order_amount, show_info
from pay import wechat_pay, ali_pay

# 【4】from 模块名 import 具体内容1 as 别名1,具体内容2 as 别名2
from order import max_order_amount as max_amt, show_info as show1
from pay import timeout as tm, show_info as show2

# 【5】from 模块名 import *
from order import *

'''
关于__all__:
【1】在python模块中，可通过__all__来控制【from 模块 import *】能导入哪些内容
【2】__all__的值可以是：列表、元组
'''

'''
关于__name__:
【1】__name__是每个python模块(.py文件)都拥有的一个内置变量
【2】它的具体值取决于模块的运行方式：
    · 作为主程序直接运行，__name__的值是__main__
    · 作为模块被导入到其他程序中运行，__name__的模块的文件名(不带.py)
'''

'''标准库模块的一些例子'''
'''拷贝对象(浅拷贝、深拷贝)'''
import copy

'''操作系统相关操作(文件、文件夹、路径系统层面的操作)'''
import os
# 创建一个文件夹
# os.mkdir('demo')

'''随机数相关(生成随机数、延时、格式化时间等)'''
import random

# 随机选择一个人
# names = ['张三', '李四', '王五']
# print(random.choice(names))

# 洗牌
# random.shuffle(names)
# print(names)

print(copy.__file__)
print(os.__file__)
print(random.__file__)

# 【内置模块】:无法看到具体实现，也没有__file__属性
'''时间相关操作(获取时间、延时、格式化时间等)'''
import time

# 休眠
# time.sleep(2)

# 获取当前时间
# print(time.strftime('%H:%M:%S'))
# print(time.strftime('%p %I:%M:%S'))

'''数学相关(开平方、去绝对值等)'''
import math

# 开平方
# print(math.sqrt(4))
# 取绝对值
# print(math.fabs(-11.1))

'''python解释器相关操作'''
import sys
# 获取python解释器的版本
# print(sys.version)

# print(sys.__file__)