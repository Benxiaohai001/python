import time
# It's only the modifier.
def timeslong(func):
    start = time.clock()
    print('It\'s time starting ...')
    func()
    print('It\'s time Ending...')
    end = time.clock()
    return "It's used :%s." %(end - start)

timeslong(func)
