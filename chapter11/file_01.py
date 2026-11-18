"""多进程 多线程"""
import time
from multiprocessing import Process, current_process, Lock, RLock

'''
一、并发 vs 并行
1.并发：在一段时间内，当CPU面对多个任务时，会将每个任务交替着执行一段时间
  特点：①对于某个瞬间，CPU实际上只在执行一个任务
       ②CPU通过高频切换不同的任务，让每个任务都能得到推进，仿佛多个任务在"同时进行"
       
2.并行：依赖于多个CPU 或 多核心的CPU，在同一时刻，每个核心都在执行不同的任务
  特点：①对于某个瞬间，每个CPU(或每个核心)都在执行不同的任务
       ②通过多个CPU(或多个核心)同时工作的方式，让多个任务真的在同时执行
       
说明:在现代操作系统中，并发与并行通常都是同时存在的              

'''
import os

# print(os.cpu_count())

'''
二、同步 vs 异步
1.同步(sync):发起一个任务之后，需要等待该任务完成后，才能继续执行后续任务
  表现：当前执行流会被【阻塞】
  
2.异步(async):发起一个任务之后，不必等该任务完成，就可以继续执行其他任务
  备注：虽然不必等待任务完成，但任务完成后，仍然可以通过特定方式获取结果
  表现：当前执行流不会被【阻塞】
'''

'''
三、注意区分概念：
并发/并行：描述的是任务如何被执行，即：多个任务在执行时，CPU要如何处理
同步/异步：描述的是任务如何被组织和等待，即：要不要等当前发起的任务执行完，再进行下一个任务

注意点：CPU的核心数和执行速度，不会改变任务之间的逻辑依赖关系
例如：一旦任务1、任务2、任务3 之间被设计为同步关系，那么：即便CPU切换任务的速度再快，核心数量再多，也不会在【任务1】没完成的情况下去启动【任务2】
'''

'''
四、进程 vs 线程
1.进程：
  ①一个正在运行的程序或软件，背后就对应着一个或多个进程
  ②进程是操作系统进行资源分配的基本单位
  ③每个进程都有自己独立的一块内存空间
  
2.线程：
  ①线程是进程内部的执行单元(一个进程中可以有多个线程)
  ②线程是操作系统进程CPU调度的基本单位
  ③同一进程内的线程共享进程资源  
'''

'''
主进程 vs 子进程
在windows操作系统中，查看：进程名、父进程pid、进程pid 的命令如下：
wmic process get Name,ParentProcessId,ProcessId
'''

# print(f'当前进程的pid是{os.getpid()}')
# print(f'当前进程的父进程的pid是{os.getppid()}')

'''
使用Process创建进程

Process的参数：
    group：默认值为None(应当始终为None)
    target：子进程要执行的可调用对象，默认值为None
    name：进程名称，默认为None,如果设置为None,python会自动分配名字
    args：给target传的位置参数(元组)
    kwargs：给target传的关键字参数(字典)
    daemon：标记进程是否为守护进程，取值为布尔值(默认为None,表示从创建方进程继承)
'''

'''
join 方法的作用：阻塞当前进程，等join前面的进程执行完，再继续往下执行
join(timeout)，其中timeout 是可选参数，表示等多久，单位是秒

注意点：
1.p.join()不是让进程p等，而是让"执行这行 join 代码的那个进程"去等，等的是p这个进程
2.当达到了 timeout 所指定的时间后，进程并不会终止，只是"不再等"了
3.join 必须在 start 之后
'''


def speak(lock):
    try:
        for index in range(5):
            # 上锁：如果锁是空闲的，立刻上锁，继续往下执行；如果锁被别人拿着：当前进程会阻塞等待(原地等)
            lock.acquire()
            print(
                f'{current_process().name}--我在说话{index + 1},进程的pid是{os.getpid()},我的父进程的pid是{os.getppid()}')
            # 释放锁：acquire 和  release必须成对出现，否则会永远卡住(死等)
            lock.release()
            time.sleep(1)
    # 注意：使用terminal终止进程，不会引起finally执行
    finally:
        print('我是finally里的逻辑')


def study(x, y, lock, msg='hello'):
    for index in range(10):
        # with lock：会自动完成两件事
        # 1.进入前：自动执行lock.acquire()上锁
        # 2.离开后：自动执行lock.release()释放锁
        # 好处：即便代码块里发生异常，也能保证释放锁，避免"卡死"
        # RLock可以多处上锁
        with lock:
            print(
                f'{x}-{y}-{msg}-{current_process().name}--我在学习{index + 1},进程的pid是{os.getpid()},我的的父进程的pid是{os.getppid()}')
        time.sleep(1)


# 注意：一定要写 if __name__ == '__main__'这个判断，原因如下：
# 1.当创建子进程时，python并不会把父进程内存里的speak函数直接交给子进程
# 2.python会启动一个全新的python解释器进程，重新执行当前的.py文件(作为模块)
# 3.在执行过程中，重新定义出一个speak函数，交给子进程
if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    # 创建两个 Process 类的实例对象(进程对象),分别是p1 和 p2
    # 注意点1：p1 和 p2 就对应着以后的两个子进程，在创建他们的时候，就要指定好他们要执行的任务
    # 注意点2：此时的 p1 和 p2 只是代码层面的两个进程对象，操作系统还没有真的创建 p1 和 p2两个进程
    lock = RLock()
    p1 = Process(target=speak, args=(lock,))
    p2 = Process(target=study, args=(6, 8, lock), kwargs={'msg': 'hello'})

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度
    p1.start()
    p2.start()

    time.sleep(3)
    print('我是主进程，我准备强制终止p1进程...')
    # 向操作系统申请强制终止p1进程
    p1.terminate()
    # 等操作系统彻底终止掉了p1进程
    p1.join()
    # 看一下p1进程是否"活着"
    print(p1.is_alive())

    # 让主进程等p1进程执行完毕后，主进程再继续执行
    # p1.join()
    # 让主进程等p2进程执行完毕后，主进程再继续执行
    # 让主进程等p2 3秒钟
    # p2.join(1)

    print('我是主进程中的【最后一行】打印')

