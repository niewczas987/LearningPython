class Spam:
    numInstances =0
    def __init__(self):
        Spam.numInstances = Spam.numInstances+1
    def printNumInstances(self):
        print('Liczba utworzonych instancji',Spam.numInstances)

a= Spam()
b= Spam()
c= Spam()

a.printNumInstances()
print(Spam.numInstances)

class Methods:
    def imeth(self,x):
        print(self, x)

    def smeth(x):
        print(x)

    def cmeth(cls,x):
        print(cls, x)

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

obj = Methods()
obj.imeth(1)
Methods.imeth(obj,2)
Methods.smeth(99)
obj.smeth(111)  #metody statyczne mogą być wywoływane z instancji
Methods.cmeth(555)
obj.cmeth(89)

'''
Klasa Spam używając metod statycznych
'''
class Spam:
    numInstances =0
    def __init__(self):
        Spam.numInstances = Spam.numInstances+1
    def printNumInstances():
        print('Liczba utworzonych instancji',Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

a=Spam()
b=Spam()
c=Spam()
Spam.printNumInstances()
Spam.printNumInstances()

class Sub(Spam):
    def printNumInstances():
        print('Something extra')
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

Sub.printNumInstances()