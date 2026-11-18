"""队列(Queue)"""

# 我们之前学过 list tuple dict 它们的特点是：数据想怎么拿就怎么拿
# 队列(Queue)是一种【先进先出】的数据结构(先放进去的数据，一会先取出来)

from multiprocessing import Queue, Process
import time

# 创建一个队列
# q1 = Queue()
#
# q2 = Queue(3)

''' 1.put方法：往队列里放数据(入队) '''
# q1.put(6)
# q1.put(7)
# q1.put(8)

''' 2.get方法：从队列里取数据(出队) '''
# value1 = q1.get()
# print(value1)
# value2 = q1.get()
# print(value2)
# value3 = q1.get()
# print(value3)

''' 3.empty方法：判断队列是否为空 '''
# result = q2.empty()
# print(result)

''' 4.full方法：判断队列是否已满 '''
# result = q1.full()
# print(result)
#
# q2.put(6)
# q2.put(7)
# q2.put(8)
# result2 = q2.full()
# print(result2)

''' 5.qsize方法：获取队列长度 '''
# size = q2.qsize()
# print(size)

'''
6.队列具备等待模式
  当队列已满，继续put,就会进入等待模式，等别人调用get方法，取走一个元素
  当队列已满，执行：put(元素,timeout=秒数),就会等待指定秒数
  put_nowait方法，会直接向队列中添加元素，不会进入等待模式，若队列已满，会抛出异常
备注：put_nowait 等价于 put(元素,block=False),block的默认值为True
  get读多了，也会进入等待模式
  当队列已空，执行get(timeout = 秒数)，就会等待指定秒数
  get_nowait方法，会直接读取队列中的元素，不会进入等待模式，若队列已空，会抛出异常
备注：get_nowait 等价于 get(block=False)  
'''


# q2.put(9)
# q2.put(9,timeout=3)
# q2.put_nowait(9)
# q2.put(10,False)


# value4 = q1.get()
# q1.get(timeout = 5)
# q1.get_nowait()
# q1.get(block=False)

def test(q):
    time.sleep(3)
    result = q.get()
    print(f'我从这个队列中取出了一个元素:{result}')


if __name__ == '__main__':
    q = Queue(2)
    q.put(7)
    q.put(9)
    print(f'队列是否已满:{q.full()}')

    p1 = Process(target=test, args=(q,))
    p1.start()

    print('即将向已满的队列中添加一个元素')
    q.put('hello')

    print('目前队列中有的元素是')
    print(q.get())
    print(q.get())

