"""异常处理"""
'''
1.为什么要进行异常处理？
程序运行过程中出现的异常，如果得不到处理，那程序就会立即奔溃，导致后续代码无法执行
异常处理不是让异常消失，而是将异常捕获到，随后根据异常的具体情况，来执行指定的逻辑

2.异常处理(初级):
【1】将可能出现异常的代码放在try中，出现异常后的处理代码写在except中
【2】如果try中的代码出现异常，那try中的后续代码将不会执行，并自动跳转到except中处理异常
【3】如果try中的代码没有异常，那except中的代码就不会执行
【4】无论是否发生异常，try-except后面的代码都会继续执行

3.异常处理的完整写法：
【try】尝试去做可能会出现异常的事情
【except】出现异常时的处理(出现异常时怎么补救)
【else】如果一切顺利(没有异常出现)要做的事
【finally】无论有没有异常，都要做的事
'''


print('欢迎使用本程序')
try:
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    result = a / b
    # print(x)
    print(f'{a}除以{b}的结果是:{result}')
# 一个except可以捕获不同的异常
except (ZeroDivisionError,ValueError,Exception) as e:
    if(isinstance(e,ZeroDivisionError)):
        print('程序异常：0不能作为除数')
    elif(isinstance(e,ValueError)):
        print('程序异常：您输入的必须是数字')
    else:
        print(f'程序异常：{e}')
# 异常处理(捕获指定的类型的异常)
# except ZeroDivisionError:
#     print('程序异常：0不能作为除数')
# except ValueError:
#     print('程序异常：您输入的必须是数字')
# except NameError as e:
#     print(f'程序异常：{e}')
# except Exception as e:
#     print(f'程序异常!异常信息：{e},{type(e)},{e.args},{e.__traceback__.tb_frame.f_code.co_filename},{e.__traceback__.tb_lineno}')
    # 通过traceback来回溯异常
    # import traceback
    # print(traceback.format_exc())
else:
    print('挺好的，try中的代码没有异常')
finally:
    print('无论有没有异常，计算都结束了')
print('**********我是后续的其他逻辑1***************')
print('**********我是后续的其他逻辑2***************')

# 验证一下异常类之间的继承关系
# print(issubclass(ZeroDivisionError,ArithmeticError))

# 多个except从上往下匹配，匹配成功后不再向下匹配
