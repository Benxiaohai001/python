import time


# 修饰符
def timeslong(func):
    def call():
        start = time.process_time()
        print('It\'s time starting ...')
        func()
        print('It\'s time ending...')
        end = time.perf_counter()
        return "It's used:%s."%(end-start)
    return call


# function itself
# Try my best using English.
@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i +1
        print(y)
    return y



print(f())
