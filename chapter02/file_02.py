""" 循环 """
''' while '''
n = 1
while n <= 10:
    print('你好啊')
    n += 1

''' for '''
for i in range(10):  # [0,10)
    print(i)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()
