class Cal:
    def __init__(self,value = 37.0):
        self.value = float(value)
    
    def __get__(self,instance,owner):
        return self.value

    def __set__(self,instance,value):
        self.value = value


class Fath:
    
    def __get__(self,instance,owner):
        return instance.cal * 1.8 + 32

    def __set__(self,instance,value):
        instance.cal = (value - 32) / 1.8


class Tempture:
    # def __init__(self,cal = 37.0):
    #   self.cal = cal

    cal = Cal()
    fath = Fath()
