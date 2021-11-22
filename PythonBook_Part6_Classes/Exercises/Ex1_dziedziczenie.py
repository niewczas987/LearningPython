# Ex.1 Dziedziczenie
class Adder:
    def add(self, x,y):
        print('Not implemented')
    def __init__(self,data=[]):
        self.data = data
    def __add__(self, other):
        return self.add(self.data,other)

class ListAdder(Adder):
    def add(self,list1= [], list2=[]):
        return list1 + list2

class DictAdder(Adder):
    def add(self, dict1={}, dict2={}):
        dict1.update(dict2)
        return dict1

x = Adder()
y = ListAdder()
z = DictAdder()

x.add(5,6)
print(y.add([1,2,3],[4,5,6]))
print(z.add(dict(a=1),dict(b=2)))

x=ListAdder([1])
print(x+[2])
