class Person:
    def __init__(self,name):
        self._name = name
    def getName(self):
        print('...pobieranie...')
        return self._name
    def setName(self,value):
        print('...modyfikacja...')
        self._name = value
    def delName(self):
        print('...usuniecie...')
        del self._name
    name = property(getName,setName,delName,'Dokumentacja właściwości name')

# using decorators
class Person:
    def __init__(self,name):
        self._name = name
@property
def name(self):
    "Dokumentacja właściwości name"
    print('...pobieranie...')
    return self._name
@name.setter
def name(self,value):
    print('...modyfikacja...')
    self._name = value

@name.deleter
def name(self):
    print('...usuniecie...')
    del self._name




if __name__ == '__main__':
    bob = Person('Rob Green')
    print(bob.name)
    bob.name = 'Rob A. Green'
    print(bob.name)
    del bob.name
    print('-'*20)
    anna = Person('Ann Red')
    print(anna.name)
    print(Person.name.__doc__)