class codeA:
    def staticize(f):
        print('Calling static method foo!!!')
        f = staticmethod(f)
        #f = staticmethod(f()) () what mean? 
        print('Calling over!')
        return None
    
    @staticize# @ has their function.
    def foo():
        pass
    
    
        
