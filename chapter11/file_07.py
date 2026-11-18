"""继承Process_创建进程"""

from multiprocessing import Process
import time, os


class SpeakProcess(Process):
    def run(self):
        for index in range(5):
            print(f'我在说话{index + 1},进程的pid是{os.getpid()},我的父进程的pid是{os.getppid()}')
            time.sleep(1)


class StudyProcess(Process):
    def __iter__(self, a, b, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.b = b

        def run(self):
            for index in range(10):
                print(f'我在学习{index + 1},进程的pid是{os.getpid()},我的的父进程的pid是{os.getppid()}')
                time.sleep(1)


if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = SpeakProcess()
    p1.start()

    p2 = StudyProcess()
    p2.start()

    p1.join()
    p2.join()

    print('我是主进程中的【最后一行】打印')
