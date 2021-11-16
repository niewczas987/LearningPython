class limiter(object):
    __slots__ = ['age','name','job']

x= limiter()
x.age = 40
print(x.age)

class E:
    __slots__ = ['c','d']
class D:
    __slots__ = ['a','__dict__']
X=D()
X.a = 1
X.b = 2
X.c = 3
print(E.__slots__)
print(D.__slots__)
print(X.__slots__)
print(X.__dict__)