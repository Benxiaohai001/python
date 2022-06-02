def something(f):
    print('Calling f()!')
    f()
    print('Calling over...')



@something
def f():
    print('I love PengJing...')
