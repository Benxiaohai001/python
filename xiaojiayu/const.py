
class const:
    def __setattr__(self,name,value):
        if name in self.__dict__:
            raiseTypeError('常量无法改变！')
        if not name.issuper():
            raise TypeError('常量名必须由大写字母组成！！！')
        self.__dict__[name] = value


import sys
sys.modules[__name__] = const()
