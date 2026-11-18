""" 数据类型转换 """

# 将指定数据转换为字符串
result = str(18)
print(type(result), result)

result = int(15.6)
print(type(result), result)

result = int('79')
print(type(result), result)

result = float('1.23')
print(type(result), result)

result = float(18)
print(type(result), result)

""" 算数运算符 """
print(9 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
print(7 % 2)
# 取整
print(7 // 2)
print(7 ** 2)

""" 赋值运算符 和 复合运算符 """
age = 18
print(age)
temp = 1
age += temp
print(age)
age -= 1
print(age)

""" 比较运算符 """
a = 5
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print(ord('a'))
print(ord('我'))

""" 逻辑运算符 """
print(True and False)
print(8 > 7 and 5 > 6)
print(True or False)
print(8 > 7 or 5 < 6)
print(8 > 7 and 8 - 1)
print((8 < 7 or 8 * 2))
print(not 0)
print(not 'abc')


