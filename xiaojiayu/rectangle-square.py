class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height


    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            '''self.name = value
                这里会出现死循环问题（递归）
                这里有两种方法：
                    调用基类的__setattr__;
                    调用字典属性self.__dict__[name] = value
                    
            '''
            # super.__setattr__(self,name,value)
            self.__dict__[name] = value
    def getArea(self):
        return self.width * self.height
    
