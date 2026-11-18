# 订单最大金额
max_order_amount = 1000000

# 创建订单
def create_order():
    print('订单创建成功')

# 关闭订单
def cancel_order():
    print('订单关闭成功')

# 提示函数
def show_info():
    print('我是来自【订单模块】的提示')

__all__ = ['create_order', 'cancel_order', 'show_info']

print('我是order模块打印的内容',__name__)

# 测试代码
if __name__ == '__main__':
    create_order()
    cancel_order()