from employees import PizzaRobot, Server

class Customer:
    def __init__(self,name):
        self.name = name
    def order(self,server):
        print(self.name,'zamawia od',server)
    def pay(self,server):
        print(self.name,'placi za zamowienie',server)

class Oven:
    def bake(self):
        print('Piec piecze')

class PizzaShop:
    def __init__(self):
        self.server = Server('Ernest')
        self.chef = PizzaRobot('Robert')
        self.oven = Oven()
    def Order(self,name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzaShop()
    scene.Order('Marek')
    print('...')
    scene.Order('Olek')
