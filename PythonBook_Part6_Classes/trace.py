class wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('śledzenie:',attrname)            #śledzenie pobrania
        return getattr(self.wrapped,attrname)   #delegacaj pobrania

x=wrapper([1,2,3])
x.append(4)
print(x.wrapped)

x=wrapper({'a':1,'b':2})
print(x.keys())