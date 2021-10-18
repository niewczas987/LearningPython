class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

X=Number(5)
Y = X-2
print(Y.data)

#indeksowanie i wycinanie - __getitem__ i __setitem__
class Indexer:
    def __getitem__(self, index):
        return index**2

X=Indexer()
print(X[2])
for i in range(5):
    print(X[i], end=' ')

L=[5,6,7,8,9]
class Indexer2:
    data = [5,6,7,8,9]
    def __getitem__(self, index):
        print('getitem',index)
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
X=Indexer2()
print(X[0],X[2:4])
#iteracja po indeksie
class Stepper:
    def __getitem__(self, i):
        return self.data[i]
X=Stepper()
X.data = 'mielonka'
for item in X:
    print(item,end=' ')

#obiekty iteratorów __iter__ i __next__
class Squares:
    def __init__(self,start,stop):
        self.value = start-1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value ==self.stop:
            raise StopIteration
        self.value +=1
        return self.value**2
for i in Squares(1,5):
    print(i, end=' ')

#wiele iteracji po 1 obiekcie
S = 'ace'
class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset +=2
            return item
class SkipObject:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(I.__next__(),I.__next__(),I.__next__())
    for x in skipper:
        for y in skipper:
            print(x+y)

#testy przynależności
class Iters:
    def __init__(self,value):
        self.data = value
    def __getitem__(self, item):
        print('get[%s]:' % item,end= ' ')
    def __iter__(self):
        print('iter=>',end=' ')
        self.ix = 0
        return self
    def __next__(self):
        print('next:',end=' ')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix +=1
        return item
    def __contains__(self, item):
        print('contains:',end=' ')
        return item in self.data
X=Iters([1,2,3,4,5])
print(3 in X)
for i in X:
    print(i,end=' ')
print()
print([i**2 for i in X])
print(list(map(bin,X)))
I = iter(X)
while True:
    try:
        print(I.__next__(),end=' @ ')
    except StopIteration:
        break

#metody __getattr__ i __setattr__
class Empty:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError(item)
X=Empty()
print(X.age)
#print(X.name) - zgłoszenie Attribute Error

class AccessControl:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value
        else:
            raise AttributeError(item)