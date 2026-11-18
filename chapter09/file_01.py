"""迭代器"""
'''初识迭代器'''
# 1.能被for循环遍历的对象，被称为：可迭代对象(iterable)
# 2.可迭代对象(iterable)能调用到__iter__方法
l1 = ['张三', '李四', '王五']
# l1.__iter__()
# print(hasattr(l1, '__iter__'))
# 3.调用__iter__方法会得到：迭代器(iterator)
'''
备注：
1.__iter__是一个魔法方法，当调用iter函数时，__iter__会自动调用
2.可迭代对象.__iter__() 等价于 iter(可迭代对象)
3.如果iter(obj)能得到一个迭代器(iterator),那么obj就是可迭代对象
'''
# print(l1.__iter__())
# print(iter(l1)) #推荐

# 4.迭代器(iterator)拥有__next__方法，每次调用都会根据当前状态，返回下一个元素
'''
备注：
1.迭代器.__next__() 等价于 next(迭代器)
2.当所有元素全都取出后，若继续调用__next__方法，python会抛出StopIteration异常
'''
it = iter(l1)
# print(it.__next__())
# print(it.__next__())
# print(next(it))
# print(it.__next__())

# for循环背后的工作逻辑
# for item in l1:
#     print(item)

# it = iter(l1)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

# 5.迭代器(iterator)也拥有__iter__方法，并且其返回值是迭代器自身
# 这么设计的原因：让for循环也能遍历迭代器(即：为了让iter(迭代器)不出错)
# print(it)
# res = iter(it)
# print(res)
# print(it == res)
#
# x = iter(res)
# print(x)

print('*' * 50)
# for item in it:
#     print(item)

# 6.迭代器协议
'''
备注：
1.能被iter()接受
2.能被next()一步一步取值
'''

'''
迭代器的优势：
1.迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用
2.当数据量很大，不确定要用多少结果时，推荐使用迭代器
'''

import tracemalloc


class Fibonacci:
    def __init__(self, total):
        self.total = total
        self.__index = 0
        self.prev = 1
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= self.total:
            raise StopIteration
        # 前两项都是1
        if self.__index < 2:
            value = 1
            self.__index += 1
        else:
            value = self.prev + self.curr
            self.prev = self.curr
            self.curr = value
            self.__index += 1
        return value


tracemalloc.start()
f1 = Fibonacci(10000)
m = tracemalloc.get_traced_memory()[1]
print(f'内用占用是{m / 1024 / 1024}MB')
# for item in f1:
#     print(item)


def fibonacci(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for i in range(2, total):
        nums.append(nums[-1] + nums[-2])
    return nums


tracemalloc.start()
f2 = fibonacci(10000)
m = tracemalloc.get_traced_memory()[1]
print(f'内用占用是{m / 1024 / 1024}MB')
