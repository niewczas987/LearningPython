#funkcje generatorów w działaniu
def gensquares(N):
    for i in range(N):
        yield i**2

for i in gensquares(5):
    print(i, end=' : ')

x=gensquares(4)
print(x)    #x jest obiektem generatora
print(next(x))
print(next(x))
print(next(x))
print(next(x))  #po przejściu wsyzstkich dostajemy wyjątek StopIteration

#instrukcja send
def gen():
    for i in range(10):
        X=yield i
        print(X)
G=gen()
print(next(G))
G.send(88)

#wyrażenia generatorów
print([x**2 for x in range(4)])
G= (x**2 for x in range(4))
print(next(G))
print(next(G))
print(next(G))
#podsumowanie
print([x*x for x in range(10)]) #lista składana
print((x*x for x in range(10))) #generator
print({x*x for x in range(10)}) #zbiór skadany
print({x:x*x for x in range(10)})   #słownik składany