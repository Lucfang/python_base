"""类型注解"""
from chapter01.file_06 import gender

# 变量类型注解：给变量加上类型说明，可增强代码的可读性、让IDE的提示更优化

num: int = 1
price: float = 12.5
msg: str = 'hello everyone'
is_vip: bool = True
# result: None = None   语法上没有问题，但是这么些没有意义

# 注意：可以先写变量的类型注解，以后再赋值
school: str
# print('*' * 20,school)
school = '第一中学'

hobby: list[str] = ['抽烟', '喝酒', '烫头']

happy: list[str | int] = ['看电影', 6, 7, 8, 9]
from typing import Union

hobby: list[Union[int, str]] = ['抽烟', '喝酒', '烫头']

citys: set[str] = {'北京', '天津'}
citys: set[str | float] = {'北京', '天津', 67.89}

persons: dict[str, int] = {'张三': 18}
persons: dict[str | int, int] = {'张三': 18, 250: 20}

# scores是元组，并且元组中仅包含1个int类型的元素
scores: tuple[int] = (100,)
scores: tuple[int, int, int] = (100, 90, 80)
scores: tuple[int, ...] = (100, 90, 80, 70, 77, 88, 99)

'''
python会根据初始赋值推导变量的类型：
1.对于普通变量：后续如果改变类型，不会警告
2.对于容器变量：要求内部元素类型必须与推到出来的一致，否则就会警告
'''


# 函数类型注解：给函数的【参数】和【返回值】添加类型说明
# 语法格式：函数名(参数1:类型,参数2:类型) -> 返回值类型

def add(a: int, b: int) -> int:
    return a + b


result = add(10, 2)
print(result)


# 参数有默认值(python可以推导出参数的类型)、设置返回值类型

def sub(x=10, y=2) -> int:
    return x - y


result = sub(10, 2)
print(result)


def show_nums_info(nums: list[int]) -> tuple[int, int, float]:
    max_value = max(nums)
    min_value = min(nums)
    result
    max_value / min_value
    return max_value, min_value, result


result = show_nums_info([6, 7, 8, 9])
print(result)


def addition(*args: int) -> int:
    return sum(args)


result = addition(2, 3, 6, 7, 8, 9)
print(result)


def show_info(**kwargs: str | int):
    print(kwargs)


show_info(name='zs', age=18, gender='male')

# 获取函数的注解信息
print(add.__annotations__)
