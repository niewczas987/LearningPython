#przykład argumentow zmienych i niezmiennych
def changer(a,b):
    a=2
    b[0] = 'mielonka'
X=1
L=[1,2]
changer(X,L)
print(X,L)  #1 ['mielonka', 2]

#symulowanie parametrów wyjscia
def f(a,b,c): print(a,b,c)
f(1,2,3)        #dopasowanie op pozycji
f(c=4,b=3,a=1)  #dopasowanie po kluczu
f(1,b=4,c=5)
#wartości domyślne
def f1(a,b=2,c=3): print(a,b,c)
f1(1)   #1 2 3
f1(1,5) #1 5 3
f1(2,c=4)   #2 2 4

#dowolne argumenty
def f2(*args): print(args)  #zebranie w krotkę
f2()
f2(1)
f2(1,2,3,4)


def f3(**args): print(args) #zebranie w słownik
f3()
f3(a=1,b=2,c=3)

def f4(a, *pargs, **kargs): print(a,pargs,kargs)
f4(1,2,3,4,x=2,z=3)

#rozpakowywanie argumentów
def f5(a,b,c,d): print(a,b,c,d)
args = 1,2
args+= 3,4
f5(*args)
args = dict(a=7,b=8,c=9)
args['d']=4
f5(**args)
f5(*(1,2),**{'d':4,'c':4})
f5(1,*(2,3),**{'d':4})
f5(1,c=3,*(2,),**{'d':4})

#argumenty mogące być tylko słowami kluczowymi
def kwonly(a,*b,c):print(a,b,c)
kwonly(1,2,c=3)
kwonly(a=1,c=4)
# kwonly(1,2,3) -> TypeError: kwonly() missing 1 required keyword-only argument: 'c'
#argumenty w formie słownika mogą być jedynie na końcu listy argumentów
def f6(a,*b,c=6,**d): print(a,b,c,d)
f6(1,2,3,c=4,x=5,y=6)   #1 (2, 3) 4 {'x': 5, 'y': 6}

