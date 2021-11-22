class Actor:
    def line(self):
        print(self.name,':',repr(self.says()))

class Customer(Actor):
    name = 'klient'
    def says(self):
        return 'To już ekspapuga'

class Clerk(Actor):
    name = 'sprzedawca'
    def says(self):
        return 'nie, wcale nie...'

class Parrot(Actor):
    name = 'papuga'
    def says(self):
        return None

class Scene:
    def __init__(self):
        self.clerk = Clerk()
        self.customer = Customer()
        self.subject = Parrot()
    def action(self):
        self.customer.line()
        self.clerk.line()
        self.subject.line()

x = Scene()
x.action()