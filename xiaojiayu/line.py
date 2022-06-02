
import random as r
import math as m
class Line():
    def __init__(self):
        self.ax = r.randint(0,10)
        self.ay = r.randint(0,10)
        self.bx = r.randint(0,10)
        self.by = r.randint(0,10)
    def getlen(self):
        ab = m.sqrt((self.ax-self.bx)*(self.ax-self.bx) + (self.ay - self.by)*(self.ay-self.by))
        print('ab之间的长度为%d'%ab)
