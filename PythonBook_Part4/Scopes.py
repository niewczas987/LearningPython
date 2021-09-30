X=99 #zmienna globalna

def func():
    X=88    #zmienna lokalna dla funkcji 'func'
    pass

def func1(Y):
    Z = X+Y
    print(Z)

func1(1)    #=100, bo X jest zmienną globalną

#built-ins
import builtins
print(dir(builtins))

#global
X=88
print(X)
def func2():
    global X
    X=99
func2()
print(X)

var =99
def local():
    var = 0
def glob1():
    global var
    var +=1
def glob2():
    var = 0
    import Scopes
    Scopes.var +=1
def glob3():
    var=0
    import sys
    glob = sys.modules['Scopes']
    glob.var +=1
def test():
    print(var)
    local()
    glob1()
    glob2()
    glob3()
    print(var)

print('Wykonanie test:')
test()

#zakresy, a domyslne wartości argumentow
def makeAction():
    acts = []
    for i in range(5):
        acts.append(lambda x: i**x)
    return acts
acts = makeAction()
print(acts[0])
print(acts[0](2))   #wszystkei wartości to 4**2, czyli potęga ostatniego i -> WYJĄTEK!
print(acts[2](2))

#żeby działało poprawnie
def makeAction():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i**x)
    return acts
acts = makeAction()
print(acts[0])
print(acts[0](2))
print(acts[2](2))


#non-local
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label,state)
        state +=1
    return nested

F = tester(0)
F('mielonka')
F('szynka')
F('jajka')
G=tester(42)
G('jajka')
F('bekon')

#zapisane jako klasa
print('Przepisanie programu jako klasa')
class tester:
    def __init__(self,start):
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state +=1

F = tester(0)
F.nested('mielonka')
F.nested('szynka')
F.nested('jajka')
G=tester(42)
G.nested('jajka')
F.nested('bekon')

#stan i atrybuty funkcji
def tester1(start):
    def nested(label):
        print(label,nested.state)
        nested.state +=1
        nested.state = start
        return nested
