"""
经常用到的算法：递归
两个条件：
    存在自身调用自身；
    存在终止循环的条件；
"""

def f(x):
    if x > 0:
        return x + f(x - 1) # 自身调用自身
    return 0  # 终止条件



def f_jiecheng(x):
    """
    求n！
    """
    if x > 0:
        return x * f_jiecheng(x - 1)

    return 1
if __name__ == "__main__":    
    print(f(3))
    print(f_jiecheng(3))