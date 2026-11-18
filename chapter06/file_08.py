"""常用内置函数"""
import time
from functools import reduce

# 一、输入与输出
# print()
# print(
#     *values: object, 要输出的内容
#     sep: str | None = " ", 分隔符
#     end: str | None = "\n", 结束符
#     file: SupportsWrite[str] | None = None, 输出位置
#     flush: Literal[False] = False, 是否立即刷新
# )
# f = open('a.txt', 'w', encoding='utf-8')
# print(6, 7, 8, 9, '都是我的幸运运数字', sep='-', end='!', file=f)

# 第一种进度条
# print('加载中', end='')
# for index in range(5):
#     print('.', end='', flush=True)
#     time.sleep(1)
# print('完成！', end='')

# 第二种进度条
# for index in range(1, 101):
#     print(f'\r已加载{index}%', end='', flush=True)
#     time.sleep(0.1)
# input()

# 二、类型转换
# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()
# dict()

# 三、数学相关
# abs() 取绝对值
print(abs(-9))
print(abs(-2.5))
# round() 四舍五入
# 注意：round函数的四舍五入，是银行家舍入发：小于5就舍，大于5就入，等于5看奇偶(奇入偶舍)
print(round(6.5))
print(round(7.5))
print(round(7.543, 2))

# pow() 次方
print(pow(2, 3))  # 2的3次方
print(pow(2, 3, 5))  # 2的3次方对5取模

# divmod()  商和余数
print(divmod(10, 3))

# max()
# min()
# sum()
# map()
# filter()
# reduce()
# sorted()

# 四、数据容器相关
# len()
# range()
# for index in range(0, 10, 2):
#     print(index,end=' ')
# enumerate() 给序列添加索引
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# enumerate中start，遍历可以从指定位置开始，但是不改变原数组的索引值
print('*' * 10)
for index, item in enumerate(num_list, start=5):
    print(index, item)
# zip() 给多个序列一一配对
names = ['张三', '李四', '王五']
score = [90, 80, 70]
result = zip(names, score)
print(list(result))

# 五、类型判断与对象相关
# type()
# isinstance()
# issubclass()
# id()

# 六、逻辑判断相关
# all() 全为真返回True
l1 = [10, 'lcf', {1, 2, 3}] 
print(all(l1))
# any() 有一个为真即可
l2 = [0, '', None, False, 0]
print(any(l2))
# 七、字符串辅助相关
# ord() 获取字符的Unicode编码值
# chr() 将Unicode编码值转换为字符
