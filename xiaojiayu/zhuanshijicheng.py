'''
砖石继承问题：
    使用未绑定的父类方法。会不止一次的调用基类方法
    使用super()方法可以解决上述问题。  但是需要注意的是，super() 方法之后不用传递参数
    


'''


class A():
    def __init__(self):
        print('进入A。。。')
        print('离开A。。。')

class B(A):
    def __init__(self):
        print('进入B。。。')
        # A.__init__(self)
        super().__init__()
        print('离开B。。。')



class C(A):
    def __init__(self):
        print('进入C。。。')
        # A.__init__(self)
        super().__init__()
        print('离开C。。。')



class D(B,C):
    def __init__(self):
        print('进入D。。。')
        # B.__init__(self)
        # C.__init__(self)
        super().__init__()
        print('离开D。。。')
