"""
经常用到的算法：递归
两个条件：
    存在自身调用自身；
    存在终止循环的条件；
缺点：
    栈溢出：数据量大的时候会出现这种情况；操作系统会自动终止这种操作；
        解决办法：人为设置递归的深度
    重复计算：例如斐波那契数列；如果用递归的话会有很多重复的计算；这样就不适合用递归了；
        解决办法：用内存空间的变量存储重复计算的值；
    # image.png
    
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