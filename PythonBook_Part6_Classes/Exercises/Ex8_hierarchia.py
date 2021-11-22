class Animal:
    def speak(self):
        print('test')
    def reply(self):
        self.speak()
class Mammal(Animal):
    def speak(self):
        print('???')

class Cat(Mammal):
    def speak(self):
        print('miau')

class Dog(Mammal):
    def speak(self):
        print('woof')

class Primate(Mammal):
    def speak(self):
        print('hello world')

class Hacker(Primate):
    pass

spot = Cat()
spot.speak()
data = Hacker()
data.speak()
