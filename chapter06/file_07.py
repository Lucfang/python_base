"""列表推导式"""
# 列表推导式：用一条简洁语句，从可迭代对象中，生成新列表的语法结构
# 备注：列表推导式本质上是对 for循环 + append() 的一种简写形式
# 语法格式：[表达式 for 变量 in 可迭代对象]

# 元素double
nums = [60, 70, 80, 90]
result = map(lambda n: n * 2, nums)
print(list(result))

result = []
for n in nums:
    result.append(n * 2)
print(result)

result = [n * 2 for n in nums]
print(result)

# 带条件的列表推导式
result = [n * 2 for n in nums if n > 70]
print(result)

# 字典推导式
names = ['张三', '李四', '王五']
score = [90, 80, 70]
result = {names[i]: score[i] for i in range(len(names))}
print(result)

# 集合推导式
result = {n + '!' for n in names}
print(result)

# python中没有元组推导式，下面这种写法叫：生成器
result = (n + '!' for n in names)
print(result)
