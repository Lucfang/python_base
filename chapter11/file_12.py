"""多进程 和 多线程 """
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

'''
多进程 和 多线程 怎么选？

适合使用多进程： 
CPU 密集型：大部分时间花在"算"上
如：图像处理、视频编码/解码、数值计算、模型训练 

适合使用多线程：
I/O 密集型任务：大部分时间花在"等"上
如：文件I/O、网络请求、操作数据库
'''

# CPU密集型
def cpu_task(n):
    print(f'任务{n}开始了')
    total = 0
    for i in range(10000000):
        total += i * i
    return total

def copy_file(index):
    with open('E:/资料/pdfjs-2.5.207-dist.zip','rb') as src, open(f'a_副本{index}.zip','wb') as dst:
        while True:
            data = src.read(1024 * 1024)
            if not data:
                break
            dst.write(data)

if __name__ == '__main__':
    # print('====多进程完成【CPU密集型任务】====')
    # start = time.time()
    # # 开启四个进程进行计算
    # with ProcessPoolExecutor(4) as executor:
    #     list(executor.map(cpu_task, [1, 2, 3, 4]))
    # end = time.time() - start
    # print(f'多进程总耗时：{end}秒')

    # print('====多线程完成【CPU密集型任务】====')
    # start = time.time()
    # # 开启四个进程进行计算
    # with ThreadPoolExecutor(4) as executor:
    #     list(executor.map(cpu_task, [1, 2, 3, 4]))
    # end = time.time() - start
    # print(f'多进程总耗时：{end}秒')

    # print('====多进程完成【I/O密集型任务】====')
    # start = time.time()
    # # 开启四个进程进行计算
    # with ProcessPoolExecutor(4) as executor:
    #     for i in range(4):
    #         executor.submit(copy_file, i)
    # end = time.time() - start
    # print(f'多进程总耗时：{end}秒')

    print('====多线程完成【I/O密集型任务】====')
    start = time.time()
    # 开启四个进程进行计算
    with ThreadPoolExecutor(4) as executor:
        for i in range(4):
            executor.submit(copy_file, i)
    end = time.time() - start
    print(f'多进程总耗时：{end}秒')

