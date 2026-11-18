"""线程创建"""

import time, os
from threading import get_native_id, Thread, RLock

'''
Thread 的参数：
    group：默认值为None(应当始终为None)
    target：子线程要执行的可调用对象，默认值为 None
    name：线程名称，默认为 None。如果设置为 None，python会自动分配名字
    args：给 target 传的位置参数(元组)
    kwargs：给target 传的关键字参数(字典)
    daemon：标记线程是否为守护线程，取值为布尔值(默认为 None)

'''

class SpeakThread(Thread):
    def __init__(self, lock):
        Thread.__init__(self)
        self.lock = lock
    def run(self):
        for index in range(10):
            with self.lock:
                print(f'我在说话{index + 1},进程的pid是{os.getpid()},线程编号：{get_native_id()}')
            time.sleep(1)

class StudyThread(Thread):
    def __init__(self, lock):
        super().__init__()
        self.lock = lock
    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在学习{index + 1},进程的pid是{os.getpid()},线程编号：{get_native_id()}')
            time.sleep(1)


def speak(lock):
    for index in range(10):
        with lock:
            print(f'我在说话{index + 1},进程的pid是{os.getpid()},线程编号：{get_native_id()}')
        time.sleep(1)


def study(lock):
    for index in range(5):
        with lock:
            print(f'我在学习{index + 1},进程的pid是{os.getpid()},线程编号：{get_native_id()}')
        time.sleep(1)


if __name__ == '__main__':
    print(f'----start---进程的pid是{os.getpid()},线程编号：{get_native_id()}')
    lock = RLock()
    # 使用Thread创建线程
    # t1 = Thread(target=speak, args=(lock,))
    # t2 = Thread(target=study, args=(lock,))

    # 继承Thread类创建线程对象
    t1 = SpeakThread(lock)
    t2 = StudyThread(lock)
    
    # 调用线程对象的 start 方法，会立刻将该线程交由操作系统进行调度
    t1.start()
    t2.start()
    # 让主线程等 t1 和 t2 线程执行完毕后，主线程再继续执行
    t1.join()
    t2.join()
    print('-------------------end-------------------')
