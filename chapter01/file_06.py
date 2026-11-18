""" 数据类型 """
import sys

print(type('张三'))
print(type(18))
print(type(65.4))
# 1是true 0是false
print(type(True))
print(type(False))
print(bool(10))
print(bool(0))
print(bool('hello'))
print(bool(''))

''' 整形 '''
age = 18
temp = -15
score = 0

# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更容易读
salary = 21_000
house_price = 3_000_000
print(salary, house_price)

# python中整数的上限值，取决于执行代码的计算机的内存和处理能力
a = 999999999999999999999999999999999999999999999999999999
print(a)
res = 9 ** 9999
sys.set_int_max_str_digits(0)
print(res)
b = res + 100

''' 浮点型 '''
# weight = 110.04
balance = 600000.5690

# 浮点型的科学技术法表示
speed_of_sound = 3.4e+2
print(speed_of_sound)
world_population = 7.8e9
print(world_population)
distance_sun_earth = 1.496E8
print(distance_sun_earth)
one_ml = 1e-3
print(one_ml)

''' 字符串定义方式 '''
message1 = '加油，天下没有难学的技术'
message1 = "加油，天下没有难学的技术"
message1 = '''加油，天下没有难学的技术'''
message1 = """加油，天下没有难学的技术"""

''' 字符串的格式化输出 '''
name = '张三'
gender = '男'
weight = 51.45
age = 18

# 直接用+进行拼接
info = '我叫' + name + '，我是' + gender + '生'
print(info)
# 使用占位符
info2 = '我叫%s，我是%s生，我的体重是%f，年龄是%i' % (name,gender,weight,age)
print(info2)
# 使用f-string
info3 = f'我叫{name}，我是{gender}生，我的体重是{weight}，年龄是{age}'
print(info3)

''' 字符串占位符精度控制：%[宽度].[精度]类型 '''
info22 = '我叫%-2.2s，我是%s生，我的体重是%6.2f，年龄是%2i' % (name,gender,weight,age)
print(info22)

''' 转义字符 '''
print('python中可以使用\'包裹一个字符出啊')
print('我想学习一下换行，\n换行成功了吗')
print('helloo\b')
print('67%\r68%')
print('ab\tcd'.expandtabs(4))
print('我是\t中文')
