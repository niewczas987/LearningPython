X=99 #zmienna globalna

def func():
    X=88    #zmienna lokalna dla funkcji 'func'
    pass

def func1(Y):
    Z = X+Y
    print(Z)

func1(1)    #=100, bo X jest zmienną globalną
