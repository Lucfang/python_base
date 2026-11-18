""" 进制 """
# 二进制
num2 = 0b1101
# 八进制
num8 = 0o7777
# 十六进制
num16 = 0x1cf

print(num2, num8, num16)

num = 7777
result2 = bin(num)
result8 = oct(num)
result16 = hex(num)
print(result2, result8, result16)

value2 = int('0b1101', 2)
value8 = int('0o7777', 8)
value16 = int('0x77', 16)
print(value2, value8, value16)
