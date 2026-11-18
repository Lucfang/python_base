"""数据容器：字符串"""
msg = '666 welcome to 666 shanxi 666'
print(msg[3])
print(msg[-1])

'''常用方法'''

result = msg.index('s')
print(result)

result = msg.split(' ')
print(result)

msg = msg.replace('s','S')
print(msg)

count_value = msg.count('S')
print(count_value)

'''从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下'''
res = msg.strip('6')
print(res)

'''常用内置函数'''
result = len(msg)
print(result)