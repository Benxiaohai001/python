import time

class timeslong(object):
    def __init__(self,func):
        self.f = func
    def __call__(self):
        start = time.perf_counter()
        print('It\'s time starting!')
        print(start)
        self.f()
        print('It\'s time ending!')
        end = time.perf_counter()
        print(end)
        return 'It\'s used:%s .'%(end - start)




@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)

    return y


print(f())
