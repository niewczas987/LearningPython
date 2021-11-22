#przeciążanie operatorów
class MyList:
    def __init__(self, data):
        self.wrapped = []
        for x in data:
            self.wrapped.append(x)
    def __add__(self, other):
        return MyList(self.wrapped + other)
    def __mul__(self, other):
        return MyList(self.wrapped * other)
    def __getitem__(self, item):
        return self.wrapped[item]
    def __len__(self):
        return len(self.wrapped)
    def __getslice__(self,low, high):
        return MyList(self.wrapped[low:high])
    def append(self,node):
        self.wrapped.append(node)
    def __getattr__(self, item):
        return getattr(self.wrapped,item)
    def __repr__(self):
        return repr(self.wrapped)

if __name__=='__main__':
    x= MyList('mielonka')
    print(x)
    print(x[2])
    print(x[1:])
    print(x+['jajka'])
    print(x*3)
    x.append('a')
    x.sort()
    for c in x:
        print(c,end=' ')