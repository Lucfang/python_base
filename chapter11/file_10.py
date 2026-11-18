"""线程池"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import os, time
from threading import get_native_id, RLock

''' 1.创建【线程池执行器】、使用 submit 方法提交任务，使用 shutdown 方法等待任务完成 '''
''' 2.获取子线程执行后的返回结果(Future类的实例对象 + result方法) '''
''' 3.使用 as_completed：按"完成顺序"获取结果 '''
''' 4.使用 add_done_callback 方法，为任务添加完成时的回调函数 '''
''' 5.使用 map方法批量提交任务(注意：map方法是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的) '''
''' 6.使用 with :线程池的"自动回收写法"，离开 with 代码块时自动执行 shutdown(wait=True)'''


def work(n, lock):
    with lock:
        print(f'work正在执行{n}....{get_native_id()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    # time.sleep(1)
    return f'我是任务{n}的结果'


if __name__ == '__main__':
    print('------------------start------------------')
    with ThreadPoolExecutor(3) as executor:

    # 创建一个线程池执行器
    # executor = ThreadPoolExecutor(3)
        # 创建线程锁
        lock = RLock()

        # map方法批量提交任务,结果按提交的顺序来
        results = executor.map(work, [1, 2, 3, 4, 5, 6, 7],[lock] * 7)
        print(results)
        print(list(results))

    # 使用 submit 方法提交任务(submit只负责"提交任务"，不会阻塞主线程)
    # f1 = executor.submit(work, 1, lock)
    # f2 = executor.submit(work, 2, lock)
    # f3 = executor.submit(work, 3, lock)
    # f1.add_done_callback(done_func)
    # f2.add_done_callback(done_func)
    # f3.add_done_callback(done_func)
    # f4 = executor.submit(work, 4, lock)
    # f5 = executor.submit(work, 5, lock)
    # f6 = executor.submit(work, 6, lock)
    # f7 = executor.submit(work, 7, lock)

    # 使用 submit 方法提交任务(submit只负责"提交任务"，不会阻塞主线程)
    # futures = [executor.submit(work, n, lock) for n in range(1, 8)]
    # 收集每个线程返回的结果
    # result_list = []


    # 定义一个线程执行成功后的回调函数
    # def done_func(future):
    #     result_list.append(future.result())

    # 开启任务并指定回调函数
    # for index in range(1, 8):
    #     f = executor.submit(work, index, lock)
    #     f.add_done_callback(done_func)

    # 将每个线程的返回结果，存入result_list
    # for f in as_completed(futures):
    #     result_list.append(f.result())

    # shutdown 的作用：不再接收新的任务
    # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕
    # executor.shutdown(wait=True)
    # print(result_list)
    # 打印结果
    # for f in futures:
    #     print(f.result())



    # print(f1.result())
    # print(f2.result())
    # print(f3.result())
    # print(f4.result())
    # print(f5.result())
    # print(f6.result())
    # print(f7.result())

    print('------------------end------------------')
