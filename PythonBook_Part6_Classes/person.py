class Person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1+ percent))
    def __str__(self):
        return '[Person: %s,%s]'%(self.name, self.pay)

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