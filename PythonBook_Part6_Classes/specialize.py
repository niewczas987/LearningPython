class Super:
    def method(self):
        print('w Super.method')
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('w Replacer.method')

class Extender(Super):
    def method(self):
        print('początek Extender.method')
        Super.method(self)
        print('koniec Extender.method')

class Provider(Super):
    def action(self):
        print('w Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor,Replacer,Extender):
        print('\n'+klass.__name__+'...')
        klass().method()
    print('\nProvider...')
    x=Provider()
    x.delegate()