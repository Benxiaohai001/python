'''
继承：
随机数
    重写
    当__init__方法被重写：
        调用未绑定的父类方法,（必须有参数，参数是子类对象）
        使用super方法（可以不用参数，而且会递归调用）


    多重继承：
        
'''



import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
        print("我的初始位置是：%d %d"%(self.x,self.y))
    def move(self):
        self.x -= 1
        print("我的当前位置是：%d %d"%(self.x,self.y))
class GoldFish(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("肚子饿了，就是要吃东西！！！")
        else:
            print("暂时不饿。。。")



class Base1:
    def fool1(self):
        print('我是fool1，我为Base1代言！！！')

class Base2:
    def fool2(self):
        print('我是fool2，我为Base2代言！！！')

class B(Base1,Base2):
    pass
