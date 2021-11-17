'''
Klasa Spam używając metod klasowych
'''
class Spam:
    numInstances =0
    def __init__(self):
        Spam.numInstances = Spam.numInstances+1
    def printNumInstances(cls):
        print('Liczba utworzonych instancji',cls.numInstances)
    printNumInstances = classmethod(printNumInstances)

# a,b = Spam(), Spam()
# a.printNumInstances()
# Spam.printNumInstances()

class Sub(Spam):
    def printNumInstances(cls):
        print('Smth extra')
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam):
    pass
# x, y = Sub(), Spam()
# x.printNumInstances()
# Sub.printNumInstances()
# y.printNumInstances()
# z = Other()
# z.printNumInstances()

'''
Zliczanie instancji dla każdej z klas z użyciem metod klasowych
'''
class Spam:
    numInstances =0
    def count(cls):
        cls.numInstances = Spam.numInstances+1
    def __init__(self):
        self.count()
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)
x=Spam()
y1, y2 = Spam(), Spam()
z1,z2,z3 = Other(),Other(),Other()

print(x.numInstances,y1.numInstances,z1.numInstances)
print(Spam.numInstances,Sub.numInstances,Other.numInstances)
