class Employee:
    def __init__(self,name,salary = 0):
        self.name = name
        self.salary = salary
    def giveRaise(self,percent):
        self.salary = self.salary +(self.salary * percent)
    def work(self):
        print(self.name,'robi różne rzeczy')
    def __repr__(self):
        return "<Pracownik: imię = %s, wynagrodzenie=%s>"%(self.name,self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,5000)
    def work(self):
        print(self.name,'przygotowuje jedzenie')

class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,4000)
    def work(self):
        print(self.name,'obsługuje klienta')

class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):
        print(self.name,'przygotowuje pizze')

if __name__ == '__main__':
    bob = PizzaRobot('robert')
    print(bob)
    bob.work()
    bob.giveRaise(0.2)
    print(bob)

    for klass in Employee,Chef,Server,PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()