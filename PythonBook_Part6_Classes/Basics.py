class C2:
    pass
class C3:
    pass
class C1(C2,C3):
    def setname(self,who):
        self.name = who

I1=C1()
I2=C1()

I1.setname('adam')
I2.setname('małysz')
print(I1.name)
print(I2.name)

class C11(C2,C3):
    def __init__(self,who):
        self.name = who

class FirstClass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

x=FirstClass()
y=FirstClass()
x.setdata('Król Artur')
y.setdata(3.1415)
x.display()
y.display()
class SecondClass(FirstClass):
    def display(self):
        print('Aktualna wartosc = "%s"'%self.data)

z=SecondClass()
z.setdata(42)
z.display()

class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass:%s]'%self.data
    def mul(self, other):
        self.data *= other

a= ThirdClass('abc')
a.display() #Aktualna wartosc = "abc"
print(a)    #[ThirdClass:abc]
b=a+'xyz'
print(b)    #[ThirdClass:abcxyz]
a.mul(3)
print(a)    #[ThirdClass:abcabcabc]

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)