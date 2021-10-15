from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Tworzy i przetwarza rekordy osób
    """
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1+ percent))

class Manager(Person):
    """
    Dostosowana do własnych potrzeb klasa Person ze specjalnymi wymaganiami
    """
    def __init__(self,name,pay):
        Person.__init__(self,name,'manager',pay)
    def giveRaise(self,percent,bonus=.10):
        Person.giveRaise(self,percent+bonus)

class Department:
    def __init__(self,*args):
        self.members = list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaise(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)


#testy
if __name__ == '__main__':
    bob = Person('Robert Green')
    anna = Person('Ann Red', 'Programmer', 5000)
    print(bob.name, bob.pay)
    print(anna.name, anna.job, anna.pay)
    print(bob.name.split()[-1])
    print(bob.lastName(), anna.lastName())
    print(anna.pay)
    anna.giveRaise(.20)
    print(anna.pay)
    print(bob, anna)
    tom = Manager('Tom Black',50000)
    tom.giveRaise(.10)
    print(tom)
    print('Wszystkie osoby:')
    for object in (bob,tom,anna):
        object.giveRaise(.10)
        print(object)

    development = Department(bob, anna)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()