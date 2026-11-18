"""进程"""

'''进程之间不共享内存，因此也就不共享任何变量'''

from multiprocessing import Process

num = 100
names = []

def test1(list1):
    global num
    num += 10
    names.append('test1')
    list1.append(num)
    print(f'我是test1进程,操作之后的num是{num},操作之后的names是{names},{list1}')


def test2(list1):
    global num
    num -= 10
    names.append('test2')
    list1.append(num)
    print(f'我是test2进程,操作之后的num是{num},操作之后的names是{names},{list1}')


if __name__ == '__main__':
    print('主进程中的【第一行】代码')

    list1 = []

    p1 = Process(target=test1, args=(list1,))
    p2 = Process(target=test2, args=(list1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'主进程中的【最后一行】代码,操作之后的num是{num},操作之后的names是{names},{list1}')
