"""文件操作：读取文件"""

'''
python中操作文件的标准流程：
1.创建【文件对象】
2.操作文件(读取、写入等)
3.关闭文件

文件操作的核心——open函数：它可以打开或创建文件，且支持多种操作模式，返回值是【文件对象】
open函数最常用的三个参数如下：
1. file:要操作的文件路径
2. mode:文件的打开模式 r:read w:write
        r：读取(默认值)
        w：写入，并先截断文件
        x：排他性创建，如果文件已存在则创建失败
        a：打开文件用于写入，如果文件存在则在文件末尾追加内容
        b：二进制模式
        t：文本模式(默认值)
        +：打开用于更新(读取与写入)
3. encoding:字符编码
'''

'''
读取操作1：使用【文件对象】的read方法，读取文件中的内容：
read方法说明：
1.read(size)中的size是可选参数
    若不传递size参数，表示：读取文件中所有的内容(注意内存占用!)
    若传递了size参数：表示：读取文件中指定个数的字符，或指定大小的字节
2.read会从上一次read的位置继续读取(指针思想)，若到达文件末尾后继续读取，将返回空字符串    
'''

# region
# 1.创建【文件对象】
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# file = open('a.txt', 'rt', encoding='utf-8')
# file = open('E:/python/test.py','rt', encoding='utf-8')
# 2.操作文件(读取、写入等)
# result = file.read()
# print(result)

# 多次调用read去逐步读取问价内容
# r1 = file.read(10)
# print(r1)
# print(repr(r1))
# r2 = file.read(10)
# print(r2)
# print(repr(r2))


# 用循环配合多次read(对内存友好)
# while True:
#     result = file.read(10)
#     if result == '':
#         break
#     print(result,end='')
# 3.关闭文件
# file.close()

#endregion

'''
读取操作2：使用文件对象的 readline 方法，读取文件中的一行
readline方法说明：
1.readline(size)中 size 是可选参数
    若不传递 size 参数，表示：读取当前这一行所有的内容
    若传递了 size 参数，表示：读取当前行时，最多能读取的字符数或字节数(size不是行数)
2.readline方法，也是从上一次位置继续读取，若到达文件末尾后继续读取，也是返回空字符串    
'''

# region
# 1.创建【文件对象】
# file = open('a.txt', 'rt', encoding='utf-8')
# 2.操作文件(读取、写入等)
#
# 逐行读取
# r1 = file.readline(20)
# # print(r1,end='')
# # print(repr(r1))
# print(r1.strip())
# r2 = file.readline()
# print(r2)
#
# 循环读取
# while True:
#     line = file.readline()
#     if line == '':
#         break
#     print(line.strip())
# 3.关闭文件
# file.close()
# endregion

'''
读取操作3：使用for循环直接遍历文件对象
'''
# region
# 1.创建【文件对象】
# file = open('a.txt', 'r',encoding='utf-8')
# 2.操作文件(读取、写入等)
# for line in file:
#     print(line.strip())
# 3.关闭文件
# file.close()
# endregion

'''
读取操作4：使用文件对象的 readlines 方法，一次性按"行"读完，返回一个列表
readlines方法说明：
1.readlines(hint) 中 hint 是可选参数
    若不传递 hint 参数，表示：读取当前文件的所有行
    若传递了 hint 参数，表示：期望读取的【字符个数 或 字节数上限】(hint不是行数)
2.注意：由于 readlines 是一次性读取文件的所有内容，所以不适合读取体积较大的文件    
'''

# region
# 1.创建【文件对象】
# file = open('a.txt', 'r',encoding='utf-8')
# 2.操作文件(读取、写入等)
# result = file.readlines()
# print(result)
# file.close()
# 3.关闭文件
# file.close()
# endregion

'''
⭐最佳实践：使用 with 上下文管理器，结合for循环遍历，逐行读取文件
'''

with open('a.txt','rt',encoding='utf-8') as file:
    for line in file:
        print(line,end='')

