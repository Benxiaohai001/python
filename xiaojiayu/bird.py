class Bird():
    def __init__(self):
        print('我是一只鸟。。。')
    def fly(self):
        print('我会飞。。。')
    def eat():
        print('我吃的很少。。。')


class Maque(Bird):
    def __init__(self):
        super().__init__()
        print('我是一只麻雀。。。')




class Qie(Bird):
    def __init__(self):
        super().__init__()
        print('我是一只企鹅。。。')

    def fly(self):
        print('我不会飞。。。。')
