""" 协程 """

'''
什么是协程？
第一种描述：协程是一种可以被挂起，并且在挂起之后，还可以恢复执行的函数
第二种描述：协程又称微线程，是一种用户态内的上下文切换技术

注意：协程不是操作系统提供的，而是由程序员在用户态，实现的一种切换机制

协程函数(coroutine Function)：使用【async关键字】修饰的函数，就是协程函数
协程对象(coroutine Object)：调用【协程函数】，就会得到【协程对象】
注意：调用【协程函数】并不会执行【协程函数】中的代码

await 关键字的作用：
1.挂起：await 会暂停当前协程的执行
2.等待：遇到 await 关键字，事件循环会立即安排 await 后面的对象去执行，并等待该对象执行完成，并且可以拿到执行结果

        💡关键点：在执行 await 后面的对象时，会出现两种情况：
        情况一：如果在执行该对象中的代码时，遇到了【await I/O操作】(需要等待外部资源返回结果的操作)
            例如：网络请求、文件读写等
            那CPU的控制权就会交给事件循环
            事件循环会去调度循环中的其他任务(如果有的话)
            
        情况二：如果该对象中的代码，不包含任何【await I/O操作】
            例如：print打印、数学计算、逻辑计算等
            此时事件循环拿不到CPU的控制权，无法调度循环中的其他任务，不会发生任务切换
    
3.恢复：当 await 后的对象执行完毕，事件循环会恢复之前被挂起的协程，该协程会从当前挂起的位置继续执行，并拿到返回值

注意：await 后面只能写【可等待的对象】，常见的可等待对象：1.协程对象 2.Future对象 2.Task对象
    
'''
import asyncio

# 定义一个协程函数
async def work():
    print('work开始')
    print('work执行中....')
    # await等待一个协程对象(靠asyncio.sleep方法返回一个协程对象)
    res = await asyncio.sleep(5)
    print(res)
    print('work结束')
    return '工作结果'

# 调用协程函数，会得到协程对象
# coroutine_object = work()

'''
asyncio.run 方法做了3件事：
  1.创建一个事件循环
  2.将收到的协程对象，包装成一个任务(task),交给事件循环
  3.启动事件循环
注意：asyncio.run 会阻塞当前线程，直到任务执行完毕，并返回该任务 return 的最终结果
'''
# result = asyncio.run(coroutine_object)
# print(result)

async def main():
    print('main开始')
    # await等待一个协程对象(靠自己去编写协程函数，随后调用该函数来得到协程对象)
    res = await work()
    print(res)
    print('main结束')
    return 'main的返回值'

result = asyncio.run(main())
print(result)


