"""包"""
from chapter01.file_07 import result

'''
包概述：
1. 在Python中，【包含__init__.py的文件夹】就是一个包(Package)
2. 我们通常会把【某个特定功能相关的所有模块】放入一个包中
3. 使用包可以进一步提升代码的可维护性、可复用性，便于管理大型项目

包的分类：
【1】标准库包
【2】自定义包
【3】第三方包
'''
'''
包与模块的关系：
1.一个模块就是一个.py文件，包是用来"管理模块"的目录(文件夹)
2.一个包中可以有多个模块，也可以有多个子包
'''

'''
包命名注意点：
1.要符合标识符命名规范
2.包名区分大小写(建议全部使用小写字母)
3.不要与标准库包同名
'''

# 常见的包导入方式：
# 【1】import 包.模块名
import trade.order
import trade.pay

print(trade.order.max_order_amount)

# 【2】import 包.模块名 as 别名
import trade.order as o
import trade.pay as p

o.show_info()

# 【3】from 包.模块名 import 具体内容1, 具体内容2,......
from trade.order import create_order, show_info
from trade.pay import wechat_pay, ali_pay

# 【4】from 包.模块名 import 具体内容1 as 别名1,具体内容2 as 别名2
from trade.order import max_order_amount as max_amt, show_info as show1
from trade.pay import timeout as tm, show_info as show2

# 【5】from 包.模块名 import *
from trade.order import *

# from trade.pay import *
show_info()

# 【6】from 包名 import 模块名
from trade import order, pay

# 【7】from 包名 import 模块名 as 别名
from trade import pay as p, order as o

o.create_order()

'''
关于__init__.py文件：
1.__init__.py 是包的初始化文件，在包被导入时，__init__.py会被自动调用
2.__init__.py 中可以编写一些包的初始化逻辑
3.__init__.py 中所定义的内容，会被【from 包名 import *】形式全部引入
4.__init__.py 中也可以使用__all__来控制包中的哪些模块可以被【from 包名 import *】引入
'''

# 【8】from 包名 import *
from trade import *

wechat_pay()

# 【9】import 包名
import trade

ali_pay()

# 引入子包
from trade.hello.hello import say_hello

say_hello()

# 标准库包的使用
from collections import Counter

names = ['java', 'sql', 'python', 'java', 'sql', 'java', 'sql', 'python']
result = Counter(names)
print(result)
