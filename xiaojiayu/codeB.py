class CodeB:
    def classmethodf(f):
        print('Calling class method f()!')
        f = classmethod(f)
        print('Calling over!!!')


    @classmethodf
    def foo():
        pass
