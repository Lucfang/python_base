""" 单分支 """
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你是成年人')
    print('成年人的世界虽不容易，但很精彩!')
# print('我正在学习python')

""" 双分支 """
if age >= 18:
    print('你是成年人')
else:
    print('你还是个小孩')
    print('好好加油，努力学习，未来可期!')

""" 多分支 """
if age <= 10:
    print('你是儿童')
elif age <= 18:
    print('你是青少年')
elif age <= 60:
    print('你是中登')
else:
    print('你可以退休了')

""" 嵌套分支 """

if age < 12:
    print('你还是个快乐的小孩')
elif 12 <= age <= 18:
    if age <= 15:
        print('你正在上初中')
    elif age <= 18:
        print('你正在上高中')
    else:
        print('你正在上大学')
else:
    print('你已经步入社会了')
