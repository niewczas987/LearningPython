class Worker:
    def __init__(self, name, pay):  # inizjalizajca przy tworzeniu
        self.name = name  # self to nowy obiekt. name to nazwisko, a pay to placa
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]  # podzial lancucha znakow na znakach pustych

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)   # uaktualnienie placy w miejkscu


adam = Worker('Adam Malysz',50000)
anna = Worker('Anna Kowalska',15000)

print(adam.lastName())
print(anna.lastName())

anna.giveRaise(.10)                   #uaktualnienie placy o 10% przy uzyciu metody 'giveRaise'
print(anna.pay)
