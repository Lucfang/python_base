"""GIL"""
import sys
'''
GIL(Global Interpreter Lock) 全局解释器锁
1.GIL锁是 CPython 解释器中的一把互斥锁
2.GIL锁的作用：无论CPU有多少个核心，在某一时刻，只允许进程中的一个线程去执行python代码

CPython解释器中的多线程模型，本质上是并发，而不是并行(是快速切换，而不是同时进行)

为何这样设计？———— 为了确保解释器级别的数据安全

何时释放GIL锁：
1.主动释放(遇到I/O操作)
2.被迫释放(任务超时)

GIL锁和编码时使用到的 Lock 和 RLock 不是同一个东西
Lock 和 RLock 是业务层面的锁，目标是：让业务逻辑别出错
'''

print(sys.getswitchinterval())